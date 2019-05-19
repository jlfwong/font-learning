import os
import random
import shutil

from itertools import chain
from PIL import ImageFont, ImageDraw, Image

fonts = [name for name in os.listdir("fonts") if os.path.isdir(f'fonts/{name}')]

charset = list(chain(range(ord("a"), ord("z")), range(ord("A"), ord("Z")), range(ord("0"), ord("9"))))

def get_random_char():
    return chr(random.choice(charset))

def get_random_word():
    length = random.randint(1, 7)
    return "".join([get_random_char() for i in range(length)])

def get_random_string():
    word_count = random.randint(1, 6)
    return " ".join([get_random_word() for i in range(word_count)])


if __name__ == '__main__':
    for font_name in fonts:
        font_path = f"fonts/{font_name}/{font_name.replace('_', '')}-Regular.ttf"
        print(f'Loading {font_path}')
        font = ImageFont.truetype(font_path, 25)
        dir_path = f"images/{font_name}"
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        os.makedirs(dir_path, exist_ok=True)

        images_per_font = 300

        for idx in range(images_per_font):
            image = Image.new('RGB', (250, 100), (255, 255, 255))
            draw = ImageDraw.Draw(image)

            name = get_random_string()

            x = random.randint(0, 50)
            y = random.randint(0, 80)

            draw.text((x, y), name, font=font, fill=(0, 0, 0))

            image.save(f"{dir_path}/{name.replace(' ', '_')}.png")