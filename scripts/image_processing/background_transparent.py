#!/usr/bin/env python3
"""
Batch process PNG images to make background pixels transparent.
Automatically detects background color from image edges.
Only makes pixels transparent if they're connected to the edge.
"""

import os
import sys
from PIL import Image
import numpy as np
from pathlib import Path
from collections import Counter
from scipy import ndimage


def detect_background_color(img_array, sample_size=5):
    """
    Detect the background color by sampling pixels from the edges of the image.
    
    Args:
        img_array: Numpy array of the image (RGBA)
        sample_size: Number of pixels to sample from each edge
        
    Returns:
        RGB tuple of the most common edge color
    """
    height, width = img_array.shape[:2]
    
    # Sample pixels from all four edges
    edge_pixels = []
    
    # Top edge
    edge_pixels.extend(img_array[0:sample_size, :, :3].reshape(-1, 3))
    
    # Bottom edge
    edge_pixels.extend(img_array[height-sample_size:height, :, :3].reshape(-1, 3))
    
    # Left edge (excluding corners already sampled)
    edge_pixels.extend(img_array[sample_size:height-sample_size, 0:sample_size, :3].reshape(-1, 3))
    
    # Right edge (excluding corners already sampled)
    edge_pixels.extend(img_array[sample_size:height-sample_size, width-sample_size:width, :3].reshape(-1, 3))
    
    # Convert to tuples for counting
    edge_colors = [tuple(pixel) for pixel in edge_pixels]
    
    # Find the most common color
    color_counts = Counter(edge_colors)
    most_common_color = color_counts.most_common(1)[0][0]
    
    # Convert to regular Python ints (in case they're numpy types)
    most_common_color = tuple(int(c) for c in most_common_color)
    
    print(f"  Detected background color: RGB{most_common_color}")
    
    return most_common_color


def find_edge_connected_pixels(mask):
    """
    Find pixels that are connected to the edges of the image.
    
    Args:
        mask: Boolean array where True indicates pixels matching the background color
        
    Returns:
        Boolean array where True indicates pixels connected to edges
    """
    height, width = mask.shape
    
    # Check if there are any matching pixels on the edges
    edge_pixels_count = (
        np.sum(mask[0, :]) +  # top
        np.sum(mask[-1, :]) +  # bottom
        np.sum(mask[:, 0]) +  # left
        np.sum(mask[:, -1])  # right
    )
    
    print(f"  Edge pixels matching color: {edge_pixels_count}")
    
    if edge_pixels_count == 0:
        print("  WARNING: No matching pixels found on edges!")
        return np.zeros_like(mask, dtype=bool)
    
    # Label connected components
    labeled_array, num_features = ndimage.label(mask)
    
    # Find which labels touch the edges
    edge_labels = set()
    edge_labels.update(labeled_array[0, :])  # top
    edge_labels.update(labeled_array[-1, :])  # bottom
    edge_labels.update(labeled_array[:, 0])  # left
    edge_labels.update(labeled_array[:, -1])  # right
    edge_labels.discard(0)  # Remove background label
    
    print(f"  Found {num_features} connected regions, {len(edge_labels)} touch edges")
    
    # Create mask of all pixels in edge-touching components
    edge_connected_mask = np.isin(labeled_array, list(edge_labels))
    
    return edge_connected_mask


def make_background_transparent(input_path, output_path, target_color=None, tolerance=20):
    """
    Make pixels of a specific color transparent in a PNG image.
    Only affects pixels connected to the image edges.
    
    Args:
        input_path: Path to input PNG file
        output_path: Path to output PNG file
        target_color: RGB tuple of the color to make transparent (None = auto-detect)
        tolerance: Color tolerance for matching (0-255, default: 30)
    """
    # Open image and convert to RGBA if needed
    img = Image.open(input_path)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Convert to numpy array for easier manipulation
    data = np.array(img)
    
    # Auto-detect background color if not provided
    if target_color is None:
        target_color = detect_background_color(data)
    
    # Get RGB channels
    r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]
    
    # Create mask for pixels matching the target color within tolerance
    color_mask = (
        (np.abs(r.astype(int) - target_color[0]) <= tolerance) &
        (np.abs(g.astype(int) - target_color[1]) <= tolerance) &
        (np.abs(b.astype(int) - target_color[2]) <= tolerance)
    )
    
    # Find only the pixels connected to edges
    edge_connected_mask = find_edge_connected_pixels(color_mask)
    
    # Count statistics
    total_matching = np.sum(color_mask)
    edge_connected = np.sum(edge_connected_mask)
    total_pixels = color_mask.size
    
    # Set alpha channel to 0 (transparent) only for edge-connected pixels
    data[edge_connected_mask, 3] = 0
    
    # Create new image from modified data
    result = Image.fromarray(data, 'RGBA')
    
    # Save the result
    result.save(output_path, 'PNG')
    print(f"  Found {total_matching:,} matching pixels, made {edge_connected:,} edge-connected pixels transparent")
    print(f"  Protected {total_matching - edge_connected:,} interior pixels")


def batch_process(input_dir, output_dir=None, target_color=None, tolerance=20):
    """
    Batch process all PNG files in a directory.
    
    Args:
        input_dir: Directory containing input PNG files
        output_dir: Directory for output files (default: input_dir + '_transparent')
        target_color: RGB tuple to make transparent (None = auto-detect for each image)
        tolerance: Color tolerance for matching (0-255)
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' does not exist")
        return
    
    # Set default output directory
    if output_dir is None:
        output_dir = str(input_path) + '_transparent'
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Find all PNG files
    png_files = list(input_path.glob('*.png')) + list(input_path.glob('*.PNG'))
    
    if not png_files:
        print(f"No PNG files found in '{input_dir}'")
        return
    
    print(f"Found {len(png_files)} PNG file(s)")
    print(f"Output directory: {output_dir}")
    if target_color:
        print(f"Target color: RGB{target_color}")
    else:
        print("Mode: Auto-detect background color for each image")
    print(f"Tolerance: {tolerance}")
    print("Mode: Edge-connected pixels only")
    print()
    
    # Process each file
    success_count = 0
    for i, png_file in enumerate(png_files, 1):
        output_file = output_path / png_file.name
        print(f"[{i}/{len(png_files)}] {png_file.name}")
        
        try:
            make_background_transparent(png_file, output_file, target_color, tolerance)
            success_count += 1
        except Exception as e:
            print(f"  Error: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\nDone! Successfully processed {success_count}/{len(png_files)} file(s)")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Batch process PNG images to make background pixels transparent. '
                    'Automatically detects background color from image edges. '
                    'Only makes pixels transparent if connected to the edge.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Auto-detect background color for each image
  %(prog)s ./my_images
  
  # Specify a custom output directory
  %(prog)s ./my_images -o ./processed_images
  
  # Use a specific background color (gray)
  %(prog)s ./my_images -c 128,128,128
  
  # Adjust tolerance for color matching
  %(prog)s ./my_images -t 50
        """
    )
    parser.add_argument(
        'input_dir',
        help='Directory containing PNG files to process'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output directory (default: input_dir + "_transparent")'
    )
    parser.add_argument(
        '-c', '--color',
        help='Target RGB color as "R,G,B" (default: auto-detect)',
        default=None
    )
    parser.add_argument(
        '-t', '--tolerance',
        type=int,
        default=20,
        help='Color matching tolerance 0-255 (default: 20)'
    )
    
    args = parser.parse_args()
    
    # Parse color if provided
    target_color = None
    if args.color:
        try:
            r, g, b = map(int, args.color.split(','))
            target_color = (r, g, b)
        except:
            print("Error: Color must be in format 'R,G,B' (e.g., '128,128,128')")
            sys.exit(1)
    
    batch_process(args.input_dir, args.output, target_color, args.tolerance)