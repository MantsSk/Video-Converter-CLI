import os
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
    old_file_path = os.path.splitext(file)[0]
    new_file_path = old_file_path + f".{format}"

    if path_to_save:
        file_name = os.path.split(new_file_path)[1]
        print(file_name)
        new_file_path = os.path.join(path_to_save, file_name)

    ffmpeg.input(file).output(new_file_path).run()

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
def main(file, video_format, path_to_save):
    convert_video(file, video_format, path_to_save)


main()

# @click.command()
# @click.argument('argum')
# @click.option('--count', type=click.Choice(["2", "20","32"]), prompt="Choose", default=2, help='Number of count.')
# def test(argum, count):
#     print(argum)
#     print(count)

# test()
