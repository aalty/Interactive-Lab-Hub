import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import random


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 40
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-BoldItalic.ttf", 24)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
start = 0
end = 3

x_center_text = width // 2
y_center_text = height // 2
x0, x1 = x_center_text - 60, x_center_text + 60
y0, y1 = y_center_text - 60 , y_center_text + 60
xy = [x0, y0, x1, y1]
hh = [x_center_text - 45, y_center_text - 45, x_center_text + 45, y_center_text + 45]

def genTwoPts():
    random.seed()
    ret = []
    up, dw, lt, rt = [False] * 4
    while len(ret) < 2:
        ran = random.randint(0, 749)
        if ran < 240 and not up:
            up = True
            ret.append((ran, 0))
        elif ran < 375 and not lt:
            lt = True
            ret.append((0, ran - 240))
        elif ran < 615 and not dw:
            dw = True
            ret.append((ran - 375, 135))
        elif not rt:
            rt = True
            ret.append((240, ran - 615))
    return ret

lines = [genTwoPts() for _ in range(60)]
while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    t = time.localtime()
    h, m, s = t[3] if t[3] < 12 else t[3] - 12, t[4], t[5]

    # h_degree = 270 + 30 * h + m // 2
    # draw.arc(hh, h_degree-2, h_degree+2, fill="#FF280A")
    # draw.pieslice(hh, h_degree-2, h_degree+2, fill="#FF280A")
    # m_degree = 270 + 6 * m
    # draw.arc(xy, m_degree-2, m_degree+2, fill="#E2B659")
    # draw.pieslice(xy, m_degree-2, m_degree+2, fill="#E2B659")
    # s_degree = 270 + 6 * s
    # draw.arc(xy, s_degree-1, s_degree+1, fill="#ff0a67")
    # draw.pieslice(xy, s_degree-1, s_degree+1, fill="#ff0a67")
    if s == 0:
        lines.clear()
        lines = [genTwoPts() for _ in range(60)]
        # print(len(lines))
    else:
        for pts in lines[:s]:
            # print(pts)
            draw.line(pts, fill="#FF280A", width=2)

    
    y = top
    draw.text((50, y), time.strftime("%m/%d/%Y", t), font=font, fill="#FFFFFF")
    y += 30
    draw.text((67, y), time.strftime("%H:%M:%S", t), font=font, fill="#FFFFFF")
        
    
    # Display image.
    disp.image(image, rotation)
    # time.sleep(1)