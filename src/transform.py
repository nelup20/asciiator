from random import randint


# TODO: actual transformation
def transform_jpg(file):
    new_circle_color = (randint(0, 255), randint(0, 255), randint(0, 255))

    image_data = file.get_data()
    new_image_data = list(map(lambda pixel: (0, 0, 0) if pixel == (255, 255, 255) else new_circle_color, image_data))

    file.create_new_file(new_image_data)


def transform_mp4(file):
    print(file.get_data())
