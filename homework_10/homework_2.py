# import re
import os

source_file_path = input('Enter path to source file: ')
destination_folder_path = input('Enter path to destination folder: ')

with open(source_file_path, 'rb') as file:
    # with open(destination_folder_path + re.compile('[/\\\]').split(source_file_path)[-1], 'wb') as file_copy:
    if not os.path.exists(destination_folder_path):
        os.makedirs(destination_folder_path)
    with open(os.path.join(destination_folder_path, os.path.split(source_file_path)[-1]), 'wb') as file_copy:
        file_copy.write(file.read())
