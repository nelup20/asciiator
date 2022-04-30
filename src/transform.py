
# TODO: actual transformation
def transform_jpg(file):
    file_data = file.get_data()
    for i, byte in enumerate(file_data):
        if byte == 146:
            file_data[i] = 0

    file.create_new_file(file_data)

def transform_mp4(file):
    print(file.get_data())