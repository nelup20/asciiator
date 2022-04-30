import sys

from input import Input, InputType
from options import Options

# TODO: multiple input files (array of tuples)
options: Options = {
    "inplace": False,
    "input": None
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in enumerate(sys.argv):
            if arg[0] == 0:
                continue

            if Input.is_input_file(arg[1]):
                print(f'Found the input file {arg[1]}')
                continue

            match arg:
                case "-h":
                    print("TODO. Sorry can't help ya right now.")
                case _:
                    print(f"Argument #{arg[0]} is invalid: {arg[1]}. Use -h for help.")

    else:
        print("No arguments provided. Use -h for help.")