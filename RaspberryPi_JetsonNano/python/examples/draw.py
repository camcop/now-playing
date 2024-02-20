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


def clear_screen():    
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)


def draw_text(text_to_draw):
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    # font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)    
 
    draw.text((0, 0), text_to_draw, font = font15, fill = 0)
    epd.display(epd.getbuffer(image))


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
