from PIL import Image


def crop(filename, selection, width, height, format):
    im = Image.open(filename)
    selection_box = (selection['x0'], selection['y0'], selection['x1'], selection['y1'])
    im = im.crop(selection_box)
    im = im.resize((width, height))
    output_filename = "{}.cropped.{}".format(filename, format)
    im.save(output_filename, format, quality=80)
