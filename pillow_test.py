from PIL import Image


def crop(filename, selection, width, height, format):
    im = Image.open(filename)
    icc_profile = im.info.get("icc_profile")
    selection_box = (selection['x0'], selection['y0'], selection['x1'], selection['y1'])
    im = im.crop(selection_box)
    im = im.resize((width, height), Image.ANTIALIAS)
    output_filename = "{}.pillow.{}".format(filename, format)
    if icc_profile:
    	im.info["icc_profile"] = icc_profile
    im.save(output_filename, format, quality=80, icc_profile=icc_profile)
