# because of https://stackoverflow.com/questions/27522626/hash-function-in-python-3-3-returns-different-results-between-sessions
# you need to run 
# PYTHONHASHSEED=0 python identicon.py
# to disable random hashing
from PIL import Image, ImageDraw
import webcolors

# create python function to read user input

name = input("What is your name?\n")
print("My name is " + name)


# use hashing function to turn the input a unique

hash_name = hash(name)

#convert hash to hexadecimal
hex_name = hex(hash_name)

#Pull last six characters of hexadecimal
hex_color = hex_name[-6:]
rbg_color = webcolors.hex_to_rgb(u'#{color}'.format(color=hex_color))
rbg_color_tuple = (rbg_color.red, rbg_color.green, rbg_color.blue)

# convert name to binary

binary_name = bin(hash_name)

#Get last 16 digits of binnary number of name
short_binary=binary_name[-16:]

#arr of indices to use when filling in 5x5 grid
symmetry = [0,1,2,1,0,3,4,5,4,3,6,7,8,7,6,9,10,11,10,9,12,13,14,13,12]

#Draw 5 by 5 image
file_name = "{name}-identicon.png".format(name=name)
image =  Image.new('RGB', (50*5+20*2, 50*5+20*2), (255, 255, 255))
draw = ImageDraw.Draw(image)
use_idx = 0
for x in [0,50,100,150,200]:
    for y in [0,50,100,150,200]:
        #grab index from symmetry we need
        current_idx = symmetry[use_idx]
        #look up value of that image in short_binary
        digit = short_binary[current_idx]
        #draw rectangle if image is 1
        if int(digit) == 1:
            draw.rectangle([x, y, x + 50, y + 50], fill=rbg_color_tuple, outline=None)
        #increment use_idx each time we go through loop
        use_idx+=1

image.show()
image.save(file_name)
    
