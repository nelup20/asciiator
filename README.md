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

## Flags

|Flag|Description|
|:---|:----------|
|-i  |Modify the file **
inplace**. The original file will be transformed to ASCII and no new output file will be generated.|
|-h  | Display the help documentation                                                                                      |
|--reduction=x|Reduce the output by a factor of x. Example: --reduction=2 to get half the amount of pixels in ASCII 