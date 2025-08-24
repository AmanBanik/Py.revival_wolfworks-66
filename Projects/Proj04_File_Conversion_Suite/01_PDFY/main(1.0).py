"""
<parameter name="title">PDFY - PDF Conversion Tool#!/usr/bin/env python3
PDFY - PDF Conversion Tool
Converts all images to PDFs and keeps existing PDFs in original resolution
Maintains chronological order based on filename sorting
"""

import os
import sys
from pathlib import Path
from PIL import Image
import shutil
from typing import List, Set

# Supported image formats
SUPPORTED_IMAGE_FORMATS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif', '.webp'}
PDF_FORMAT = '.pdf'

def get_supported_files(directory: Path) -> tuple[List[Path], List[Path]]:
    """
    Get lists of PDF files and image files from directory
    Returns: (pdf_files, image_files) sorted chronologically
    """
    all_files = [f for f in directory.iterdir() if f.is_file()]
    
    pdf_files = []
    image_files = []
    
    for file in all_files:
        if file.suffix.lower() == PDF_FORMAT:
            pdf_files.append(file)
        elif file.suffix.lower() in SUPPORTED_IMAGE_FORMATS:
            image_files.append(file)
    
    # Sort chronologically (assuming filenames are in chronological order)
    pdf_files.sort(key=lambda x: x.name)
    image_files.sort(key=lambda x: x.name)
    
    return pdf_files, image_files

def convert_image_to_pdf(image_path: Path, output_path: Path) -> bool:
    """
    Convert an image to PDF format maintaining original resolution
    """
    try:
        with Image.open(image_path) as img:
            # Convert RGBA to RGB if necessary (for PNG with transparency)
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Handle DPI information more robustly
            try:
                dpi = img.info.get('dpi')
                if dpi is None:
                    # No DPI info, use default
                    resolution = 300
                elif isinstance(dpi, (tuple, list)) and len(dpi) >= 2:
                    # DPI is a tuple/list, use first value or average
                    resolution = int(dpi[0]) if isinstance(dpi[0], (int, float)) else 300
                elif isinstance(dpi, (int, float)):
                    # DPI is a single number
                    resolution = int(dpi)
                else:
                    # Fallback to default
                    resolution = 300
            except:
                resolution = 300
            
            # Save as PDF with proper resolution handling
            img.save(output_path, 'PDF', resolution=resolution)
            return True
            
    except Exception as e:
        print(f"Error converting {image_path.name}: {e}")
        return False

def copy_existing_pdf(src_path: Path, dest_path: Path) -> bool:
    """
    Copy existing PDF to output directory
    """
    try:
        if src_path != dest_path:  # Only copy if different locations
            shutil.copy2(src_path, dest_path)
        return True
    except Exception as e:
        print(f"Error copying {src_path}: {e}")
        return False

def process_directory(input_dir: str, output_dir: str = None) -> None:
    """
    Process all files in directory, converting images to PDFs and copying existing PDFs
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"Error: Input directory '{input_dir}' does not exist")
        return
    
    if not input_path.is_dir():
        print(f"Error: '{input_dir}' is not a directory")
        return
    
    # Set output directory (same as input if not specified)
    if output_dir is None:
        output_path = input_path
    else:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Processing directory: {input_path}")
    print(f"Output directory: {output_path}")
    
    # Get files to process
    pdf_files, image_files = get_supported_files(input_path)
    
    print(f"\nFound {len(pdf_files)} PDF files and {len(image_files)} image files")
    
    if not pdf_files and not image_files:
        print("No supported files found in directory")
        return
    
    # Process statistics
    processed_count = 0
    error_count = 0
    
    # Process existing PDFs
    if pdf_files:
        print(f"\nProcessing {len(pdf_files)} existing PDF files...")
        for pdf_file in pdf_files:
            output_file = output_path / pdf_file.name
            if copy_existing_pdf(pdf_file, output_file):
                print(f"✓ Kept: {pdf_file.name}")
                processed_count += 1
            else:
                print(f"✗ Failed: {pdf_file.name}")
                error_count += 1
    
    # Process image files
    if image_files:
        print(f"\nProcessing {len(image_files)} image files...")
        for image_file in image_files:
            # Generate output filename (keep original name + .pdf extension)
            # Change this line to: output_name = image_file.name + '.pdf' 
            # if you want to keep original extension (e.g., image.jpg.pdf)
            output_name = image_file.stem + '.pdf'  # Current: replaces extension
            output_file = output_path / output_name
            
            if convert_image_to_pdf(image_file, output_file):
                print(f"✓ Converted: {image_file.name} → {output_name}")
                processed_count += 1
            else:
                print(f"✗ Failed: {image_file.name}")
                error_count += 1
    
    # Summary
    print(f"\n=== Processing Complete ===")
    print(f"Successfully processed: {processed_count} files")
    print(f"Errors: {error_count} files")
    print(f"Total files processed: {processed_count + error_count}")
    
    if output_path != input_path:
        print(f"All PDFs saved to: {output_path}")

def get_user_input() -> tuple[str, str]:
    """
    Get input and output directory paths from user
    """
    print("=== PDFY ===")
    print("This tool converts images to PDFs and keeps existing PDFs\n")
    
    # Get input directory
    while True:
        input_dir = input("Enter the input directory path: ").strip()
        if not input_dir:
            print("Please enter a valid path")
            continue
        
        # Remove quotes if user added them
        input_dir = input_dir.strip('"').strip("'")
        
        if Path(input_dir).exists():
            break
        else:
            print(f"Directory '{input_dir}' does not exist. Please try again.")
    
    # Get output directory
    while True:
        output_dir = input("Enter the output directory path (or press Enter for same as input): ").strip()
        
        # If empty, use same as input
        if not output_dir:
            output_dir = input_dir
            print(f"Using input directory as output: {output_dir}")
            break
        
        # Remove quotes if user added them
        output_dir = output_dir.strip('"').strip("'")
        
        # Check if parent directory exists (we'll create the output dir if needed)
        output_path = Path(output_dir)
        try:
            # Try to create the directory to test if path is valid
            output_path.mkdir(parents=True, exist_ok=True)
            break
        except Exception as e:
            print(f"Cannot create directory '{output_dir}': {e}")
            print("Please try again.")
    
    return input_dir, output_dir

def main():
    """
    Main function - gets user input interactively or from command line
    """
    # Check if command line arguments were provided
    if len(sys.argv) >= 2:
        # Use command line arguments
        input_directory = sys.argv[1]
        output_directory = sys.argv[2] if len(sys.argv) > 2 else None
        print(f"Using command line arguments:")
        print(f"Input: {input_directory}")
        print(f"Output: {output_directory if output_directory else 'Same as input'}")
    else:
        # Get input interactively
        input_directory, output_directory = get_user_input()
    
    print(f"\n{'='*50}")
    print(f"Starting conversion process...")
    print(f"{'='*50}")
    
    try:
        process_directory(input_directory, output_directory)
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    input("\nPress Enter to exit...")  # Keep terminal open
    
    try:
        process_directory(input_directory, output_directory)
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()