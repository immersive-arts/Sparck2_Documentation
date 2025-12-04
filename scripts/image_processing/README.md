# Basic usage - auto-detects background for each image
python make_background_transparent.py ./your_images_folder

# Custom output directory
python make_background_transparent.py ./your_images_folder -o ./processed

# Specify a specific color if you want (RGB format)
python make_background_transparent.py ./your_images_folder -c 128,128,128

# Adjust tolerance (higher = more aggressive color matching)
python make_background_transparent.py ./your_images_folder -t 50