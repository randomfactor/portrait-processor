import os
import sys
from PIL import Image, UnidentifiedImageError

def process_images():
    if len(sys.argv) < 2:
        print("Usage: python process_photos.py <source_directory>")
        return

    source_dir = sys.argv[1]

    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' not found.")
        return

    dest_dir = os.path.join(source_dir, 'final')
    target_size = (600, 800)
    target_ratio = target_size[0] / target_size[1]

    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    files = os.listdir(source_dir)
    total_files = len(files)
    
    # Filter for likely image files to get a more accurate count for the progress log if desired,
    # but the prompt implies iterating through every file and handling errors.
    # We'll stick to iterating all and counting as we go.
    
    print(f"Found {total_files} files in '{source_dir}'. Starting processing...")

    for index, filename in enumerate(files, start=1):
        file_path = os.path.join(source_dir, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        print(f"Processing [{index}/{total_files}]: {filename}...", end=' ', flush=True)

        try:
            with Image.open(file_path) as img:
                # 1. Format Conversion: Ensure RGB
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                # 2. Crop & Resize
                current_width, current_height = img.size
                current_ratio = current_width / current_height

                if current_ratio > target_ratio:
                    # Image is too wide - crop width
                    new_width = int(current_height * target_ratio)
                    new_height = current_height
                    left = (current_width - new_width) // 2
                    top = 0
                    right = left + new_width
                    bottom = current_height
                else:
                    # Image is too tall - crop height
                    new_width = current_width
                    new_height = int(current_width / target_ratio)
                    left = 0
                    top = (current_height - new_height) // 2
                    right = current_width
                    bottom = top + new_height

                img_cropped = img.crop((left, top, right, bottom))
                img_resized = img_cropped.resize(target_size, Image.Resampling.LANCZOS)

                # 4. Final Output
                base_name = os.path.splitext(filename)[0]
                output_filename = f"{base_name}.jpg"
                output_path = os.path.join(dest_dir, output_filename)

                # 3. Quality Setting: 80%
                img_resized.save(output_path, 'JPEG', quality=80)
                print("Success")

        except UnidentifiedImageError:
            print("Skipped (Not a valid image)")
        except OSError as e:
            print(f"Skipped (Corrupted or error: {e})")
        except Exception as e:
            print(f"Failed ({e})")

if __name__ == "__main__":
    process_images()
