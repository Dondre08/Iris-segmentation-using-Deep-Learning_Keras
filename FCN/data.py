from __future__ import print_function

import os
import numpy as np

import cv2

data_path = 'data/'

image_rows = 280
image_cols = 320

def create_train_data():
    train_data_path = os.path.join(data_path, 'train')
    images = os.listdir(train_data_path)
    total = len(images) #24000 images
    imgs = np.ndarray((total, 1, image_rows, image_cols), dtype=np.uint8)
    
    train_label = np.loadtxt("data/train_label.csv", delimiter=",")

    i = 0
    print('-'*30)
    print('Creating training images...')
    print('-'*30)
    for image_name in images:
        img = cv2.imread(os.path.join(train_data_path, image_name), cv2.IMREAD_GRAYSCALE)
        img = np.array([img])
        imgs[i] = img

        if i % 100 == 0:
            print('Done: {0}/{1} images'.format(i, total))
        i += 1
    print('Loading done.')

    np.save('imgs_train.npy', imgs)
    np.save('imgs_train_label.npy', train_label)
    print('Saving to .npy files done.')


def load_train_data():  
    imgs_train = np.load('imgs_train.npy')
    imgs_train_label = np.load('imgs_train_label.npy')
    return imgs_train, imgs_train_label


def create_test_data(): 
    train_data_path = os.path.join(data_path, 'test')
    images = os.listdir(train_data_path)
    total = len(images)

    imgs = np.ndarray((total, 1, image_rows, image_cols), dtype=np.uint8)

    i = 0
    print('-'*30)
    print('Creating test images...')
    print('-'*30)
    for image_name in images:
        img = cv2.imread(os.path.join(train_data_path, image_name), cv2.IMREAD_GRAYSCALE)

        img = np.array([img])
        imgs[i] = img

        if i % 100 == 0:
            print('Done: {0}/{1} images'.format(i, total))
        i += 1
    print('Loading done.')

    np.save('imgs_test.npy', imgs)
    print('Saving to .npy files done.')


def load_test_data():
    imgs_test = np.load('imgs_test.npy')
    return imgs_test

if __name__ == '__main__':
    create_train_data()
    create_test_data()