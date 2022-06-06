# asciiator
A tool to turn image and video files into ASCII art.

Simply execute with the input file as the first argument
```sh
asciiator input.jpg
```

and asciiator will transform the content/pixels to ASCII and save to a new file.

Supported input/output formats:

- [ ] Image:
   - [ ] JPEG
- [ ] Video:
   - [ ] MP4

## Requirements

- Python 3.10+
- Pillow

## Optional flags

| Flag                | Description                                                                                                                                                                                                                                |
|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -i                  | Modify the file **inplace**. The original file will be transformed to ASCII and no new output file will be generated.                                                                                                                      |
| -h                  | Display the help documentation                                                                                                                                                                                                             |
| --reduction=x       | Reduce the output by a factor of x (int). Default value: 1 (no reduction). Example: --reduction=2 to get half the amount of pixels in ASCII                                                                                                |
| --inverted_colors=x | Invert the colors for the background and text. By default (--inverted_colors=false), the background color is white (255) and the text color is black (0). If set to "true", the background will be black and the text color will be white. |
| --output_path=x     | Specify the output path where all new files will be created. By default it's the current directory.                                                                                                                                        |