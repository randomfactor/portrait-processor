# Project Overview: Batch Image Processor for A Cappella Group

**Role:** Act as an experienced Python developer specializing in image processing automation on Linux.

## Objective
Write a robust Python script to automate the processing of 24 portrait photos for a website. The photos are headshots of a cappella group members. The script must handle common image variations and produce uniform output.

## Environment
This project is running on **Pop!_OS Linux** and uses `uv` for Python package management.

## Input/Output Specifications

### Source Directory
The script should read images from a directory named `source_images` located in the same directory as the script. (Assume this directory contains mixed file types like PNG, JPEG, Maybe TIFF).

### Destination Directory
Processed images must be saved into a directory named `final`. The script must create this directory if it does not already exist.

## Processing Steps (Per Image)
Iterate through every file in the `source_images` directory. For each valid image file, perform the following sequence exactly:

1. **Format Conversion:** Ensure internally the image is treated as **RGB** (dropping alpha channels if present) to prepare for JPEG saving.

2. **Crop & Resize (Targeting 600x800):**
   - The final goal is an image exactly **600 pixels wide by 800 pixels high** (a 3:4 portrait aspect ratio).
   - *Crucial:* Do not stretch or distort the image.
   - Implement a "center crop to aspect ratio" approach: Calculate the largest possible 3:4 area centered in the original image, crop to that area, and then resize down to 600x800.

3. **Quality Setting:** Set the JPEG compression quality to **80%**.

4. **Final Output:** Save the processed image to the `final` folder. Ensure the output filename uses the original base name but with a `.jpg` extension (e.g., `member01.png` becomes `final/member01.jpg`).

## Technical Requirements & Constraints

- **Library:** Use the standard **Pillow (PIL)** library for all image manipulations.
- **Robustness:** The script must handle errors gracefully. If it encounters a non-image file in the source folder, or a corrupted image, it should print a warning message to the console and skip to the next file, rather than crashing completely.
- **Logging:** Provide clear console output indicating progress (e.g., "Processing [1/24]: image_name.jpg... Success").

## Deliverables

1. The complete Python script code (e.g., `process_photos.py`).
2. The exact `uv pip install ...` command required to install dependencies for this script.
