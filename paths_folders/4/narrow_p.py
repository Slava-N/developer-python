import os
import glob
import os.path
import subprocess

program_to_use = 'sips'
operation = '--resampleWidth'
operation_argument = '200'
input_photo_folder = "Source"
output_photo_folder = "Result"

def create_file_list(folder_name):
    files = glob.glob(os.path.join(folder_name, '*.jpg'))
    return files

def create_result_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def narrow_photo(input_photo, output_photo):
    subprocess.run(['sips', '--resampleWidth', '200', os.path.join(input_photo_folder, input_photo),
                    '--out', os.path.join(output_photo_folder, output_photo)])


def execute_multiple_corrections(files):
    for input_photo in files:
        photo_name = os.path.basename(input_photo)
        print(photo_name)
        narrow_photo(photo_name, photo_name)

create_result_folder(output_photo_folder)

execute_multiple_corrections(create_file_list(input_photo_folder))
