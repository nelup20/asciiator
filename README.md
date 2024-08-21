# Asciiator
A CLI tool to turn images and videos into ASCII art.

* [Examples](#examples)
* [Installation](#installation)
* [Usage and Options](#usage-and-options)
  * [Usage](#usage)
  * [Supported formats:](#supported-formats)
  * [Optional flags](#optional-flags)
* [Local development](#local-development)
  * [Requirements/Dependencies](#requirementsdependencies)
  * [Running](#running)
* [Contributing and issues](#contributing-and-issues)

## Examples
|                                                 Input                                                 |                                                Output                                                 |
|:-----------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------:|
|                                  ![](./examples/example_1_input.jpg)                                  |                                 ![](./examples/example_1_output.jpg)                                  |
| <video src="https://github.com/user-attachments/assets/64d684ac-0a2a-442c-8058-128d80618d24"></video> | <video src="https://github.com/user-attachments/assets/43829418-012a-489a-8eca-ef3136930ae5"></video> |

## Installation
The binaries for Asciiator can be found under [releases](https://github.com/nelup20/asciiator/releases). The only requirement is [FFmpeg](https://ffmpeg.org/) which needs to be installed & in your PATH in order to convert videos.

## Usage and Options
### Usage
Simply execute with the path to your input files
```sh
asciiator "./your_image.jpg" "./your_image_2.jpg"
```

and asciiator will transform the content/pixels to ASCII and save to a new file.

### Supported formats:

- [x] Image:
   - [x] JPEG
   - [x] PNG
   - [x] WEBP
   - [x] BMP
   - [x] TIFF
   - [x] GIF
- [x] Video:
   - [x] MP4
   - [x] AVI
   - [x] FLV
   - [x] MOV
   - [x] WEBM
   - [x] WMV
   - [x] MKV
   - [x] MPEG

### Optional flags

| Flag                          | Description                                                                                                                                                                                                                    |
|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --inplace                     | Modify the file **inplace**. The original file will be transformed to ASCII and no new media/output file will be generated.                                                                                                    |
| --help                        | Display the help documentation                                                                                                                                                                                                 |
| --inverted                    | Invert the colors for the background and text. By default, the background color is black (0) and the text color is white (255). If --inverted is present, the background will be white and the text color will be black.       |
| --text_file                   | Save the transformed ASCII art to a .txt file as well (only applicable when the input is a image)                                                                                                                              |
| --reduction x                 | Reduce the output by a factor of x (int). Default value: 4. Example: --reduction 2 to convert half of the pixels to ASCII                                                                                                      |
| &#x2011;&#x2011;output_path x | Specify the output path where all new files will be created. By default it's the current directory. **Warning:** if the --inplace flag is present, then this flag will be ignored, so the original absolute path will be used. |
| --version                     | Display the version of Asciiator                                                                                                                                                                                               |

## Local development
This project uses [Poetry](https://python-poetry.org/) as its package/dependency manager & [FFmpeg](https://ffmpeg.org/) for converting videos.
Once both are installed, install the project's dependencies & dev dependencies via:
```sh
poetry install
```

You should now be able to run the project locally.

### Requirements/Dependencies

- Python 3.10+
- FFmpeg 4.4.1+
- Poetry 1.0.0+

### Running
```sh
python -m src.main "path_to_your_image"
```

Or if you want to run via Docker:
```sh
docker build . -t asciiator
```
```sh
docker run -it --entrypoint=bash asciiator
```
Inside the container:
```sh
python -m src.main "path_to_your_image"
```

## Contributing and issues
Please create an issue with an applicable label instead of mailing me directly and include any logs if appropriate. Asciiator stores logs in your home directory at `~/.asciiator/logs`\
For small things like typo's feel free to create a PR directly without an issue. 
