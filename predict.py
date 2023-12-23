import shutil
import cv2
import sys
import os
import numpy as np
import base64
from ultralytics import YOLO

percentage_yellow_lab = 0.0

def calculate_yellow_percentage_lab(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to LAB
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Define a mask for yellow color in LAB color space
    lower_yellow_lab = np.array([0, 128, 128], dtype=np.uint8)
    upper_yellow_lab = np.array([255, 255, 255], dtype=np.uint8)
    yellow_mask_lab = cv2.inRange(image_lab, lower_yellow_lab, upper_yellow_lab)

    # Calculate the percentage of yellow pixels
    total_pixels = image_lab.size // 3  # Total number of pixels (assuming 3 channels)
    yellow_pixels = np.count_nonzero(yellow_mask_lab)
    yellow_percentage = (yellow_pixels / total_pixels) * 100

    return yellow_percentage


image_data = sys.stdin.buffer.read()

# Load the YOLO model, image, and directory for save predict result
mod = 'detect.pt' # Mango detection model
img = '_temp.png'
dir = 'runs'

# Load a pretrained YOLOv8 model
model = YOLO(mod)

# Run inference on an image
results = model(img, save=True)  # results list

# View results
for r in results:
    r.save_crop(dir, file_name='_temp')

# Write predict image to public file
image = cv2.imread('runs/detect/predict/_temp.png')
cv2.imwrite('public/_temp.png', image)

# Checking if any mango have detected
if not os.path.isdir('runs/body'):
    predict = "Can not reconize mango in image, please try another image!"
else:
    pr_model = YOLO('classify.pt') # Load pretrained mango ripeness classification model
    image_path = "runs/body/_temp.jpg"

    # Get the classìication result
    result = pr_model(image_path)
    names = result[0].names
    in_top1 = result[0].probs.top1

    # Get the percentage of yellow component in the image
    percentage_yellow_lab = calculate_yellow_percentage_lab(image_path)

    # Calculate the result and give predict on ripeness
    if in_top1 == 0:
        predict = "Unripe Mango"
    elif percentage_yellow_lab > 55: # Adjust the color percentage to determine fully ripe or partially ripe, current best rate is 55%
        predict = "Ripe Mango"
    else:
        predict = "Partially Ripe Mango"
    
# Clear the directory
shutil.rmtree('runs')

# Print the result
print("Result:", predict)
if percentage_yellow_lab > 0:
    print(f"The percentage of yellow color in the image (LAB color space) is: {percentage_yellow_lab:.2f}%")