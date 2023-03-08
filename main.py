from pathlib import Path
import ffmpeg
import click

# def convert_to_mp4(start_dir, file):
#     name, ext = os.path.splitext(file)
#     folder_name = "Converted"
#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
#     new_file_name = name + ".mp4"
#     ffmpeg.input(file).output(
#         os.path.join(folder_name, new_file_name)).run()
#     print("Finished converting {}".format(file))


# start_dir = os.getcwd()

# for path, folder, files in os.walk(start_dir):
#     for file in files:
#         if file.endswith('.mkv'):
#             print("Found file: %s" % file)
#             convert_to_mp4(start_dir, file)
#         else:
#             pass


def convert_video(file, format, path_to_save):

    file_name = Path(file).stem
    new_file = file_name + f".{format}"

    if path_to_save:
        file_name = Path(file).stem
        new_file_path = Path(path_to_save, file_name).stem
        new_file = new_file_path + f".{format}"

    ffmpeg.input(file).output(new_file).run()

# def convert_to_mp4(start_dir, file):
#     name, ext = os.path.splitext(file)
#     folder_name = "Converted"
#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
#     new_file_name = name + ".mp4"
#     ffmpeg.input(file).output(
#         os.path.join(folder_name, new_file_name)).run()
#     print("Finished converting {}".format(file))


format_list = [
    "mp4", "mp3", "avi", "mkv"
]


@click.command()
@click.argument('file')
@click.option('--video_format', type=click.Choice(format_list), prompt="Choose to which format to convert video", default=format_list[0], help='Format to convert video to')
@click.option('--path_to_save', type=click.Path(exists=True), default=None, help='Path to save video to')
def convert(file, video_format, path_to_save):
    convert_video(file, video_format, path_to_save)


@click.command()
@click.argument('file')
@click.option('--overlay_image', type=click.Path(exists=True), default=None, help='Image to add onto video')
def overlay(file, overlay_image):
    overlay_file = ffmpeg.input(overlay_image)
    in_file = ffmpeg.input(file)
    ffmpeg.concat(in_file).overlay(overlay_file).drawbox(
        4, 4, 4, 4, color='red', thickness=1).output('out.mp4').run()

    # convert()
overlay()


# @click.command()
# @click.argument('argum')
# @click.option('--count', type=click.Choice(["2", "20","32"]), prompt="Choose", default=2, help='Number of count.')
# def test(argum, count):
#     print(argum)
#     print(count)

# test()
