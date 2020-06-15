# Recolor
Map and transform "allRGB" images

Use like this: `python3 recolor.py 1.png 2.png 3.png`

The script looks at the first two images and it creates a map describing the difference in location of each pixel, then it applies the same movements to the pixels of the third image.

![Diagram](https://github.com/jankais3r/Recolor/blob/master/diagram.png)

Pixel map:
```
{(0, 0): (0, 1), (0, 1): (1, 0), (0, 2): (2, 0),
 (1, 0): (2, 1), (1, 1): (2, 2), (1, 2): (0, 0),
 (2, 0): (1, 2), (2, 1): (1, 1), (2, 2): (0, 2)}
```

Requirements:
- Pictures 1 and 2 have to have a resolution of 4096x4096 with no repeating colors (see [allRGB](https://allrgb.com)'s gallery of such images).
- Picture 3 has to have a resolution of 4096x4096, colors don't matter.

Example gallery: [here](https://allrgb.com/esko)
