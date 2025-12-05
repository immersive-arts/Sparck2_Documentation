# Basic usage - auto-detects background for each image
python background_transparent.py ./your_images_folder

# Custom output directory
python background_transparent.py ./your_images_folder -o ./processed

# Specify a specific color if you want (RGB format)
python background_transparent.py ./your_images_folder -c 128,128,128

# Adjust tolerance (higher = more aggressive color matching)
python background_transparent.py ./your_images_folder -t 5