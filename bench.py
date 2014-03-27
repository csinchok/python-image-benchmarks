#!/usr/bin/env python

import timeit
import os
import sys

BENCH_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_IMAGE_DIR = os.path.join(BENCH_DIR, "test_images")


TESTS = (

    # Liars.jpg
    'crop("%s/Liars.jpg", {"y1": 1440, "y0": 540, "x0": 0, "x1": 1600}, 600, 338, "jpeg")',
    'crop("%s/Liars.jpg", {"y1": 2006, "y0": 406, "x0": 0, "x1": 1600}, 600, 600, "jpeg")',
    'crop("%s/Liars.jpg", {"y1": 1440, "y0": 540, "x0": 0, "x1": 1600}, 600, 338, "png")',
    'crop("%s/Liars.jpg", {"y1": 2006, "y0": 406, "x0": 0, "x1": 1600}, 600, 600, "png")',

    # Lenna.png
    'crop("%s/Lenna.png", {"y1": 502, "y0": 10, "x0": 10, "x1": 502}, 600, 600, "jpeg")',
    'crop("%s/Lenna.png", {"y1": 502, "y0": 10, "x0": 10, "x1": 502}, 600, 600, "png")',

    # Mistaken.jpg
    'crop("%s/Mistaken.jpg", {"y1": 1577, "y0": 452, "x0": 0, "x1": 3375}, 1200, 675, "jpeg")',
    'crop("%s/Mistaken.jpg", {"y1": 1577, "y0": 452, "x0": 0, "x1": 3375}, 1200, 675, "png")',
    'crop("%s/Mistaken.jpg", {"y1": 2247, "y0": 0, "x0": 634, "x1": 2320}, 900, 1199, "jpeg")',
    'crop("%s/Mistaken.jpg", {"y1": 2247, "y0": 0, "x0": 634, "x1": 2320}, 900, 1199, "png")',
)


def main():

    ITERATIONS = 25
    if len(sys.argv) == 2:
        ITERATIONS = int(sys.argv[1])

    for test in TESTS:

        pillow_duration = timeit.timeit(test % TEST_IMAGE_DIR, setup="from pillow_test import crop", number=ITERATIONS)
        wand_duration = timeit.timeit(test % TEST_IMAGE_DIR, setup="from wand_test import crop", number=ITERATIONS)

        if pillow_duration < wand_duration:
            print("Pillow ({pillow_duration}) > Wand ({wand_duration})".format(
                pillow_duration=pillow_duration,
                wand_duration=wand_duration
            ))
        else:
            print("Wand ({wand_duration}) > Pillow ({pillow_duration})".format(
                pillow_duration=pillow_duration,
                wand_duration=wand_duration
            ))


if __name__ == "__main__":
    main()
