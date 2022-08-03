import cv2
import numpy as np
import os
import shutil
import argparse



def get_arguments():
    arg = argparse.ArgumentParser()
    arg.add_argument('-in', '--input_f', help='link to image', default='image/')
    arg.add_argument('-out', '--output_f', help='link to save label image', default='output/')
    arg.add_argument('-i', '--index', help='index image in folder input_f', default=0)
    return arg.parse_args()

args = get_arguments()

# input_f = 'image/'
input_path = [args.input_f + name for name in os.listdir(args.input_f) if name.endswith(('jpg', 'png', 'jpeg'))]

i = args.index
k = 0
l_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p',
          'r', 's', 't', 'u', 'v', 'x', 'y', 'z', '0', '1', '2', '3',
          '4', '5', '6', '7', '8', '9', "/"]

def create_folder_output(output_f='output/'):
    if not os.path.exists(output_f):
        os.makedirs(output_f, exist_ok=True)

    for char in [l_upper.upper() for l_upper in l_char]:
        if char == '/':
            char = 'Background'
        os.makedirs(f'{output_f}/{char}', exist_ok=True)

create_folder_output(args.output_f)

img = cv2.imread(input_path[i])

print('--------------------TUTORIAL-------------------------')
print('HOW TO USGE: Press character or digital corresponding with image to annotation data')
print('Next: press [.] to next image')
print('Previous: press [,] to previous image')
print('Quit: press [Q] to quit')
print(f'Start annotation at index image [{i}]')
print(f'Labels have save in {args.output_f} folder')
print('-----------------------------------------------------')

while k != ord('Q'):
    cv2.imshow("Classify character", img)
    k = cv2.waitKey(20) & 0xFF

    # Next or Previos
    if k == ord('.'):
        i = 0 if i == len(input_path) - 1 else i + 1
        img = cv2.imread(input_path[i])
    if k == ord(','):
        i = len(input_path) - 1 if i == -1 else i - 1
        img = cv2.imread(input_path[i])

    # Digital & character
    for c in l_char:
        if k == ord(c):
            if c == '/':
                c = 'Background'
            shutil.copy(input_path[i], os.path.join(args.output_f, c))
            i = 0 if i == len(input_path) - 1 else i + 1
            img = cv2.imread(input_path[i])
            print(f'Index image: [{i}] - Copy {input_path[i]} to folder label {c.capitalize()}')
print(f'Break at index image [{i}]')
