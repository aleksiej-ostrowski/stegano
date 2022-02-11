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
from mix import mix_two
from os import path
from shutil import copyfile


def flatten(lst: list[str]) -> list[str]:
    for el in lst:
        if isinstance(el, list):
            yield from flatten(el)
        else:
            yield el


def mult(lst: list[str], n: int) -> list[str]:
    return list(flatten([[x] * n for x in lst])) # [: len(lst)]


def list_dir(fl: str) -> list[str]:
    return sorted([x for x in glob("./{fl}/*.png".format(fl=fl))])


def main():

    import argparse

    parser = argparse.ArgumentParser(
        description="This script must be used to mix PNG images from two folders."
    )

    parser.add_argument(
        "-one", "--onefolder", help="One input folder", default="frames1"
    )
    parser.add_argument(
        "-two", "--twofolder", help="Two input folder", default="frames2"
    )
    parser.add_argument("-res", "--resfolder", help="Result folder", default="frames3")
    parser.add_argument(
        "-mul", "--multiply", help="Multiply frames", type=int, default=25
    )
    parser.add_argument(
        "-s", "--seed", help="SEED for random generator", type=int, default=102
    )

    args = parser.parse_args()

    f1 = list_dir(args.onefolder)
    f2 = list_dir(args.twofolder)

    lenf1 = len(f1)
    lenf2 = len(f2)

    lenf = min(lenf1, lenf2)

    f1 = f1[:lenf]
    f2 = f2[:lenf]

    hash_s = {}
    crc = 0

    for i, (i1, i2) in enumerate(zip(mult(f1, args.multiply), mult(f2, args.multiply)), start=1):

        tail = "out-{:08d}.png".format(i)

        key_s = i1 + i2
        if key_s in hash_s.keys():
            tail_old, crc_old = hash_s[key_s]
            copyfile(
                "./{fl}/{tail}".format(fl=args.resfolder, tail=tail_old),
                "./{fl}/{tail}".format(fl=args.resfolder, tail=tail),
            )
            crc += crc_old
        else:
            crc_new = mix_two(
                i1,
                i2,
                "./{fl}/{tail}".format(fl=args.resfolder, tail=tail),
                s=args.seed,
            )
            hash_s[key_s] = (tail, crc_new)
            crc += crc_new

    print("crc for mix = ", crc)


if __name__ == "__main__":
    main()
