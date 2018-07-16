import os

source_file_path = input('Enter path to source file: ')

size = os.stat(source_file_path).st_size

print('File --{}-- size is:\n'
      '{} bytes\n'
      '{} megabytes\n'
      '{} gigabytes'.format(os.path.split(source_file_path)[-1], size, size / 1048576, size / 1073741824))
