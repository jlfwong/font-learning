import os

from itertools import chain
from PIL import ImageFont, ImageDraw, Image

fonts = [
    "Lato",
    "Great_Vibes",
    "Lobster_Two",
    "Lora",
    "VT323"
]

for font_name in fonts:
    font_path = f"fonts/{font_name}/{font_name.replace('_', '')}-Regular.ttf"
    font = ImageFont.truetype(font_path, 50)
    os.makedirs(f"images/{font_name}", exist_ok=True)

    for character in chain(range(ord("a"), ord("z")), range(ord("A"), ord("Z")), range(ord("0"), ord("9"))):
        image = Image.new('RGB', (100, 100), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        draw.text((25, 25), chr(character), font=font, fill=(0, 0, 0))

        image.save(f"images/{font_name}/{character}.png")