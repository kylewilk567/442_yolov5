import cv2
import numpy as np
import os
import subprocess
import shutil
# import cv2.ximgproc

INPUT_DIR = './dataset/UOT_unprocessed_dataset'
OUTPUT_DIR = './dataset/UOT_processed_dataset'

# TODO: CHANGE THIS TO YOUR NUMBER
number = 0

def process():
    # Create output directory structure
    os.makedirs(os.path.join(OUTPUT_DIR, 'images', 'train'), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'images', 'val'), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'images', 'test'), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'labels', 'train'), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'labels', 'val'), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'labels', 'test'), exist_ok=True)

    image_files =  [os.path.join(INPUT_DIR, 'images/test', f) for f in os.listdir(os.path.join(INPUT_DIR, 'images/test'))] + [os.path.join(INPUT_DIR, 'images/train', f) for f in os.listdir(os.path.join(INPUT_DIR, 'images/train'))] + [os.path.join(INPUT_DIR, 'images/val', f) for f in os.listdir(os.path.join(INPUT_DIR, 'images/val'))]
    for image_file in image_files:
        file_name = os.path.basename(image_file)
        file_number = int(file_name[:-4])
        if file_number % 5 != number:
            continue
        sub_dir = image_file.split('/')[4]
        file_name = os.path.basename(image_file)
        subprocess.run(["python3", "sea_thru_new.py", "--image",
                        image_file,
                        "--output", os.path.join(OUTPUT_DIR, 'images', sub_dir, file_name)])
    label_files =  [os.path.join(INPUT_DIR, 'labels/test', f) for f in os.listdir(os.path.join(INPUT_DIR, 'labels/test'))] + [os.path.join(INPUT_DIR, 'labels/train', f) for f in os.listdir(os.path.join(INPUT_DIR, 'labels/train'))] + [os.path.join(INPUT_DIR, 'labels/val', f) for f in os.listdir(os.path.join(INPUT_DIR, 'labels/val'))]
    for label_file in label_files:
        file_number = int(file_name[:-4])
        if file_number % 5 != number:
            continue
        sub_dir = label_file.split('/')[4]
        file_name = os.path.basename(label_file)
        shutil.copyfile(label_file, os.path.join(OUTPUT_DIR, 'labels', sub_dir, file_name))

          



if __name__ == '__main__':
    process()

