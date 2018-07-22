import os
import glob
import os.path
import subprocess


# sips --resampleWidth 200 myphoto.jpg
# subprocess.run(['sips', '--resampleWidth', 'new_width', '--out',
#                   os.path.join(directory_out,file_name), os.path.join(directory_source,file_name)])



program_to_use = 'sips'
operation = '--resampleWidth'
operation_argument = '200'
input_photo_folder = "Source"
output_photo_folder = "Result"

def create_file_list(folder_name):
    files = glob.glob(os.path.join(folder_name, '*.jpg'))
    return(files)

def create_result_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def narrow_photo(program_to_use, input_photo, operation, operation_argument, output_photo):
    subprocess.run(['sips', '--resampleWidth', '200', os.path.join(input_photo_folder,input_photo), '--out', os.path.join(output_photo_folder,output_photo)])


def execute_multiple_corrections(program_to_use, operation, operation_argument, files, output_photo_folder):
    for input_photo in files:
        photo_name_list = input_photo.split('/')
        photo_name = photo_name_list[1]
        # output_photo = os.path.join(photo_name)
        narrow_photo(program_to_use, photo_name, operation, operation_argument, photo_name)

create_result_folder(output_photo_folder)

execute_multiple_corrections(program_to_use,
                operation,
                operation_argument,
                create_file_list(input_photo_folder),
                output_photo_folder
                )
