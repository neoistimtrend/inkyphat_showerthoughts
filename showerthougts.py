#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw

from inky import InkyPHAT

import requests

# https://www.reddit.com/r/Showerthoughts/top/.json?t=hour/
url = 'https://www.reddit.com/r/Showerthoughts/top/.json'
params = dict(t='hour',limit='1')
resp = requests.get(url=url, params=params, headers={'User agent' : 'inky 0.1'})
json=resp.json()
data = json['data']['children'][0]['data']['title']

import textwrap
wrapper = textwrap.TextWrapper(width=35)
showerthought = wrapper.wrap(text=data)
showerthought = '\n'.join(showerthought)


def main():
# Set up the display

inky_display = InkyPHAT('red')
inky_display.set_border(inky_display.BLACK)
# inky_display.set_rotation(180)

# get an image
img = Image.open('Pillow/Tests/images/hopper.png').convert('RGBA')

draw = ImageDraw.Draw(img)

draw.text((0, 0),showerthought,(255,255,255),font=font)



inkyphat.set_image(img)
inkyphat.show()
