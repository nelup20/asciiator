from os import makedirs, path

from .options import Options


def main():
    options = Options()

    if not options.inplace and not path.exists(options.output_path):
        makedirs(options.output_path)

    for file in options.input:
        file.transform(options)


if __name__ == "__main__":
    main()
