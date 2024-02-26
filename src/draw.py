#!/usr/bin/python
# -*- coding:utf-8 -*-
from os import path
import logging
from PIL import Image,ImageDraw,ImageFont

from epd import epd2in13_V2

logging.basicConfig(level=logging.DEBUG)
epd = epd2in13_V2.EPD()

images_dir = ('./images')
fonts_dir = ('./fonts')

font_profiles = {
    'default': ('default-font.ttc', 15, 13),
    'franie': ('franie-regular.otf', 12, 10)
}

font_in_use = 'default'


def get_font(font, size):
    return ImageFont.truetype(path.join(fonts_dir, font_profiles.get(font)[0]), size)


def clear_screen():    
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)


def text(text_to_draw):
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)    
 
    font = get_font(font_in_use, 15)
    draw.text((0, 0), text_to_draw, font = font, fill = 0)
    epd.display(epd.getbuffer(image))


def text_top_bottom(text_to_draw_top, text_to_draw_bottom):
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)    

    font20 = get_font(font_in_use, 20)
    font30 = get_font(font_in_use, 30)

    draw.text((0, 0), text_to_draw_top, font = font30, fill = 0)
    draw.text((0, 50), text_to_draw_bottom, font = font20, fill = 0)
    epd.display(epd.getbuffer(image.rotate(180)))


def image(image_filename):
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)

    epd.display(epd.getbuffer(image.rotate(180)))

    size = 122, 122
    image1 = Image.new('1', (epd.height, epd.width), 255)
    bmp = Image.open(image_filename)
    bmp.thumbnail(size)
    image1.paste(bmp)    
    epd.display(epd.getbuffer(image1.rotate(180)))


def image_and_text(image_filename, text_to_draw_top, text_to_draw_bottom):
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)
    
    epd.display(epd.getbuffer(image.rotate(180)))

    # draw text
    font13 = get_font(font_in_use, 13)
    font15 = get_font(font_in_use, 15)

    draw.text((125, 40), text_to_draw_top, font = font15, fill = 0)
    draw.text((125, 65), text_to_draw_bottom, font = font13, fill = 0)

    # draw image
    size = 122, 122
    bmp = Image.open(image_filename)
    bmp.thumbnail(size)
    image.paste(bmp)

    epd.display(epd.getbuffer(image.rotate(180)))
