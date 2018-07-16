import os.path

with open(os.path.join('res', 'photo.jpg'), 'rb') as file:
    with open(os.path.join('res', 'photo_copy.jpg'), 'wb') as file_copy:
        file_copy.write(file.read())

