import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import typing as t
import glob, os
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers

TRAINING_DATA_DIR = Path("/datasets/MP2_FaceMask_Dataset/train")
VALIDATION_DATA_DIR = Path("/datasets/MP2_FaceMask_Dataset/test")

img_height=224
img_width=224

class_labels = ["with_mask", "without_mask"]

def train_generator():
    train_datagen=ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    
    train_generator = train_datagen.flow_from_directory(
        TRAINING_DATA_DIR,
        target_size=(img_height, img_width),
        batch_size=64,
        class_mode='categorical',
        classes=class_labels,
        shuffle=True
    )
    return train_generator

def validation_generator():
    validation_datagen=ImageDataGenerator(rescale=1./255)
    
    validation_generator = validation_datagen.flow_from_directory(
        VALIDATION_DATA_DIR,
        target_size=(img_height, img_width),
        batch_size=64,
        class_mode='categorical',
        classes=class_labels,
        shuffle=True
    )
    return validation_generator

def model1 = Sequential(
    [set]
)