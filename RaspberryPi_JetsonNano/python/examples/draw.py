#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)
epd = epd2in13_V2.EPD()
# fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)

def clear_screen():    
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)


def text(text_to_draw):
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    # font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)    
 
    draw.text((0, 0), text_to_draw, font = font15, fill = 0)
    epd.display(epd.getbuffer(image))


def text_top_bottom(text_to_draw_top, text_to_draw_bottom):
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)

    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)    

    draw.multiline_text((0, 0), text_to_draw_top, font = font30, fill = 0)
    draw.multiline_text((0, 50), text_to_draw_bottom, font = font20, fill = 0)
    epd.display(epd.getbuffer(image.rotate(180)))


def image(image_filename):
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)

    epd.display(epd.getbuffer(image.rotate(180)))

    size = 122, 122
    image1 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    bmp = Image.open(image_filename)
    bmp.thumbnail(size)
    image1.paste(bmp)    
    epd.display(epd.getbuffer(image1.rotate(180)))


def image_and_text(image_filename, text_to_draw_top, text_to_draw_bottom):
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    
    epd.display(epd.getbuffer(image.rotate(180)))

    # draw text
    font10 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 10)
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)

    draw.multiline_text((125, 0), text_to_draw_top, font = font15, fill = 0)
    draw.multiline_text((125, 40), text_to_draw_bottom, font = font10, fill = 0)

    # draw image
    size = 122, 122
    bmp = Image.open(image_filename)
    bmp.thumbnail(size)
    image.paste(bmp)    

    epd.display(epd.getbuffer(image.rotate(180)))



# try:
#     epd = epd2in13_V2.EPD()

#     logging.info("Clearing screen")
#     clear_screen()
    
#     text_to_draw = ""
#     try:
#         text_to_draw = sys.argv[1]
#     except IndexError:
#         logging.error("no argument found")
#     logging.info("Drawing text: " + text_to_draw)

#     draw_text(text_to_draw)
#     time.sleep(5)

#     logging.info("Clearing screen")
#     clear_screen()
    
#     logging.info("Going to sleep...")
#     epd.sleep()
        
# except IOError as e:
#     logging.info(e)
    
# except KeyboardInterrupt:    
#     logging.info("ctrl + c:")
#     epd2in13_V2.epdconfig.module_exit(cleanup=True)
#     exit()
