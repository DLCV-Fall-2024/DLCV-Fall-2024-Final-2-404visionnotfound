import cv2
import numpy as np
import random
import os
from PIL import Image
from tqdm import tqdm

alpha_range_s = (0.25, 1.5)
alpha_range_v = (0.25, 1.5)
data_aug_factor = 30

def random_rotate(image):
    """
    Applies a random rotation to the image.

    :param image: Input image as a NumPy array.
    :return: Rotated image.
    """
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    
    # Generate a random angle for rotation
    angle = random.uniform(-180, 180)  # Random angle between -30 and 30 degrees
    
    # Get rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Perform the rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return rotated_image

def random_perspective_transform(image):
    """
    Applies a random perspective transformation to the image.

    :param image: Input image as a NumPy array.
    :return: Warped image.
    """
    height, width = image.shape[:2]
    
    # Define random perturbations for the four corners
    margin = 50  # Maximum pixel displacement
    src_pts = np.float32([
        [random.randint(0, margin), random.randint(0, margin)],  # Top-left
        [width - random.randint(0, margin), random.randint(0, margin)],  # Top-right
        [width - random.randint(0, margin), height - random.randint(0, margin)],  # Bottom-right
        [random.randint(0, margin), height - random.randint(0, margin)],  # Bottom-left
    ])
    dst_pts = np.float32([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1],
    ])
    
    # Get the perspective transform matrix
    matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
    
    # Perform the perspective warp
    warped_image = cv2.warpPerspective(image, matrix, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return warped_image

def random_crop(image, max_size_ratio=0.6, min_size_ratio=0.4):
    """
    Randomly crops an image with a random size and position.

    :param image: Input image as a NumPy array.
    :return: Cropped image.
    """
    height, width = image.shape[:2]

    min_crop_height = int(height * min_size_ratio)
    min_crop_width = int(width * min_size_ratio)

    max_crop_height = int(height * max_size_ratio)
    max_crop_width = int(width * max_size_ratio)
    
    # Random crop size
    crop_height = random.randint(min_crop_height, max_crop_height)
    crop_width = random.randint(min_crop_width, max_crop_width)
    
    # Random top-left corner
    x_start = random.randint(0, width - crop_width)
    y_start = random.randint(0, height - crop_height)
    
    # Crop the image
    cropped_image = image[y_start:y_start + crop_height, x_start:x_start + crop_width]
    return cropped_image

def modify_hsv(image_path, output_path):
    # Load the image in BGR format
    image_bgr = cv2.imread(image_path)
    
    if image_bgr is None:
        raise ValueError(f"Image at path {image_path} could not be loaded. Please check the path.")

    # Perform random rotation
    rotated_image = random_rotate(image_bgr)
    
    # Apply random perspective transformation
    warped_image = random_perspective_transform(rotated_image)
    
    # Perform random cropping
    cropped_image = random_crop(warped_image)
    
    # Convert the cropped image to HSV
    image_hsv = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    
    # Split the HSV channels
    h, s, v = cv2.split(image_hsv)
    
    # Modify Hue: Add a random number (0–179), wrap around at 179
    h = (h.astype(np.int32) + random.randint(0, 179)) % 180  # Ensure modulo operation works
    h = h.astype(np.uint8)  # Convert back to uint8

    # Generate random alpha factors for S and V
    alpha_s = random.uniform(*alpha_range_s)
    alpha_v = random.uniform(*alpha_range_v)
    
    # Adjust Saturation and Value with random alpha factors
    s = np.clip(s.astype(np.float32) * alpha_s, 0, 255).astype(np.uint8)
    v = np.clip(v.astype(np.float32) * alpha_v, 0, 255).astype(np.uint8)
    
    # Merge the modified channels back
    modified_hsv = cv2.merge([h, s, v])
    
    # Convert the modified HSV image back to BGR
    modified_bgr = cv2.cvtColor(modified_hsv, cv2.COLOR_HSV2BGR)
    
    # Save the output image
    cv2.imwrite(output_path, modified_bgr)
    #print(f"Modified, rotated, warped, and cropped image saved to {output_path}")


in_path = os.path.join("Data/concept_image/watercolor")

for base_img in [path for path in os.listdir(in_path) if path[-3:] == "jpg" or path[-3:] == "png"]:
    for gen_img in tqdm(range(data_aug_factor)):
        # Example usage
        new_img = f"{base_img[:-4]}_{gen_img:03d}.{base_img[-3:]}"
        input_image_path = os.path.join("Data/concept_image/watercolor", base_img)  # Replace with your input image path
        output_image_path = os.path.join("./newData/concept/watercolor/image", new_img)  # Replace with your output image path
        modify_hsv(input_image_path, output_image_path)

        # Create caption file
        caption_file_path = os.path.join("./newData/concept/watercolor/caption",  f"{base_img[:-4]}_{gen_img:03d}.txt")
        with open(caption_file_path, 'w', encoding='utf-8') as cap_file:
            cap_file.write(f"<watercolor>\n")


        # Create a dummy white mask with the same size as the image
        with Image.open(output_image_path) as img:
            width, height = img.size
            mask = Image.new("RGB", (width, height), (255, 255, 255))  # White mask
            mask_file_path = os.path.join("./newData/concept/watercolor/mask", f"{base_img[:-4]}_{gen_img:03d}.png")
            mask.save(mask_file_path)
