import sys,core.htmltoimg as htmltoimg

input_dir = 'C:\GUIComponents\samples\GUIComponents'
img_format = 'jpg'

args_length = len(sys.argv)
if args_length > 1:

    input_dir = sys.argv[1]

    if args_length > 2:
        img_format = sys.argv[2]

htmltoimg.html_to_img(input_dir, img_format)