import cv2
import numpy as np
import os

def penTool(action, x, y, flags, userdata):
    global mask, points, color
    if action == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 4:
            contours = np.array(points)
            cv2.fillPoly(mask, pts = [contours], color = color)
            points = []
        cv2.imshow('Label Tool', mask)

    elif action == cv2.EVENT_LBUTTONUP:
        cv2.imshow("Label Tool", mask)

def brushTool(action, x, y, flags, userdata):
    global mask, color, r
    if action == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(mask, (x, y), r, color, -1)
        cv2.imshow('Label Tool', mask)
    elif action == cv2.EVENT_LBUTTONUP:
        cv2.imshow('Label Tool', mask)

def readImage(i):
    global input_path, path_mask, mask, id, input
    input = cv2.imread(input_path[i])
    id = input_path[i].split('/')[-1].split('.')[0]
    path_mask = 'Images/Mask/' + id + '_skin_' + id + '.png'
    mask = cv2.imread(path_mask)

input_f = 'Images/Input/'
input_path = [input_f + name for name in os.listdir(input_f)]

if __name__ == '__main__':
    points = []
    color = (0, 0, 0)
    i = 0
    r = 15
    k = 0
    mode = brushTool
    readImage(i)
    cv2.namedWindow("Label Tool")
    cv2.setMouseCallback("Label Tool", mode)
    
    print('--------------------TUTORIAL-------------------------')
    print(f"Radius: {r}, press [-] to down, [+] to up")
    print('Mode: BrushTool, press [m] to change to PenTool')
    print('Color: White, press [b] to change to Black')
    print('Reset: press [r] to reset')
    print('Save: press [s] to save')
    print('Next: press [d] to next image')
    print('Previous: press [a] to previous image')
    print('Quit: press [q] to quit')
    print('-----------------------------------------------------')
    
    while k != ord('q'):
        img = cv2.addWeighted(input, 0.85, mask, 0.4, 0)
        cv2.imshow("Label Tool", img)
        k = cv2.waitKey(20) & 0xFF

        if k == ord('m'):
            if mode == brushTool:
                mode = penTool
                cv2.setMouseCallback("Label Tool", mode)
                print('Mode: PenTool')
            else:
                mode = brushTool
                cv2.setMouseCallback("Label Tool", mode)
                print('Mode: BrushTool')

        if k == ord('c'):
            if color == (255, 255, 255):
                color = (0, 0, 0)
                print('Color: Black')
            else:
                color = (255, 255, 255)
                print('Color: White')

        if k == ord('r'):
            readImage(i)
            print('Reset mask')

        if k == ord('d'):
            i = 0 if i == len(input_path) - 1 else i + 1
            readImage(i)
            print(f'Next image --> {i}')
        if k == ord('a'):
            i = len(input_path) - 1 if i == -1 else i - 1
            readImage(i)
            print(f'Previous image --> {i}')
        if k == ord('='):
            r += 2
            print(f"Radius: {r}")
        if k == ord('-'):
            r -= 2
            print(f"Radius: {r}")
        if k == ord('s'):
            cv2.imwrite('Images/Mask_new/' + path_mask.split('/')[-1], mask)
            print('Saved!')
    print(input_path[i], i)
    cv2.destroyAllWindows()