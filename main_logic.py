import numpy as np
import glob
import cv2
import pickle
from PIL import Image


PATH = glob.glob("C:\\Users\\Varadh\\Documents\\GitHub\\PyProject_ML_Preprocessing\\Active_Workspace\\*.jpg")


def convert_filetype():
    y = glob.glob("C:\\Users\\Varadh\\Documents\\GitHub\\PyProject_ML_Preprocessing\\Active_Workspace\\*.png")

    for im_png in y:
        im = cv2.imread(im_png)
        cv2.imwrite(im_png[:-3] + 'jpg', im)


def img_resize(temp_width=100, temp_height=100):

    for my_img in PATH:
        img = cv2.imread(my_img)
        print('\nOriginal Dimensions:  ', img.shape)
        resized_img = cv2.resize(img, (temp_width, temp_height))
        print('Resized Dimensions:   ', resized_img.shape)
        cv2.imwrite(my_img, resized_img)


def img_to_grey():
    print("\n============================================================================================")
    print("GREYSCALLING IMAGES")
    print("============================================================================================")

    global PATH

    for my_img in PATH:
        img = cv2.imread(my_img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(my_img, gray)
    print("\n============================================================================================")
    print("Completed Greyscalling Images")
    print("============================================================================================\n")


def extracting_features(x='_', y=1):
    print("\n============================================================================================")
    print("EXTRACTING FEATURES")
    print("============================================================================================")
    # x = input("Enter the feature separating symbol (E.g:- '_' or '-'):  ")
    # y = int(input("Enter the offset of the separating symbol:  "))

    global PATH

    z = []
    for myfiles in PATH:
        z.append(myfiles.split('.')[0].split('\\')[-1].split(x)[y:])
    return z


def img_to_numpy_w_label(x, y):
    print("\n============================================================================================")
    print("IMAGES TO NUMPY ARRAY")
    print("============================================================================================")

    global PATH

    y = int(y)
    z = extracting_features(x, y)

    op_list = []
    final_list = []

    for myfiles in PATH:
        im = Image.open(myfiles)
        np_im = np.array(im)
        op_list.append(np_im)

    final_list = [(i, j) for i, j in zip(op_list, z)]

    f = open('numpy_images_with_labels.pckl', 'wb')
    pickle.dump(final_list, f)
    print('Values stored in: "numpy_images_with_labels.pckl"')
    f.close()

    return final_list

