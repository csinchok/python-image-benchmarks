from wand.image import Image


def crop(filename, selection, width, height, format):
    with open(filename, 'rb') as source_file:
        with Image(file=source_file) as img:
            img.crop(selection['x0'], selection['y0'], selection['x1'], selection['y1'])
            img.transform(resize="{width}x{height}".format(width=width, height=height))
            if format.lower() == 'jpeg':
                img.format = 'jpeg'
                img.compression_quality = 80
            if format.lower() == 'png':
                img.format = 'png'
            output_filename = "{}.cropped.{}".format(filename, format)
            img.save(filename=output_filename)
