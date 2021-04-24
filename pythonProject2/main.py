# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib
import pandas as pd
import tensorflow as tf
import numpy as np
import cv2
import MyFunctions
import ExtractRGB

def myfunct1():
    print("Always executed")

    image = cv2.imread('/Users/klrao/Downloads/input.jpeg')
    cv2.imshow('My Test', image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    print(image.shape)

    print('Height of Image:', int(image.shape[0]), 'pixels')
    print('Width of Image: ', int(image.shape[1]), 'pixels')
    print('Depth of Image: ', int(image.shape[2]), 'colors components')
    cv2.imwrite('/Users/klrao/Downloads/output.jpg', image)


def myfunct5():
    # Load our input image
    image = np.zeros((512, 512, 3), np.uint8)
    cv2.imshow("Black Rectangle (Color)", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Can we make this in black and white? grayscale
    image_bw = np.zeros((512, 512), np.uint8)
    cv2.imshow("Black Rectangle (Color)", image_bw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image = cv2.imread('/Users/klrao/Downloads/input.jpeg')
    ###cv2.imshow('Original', image)

    # Create our black canvas again
    image = np.zeros((512, 512, 3), np.uint8)

    cv2.line(image, (0, 0), (511, 511), (255, 127, 0), 5)
    cv2.imshow("Blue Line", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    B, G, R = cv2.split(image)

    print(B.shape, G.shape, R.shape)

    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Let's re-make the original image,
    merged = cv2.merge([B, G, R])
    cv2.imshow("Merged", merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Let's amplify the blue color
    merged = cv2.merge([B + 100, G, R])
    cv2.imshow("Merged with Blue Amplified", merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Let's amplify the green color
    merged = cv2.merge([B, G + 40, R])
    cv2.imshow("Merged with Green Amplified", merged)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


def myfunct6():
    image = np.zeros((512, 512), np.uint8)
    image_bw = np.zeros((512, 512, 3), np.uint8)

    cv2.imshow('black', image)
    cv2.imshow('black white', image_bw)
    cv2.waitKey()
    cv2.destroyAllWindows()


'''
Let's draw a line over our black square
cv2.line(image, starting cordinates, ending cordinates, color, thickness)
'''


def myfunct7():
    image = np.zeros((512, 512, 3), np.uint8)
    # print(image)
    cv2.line(image, (0, 0), (511, 511), (255, 127, 0), 50)
    cv2.imshow("Blue line", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():

    p1 = MyFunctions.MyClass()
    print(p1.x)
    image = cv2.imread('/Users/klrao/Downloads/input.jpeg')

    '''
    ------------------------------------
        Convert To Grey Scale Image
    ------------------------------------    
    '''
    '''
    p2 = MyFunctions.ConvertGreyScale(image, "input")
    p2.display()
    p2.conv2grey(image)
    p2.display()
    '''
    '''
    ------------------------------------
            Extract R G B
    ------------------------------------    
    '''
    p3 = ExtractRGB.ExtractRGB(image, "input")
    p3.extractRGBChannels()

    p3.individualChannels()

    p3.hsv_filtering()


if __name__ == "__main__":
    main()
