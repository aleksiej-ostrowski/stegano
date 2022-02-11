# ------------------------------- #
#                                 #
#  version 0.0.1                  #
#                                 #
#  Aleksiej Ostrowski, 2022       #
#                                 #
#  https://aleksiej.com           #
#                                 #
# ------------------------------- #

from glob import glob
from mix import extract_two, size_of_image
from os import path


def list_dir(fl: str) -> list[str]:
    return sorted([x for x in glob("./{fl}/*.png".format(fl=fl))])


def main():

    import argparse

    parser = argparse.ArgumentParser(
        description="This script must be used to extract internal images from PNG images in a folder."
    )

    parser.add_argument("-inp", "--inpfolder", help="Input folder", default="frames4")
    parser.add_argument("-out", "--outfolder", help="Output folder", default="frames5")
    parser.add_argument("-two", "--twofolder", help="Two folder", default="frames2")
    parser.add_argument(
        "-exm", "--example", help="Example from two folder", default="out-00000001"
    )
    parser.add_argument(
        "-s", "--seed", help="SEED for random generator", type=int, default=102
    )

    args = parser.parse_args()

    width_two, height_two = size_of_image(
        "./{fl}/{e}.png".format(fl=args.twofolder, e=args.example)
    )

    crc = 0
    for i in list_dir(args.inpfolder):

        _, tail = path.split(i)
        crc += extract_two(
            i,
            width_two,
            height_two,
            "./{fl}/{tail}".format(fl=args.outfolder, tail=tail),
            s=args.seed,
        )

    print("crc for extract =", crc)


if __name__ == "__main__":
    main()
