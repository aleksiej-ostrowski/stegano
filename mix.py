# ------------------------------ #
#                                #
#  version 0.0.1                 #
#                                #
#  Aleksiej Ostrowski, 2022      #
#                                #
#  https://aleksiej.com          #
#                                #
# ------------------------------ #

from PIL import Image
from random import seed, randint


def mix_two(one_image, two_image, save_image, s=101):

    seed(s)

    crc = 0.0

    hash_xy = {}

    with Image.open(one_image).convert("RGBA") as one, Image.open(two_image).convert(
        "RGBA"
    ) as two:

        width_one, height_one = one.size
        width_two, height_two = two.size

        for x_two in range(width_two):
            for y_two in range(height_two):

                r, g, b, a = two.getpixel((x_two, y_two))

                while True:

                    x_one = randint(0, width_one - 1)
                    y_one = randint(0, height_one - 1)

                    key_xy = y_one * width_one + x_one

                    if key_xy in hash_xy.keys():
                        continue

                    crc += (0.2627 * r + 0.678 * g + 0.0593 * b) * key_xy

                    hash_xy[key_xy] = True

                    one.putpixel((x_one, y_one), (r, g, b, a))

                    break

        one.save(save_image, "PNG")

        return round(crc)


def extract_two(one_image, width_two, height_two, save_image, s=101):

    seed(s)

    crc = 0.0

    hash_xy = {}

    with Image.open(one_image).convert("RGBA") as one, Image.new(
        "RGBA", (width_two, height_two)
    ) as two:

        width_one, height_one = one.size

        for x_two in range(width_two):
            for y_two in range(height_two):

                while True:

                    x_one = randint(0, width_one - 1)
                    y_one = randint(0, height_one - 1)

                    key_xy = y_one * width_one + x_one

                    if key_xy in hash_xy.keys():
                        continue

                    hash_xy[key_xy] = True

                    r, g, b, a = one.getpixel((x_one, y_one))

                    crc += (0.2627 * r + 0.678 * g + 0.0593 * b) * key_xy

                    two.putpixel((x_two, y_two), (r, g, b, a))

                    break

        two.save(save_image, "PNG")

        return round(crc)


def size_of_image(image):
    with Image.open(image) as im:
        return im.size


if __name__ == "__main__":

    one = "one.png"
    two = "two.png"

    w1, h1 = size_of_image(one)
    w2, h2 = size_of_image(two)

    if w1 * h1 <= w2 * h2:
        assert "Image #1 must be larger than Image #2"

    if mix_two(one, two, "mixed.png") != extract_two(
        "mixed.png", w2, h2, "demixed.png"
    ):
        assert "Extract does not work."

    print("Autotest is ok.")
