import sys

from file import File, FileType
from options import Options
from transform import transform_jpg, transform_mp4

options: Options = {
    "inplace": False,
    "input": [],
    "reduction_factor": 1
}


def init():
    if len(sys.argv) > 1:
        for arg in enumerate(sys.argv):
            if arg[0] == 0:
                continue

            if File.is_input_file(arg[1]):
                options["input"].append(File(arg[1]))
                continue

            if "--reduction=" in arg[1]:
                options["reduction_factor"] = int(arg[1].split("=")[1])
                continue

            match arg[1]:
                case "-h":
                    print("TODO. Sorry can't help ya right now.")
                case _:
                    print(f"Argument #{arg[0]} is invalid: {arg[1]}. Use -h for help.")

    else:
        print("No arguments provided. Use -h for help.")


if __name__ == "__main__":
    init()

    for file in options["input"]:
        match file.type:
            case FileType.Image:
                transformed_data = transform_jpg(file, options['reduction_factor'])
                File.create_new_file(transformed_data, f"./{file.name}_asciiator.txt")
            case FileType.Video:
                transform_mp4(file)
            case _:
                print(f"Invalid file type for file: {file.relative_path}")
