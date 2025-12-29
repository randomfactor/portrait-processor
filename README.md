# Portrait Processor

## Purpose
This project contains a Python script designed to automate the batch processing of portrait photos, specifically for an a cappella group's website. It takes a collection of raw headshots and standardizes them by:
1.  Converting them to RGB format.
2.  Center-cropping them to a 3:4 aspect ratio.
3.  Resizing them to exactly 600x800 pixels.
4.  Saving them as optimized JPEGs (80% quality).

## Installation

### Prerequisites
- Python 3.10 or higher
- `uv` package manager (recommended) or `pip`

### Dependencies
Install the required **Pillow** library:

Using `uv`:
```bash
uv pip install Pillow
```

Or using standard `pip`:
```bash
pip install Pillow
```

## Usage

Run the script from the command line, providing the path to the directory containing your source images:

```bash
python process_photos.py <path_to_source_images>
```

**Example:**
```bash
python process_photos.py ./raw_photos
```

The script will create a `final` subdirectory inside your source directory and save the processed images there.
