# asciiator
A tool to turn image and video files into ASCII art.

Simply execute with the input file as the first argument
```sh
asciiator input.jpg
```

and asciiator will transform the content/pixels to ASCII and save to a new file.

Supported input/output formats:

- [ ] Image:
   - [x] JPEG
   - [x] PNG
- [ ] Video:
   - [ ] MP4

## Requirements/Dependencies

- Python 3.10+
- Pillow
- FFmpeg
- Poetry
- Black
- Mypy

## Optional flags

| Flag              | Description                                                                                                                                                                                                                    |
|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -inplace          | Modify the file **inplace**. The original file will be transformed to ASCII and no new media output file will be generated.                                                                                                    |
| -help             | Display the help documentation                                                                                                                                                                                                 |
| -inverted         | Invert the colors for the background and text. By default, the background color is white (255) and the text color is black (0). If -inverted is present, the background will be black and the text color will be white.        |
| -text_file        | Save the transformed ASCII art to a .txt file as well                                                                                                                                                                          |
| --reduction=x     | Reduce the output by a factor of x (int). Default value: 1 (no reduction). Example: --reduction=2 to get half the amount of pixels in ASCII                                                                                    |
| --output_path="x" | Specify the output path where all new files will be created. By default it's the current directory. **Warning:** if the -inplace flag is present, then this flag will be ignored, so the original absolute paths will be used. |