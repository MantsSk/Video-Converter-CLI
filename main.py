import os
import ffmpeg


def convert_to_mp4(start_dir, file):
    name, ext = os.path.splitext(file)
    folder_name = "Converted"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    new_file_name = name + ".mp4"
    ffmpeg.input(file).output(
        os.path.join(folder_name, new_file_name)).run()
    print("Finished converting {}".format(file))


start_dir = os.getcwd()

for path, folder, files in os.walk(start_dir):
    for file in files:
        if file.endswith('.mkv'):
            print("Found file: %s" % file)
            convert_to_mp4(start_dir, file)
        else:
            pass
