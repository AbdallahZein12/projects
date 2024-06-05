from PIL import Image
import os

def pillow(path):
    output_txt = os.path.join('pic2ascii','filehandling', 'output.txt')
    with open(output_txt,'w') as output:
        with Image.open(path) as im:
            im = im.convert('L')
            im = im.resize((60,30))
            chars = '.:-=+*#%@'
            for y in range(im.size[1]):
                for x in range(im.size[0]):
                    gray = im.getpixel((x,y))
                    char = chars[gray * len(chars) // 355]
                    output.write(char)
                output.write('\n')
    with open(output_txt,'r') as output:
        final_output = output.read()
    os.remove(path)
    os.remove(output_txt)
    return final_output
