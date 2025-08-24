"""
<parameter name="title">PDMUGGY - PDF Merger Tool#!/usr/bin/env python3
PDMUGGY - PDF Merger Tool
Merges all PDFs in a directory in chronological order into a single PDF
Companion tool to PDFY
"""

import os
import sys
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from typing import List
import datetime
import re

def natural_sort_key(text: str) -> List:
    """
    Convert a string into a list of mixed strings and integers for natural sorting
    This makes '2' come before '10' instead of after it
    """
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r'(\d+)', text)]

def get_pdf_files(directory: Path) -> List[Path]:
    """
    Get all PDF files from directory sorted chronologically by filename (natural sort)
    """
    pdf_files = []
    
    for file in directory.iterdir():
        if file.is_file() and file.suffix.lower() == '.pdf':
            pdf_files.append(file)
    
    # Sort using natural sorting (handles numbers properly)
    pdf_files.sort(key=lambda x: natural_sort_key(x.name))
    
    return pdf_files

def merge_pdfs(pdf_files: List[Path], output_path: Path) -> bool:
    """
    Merge multiple PDF files into a single PDF
    """
    try:
        writer = PdfWriter()
        
        print(f"Merging {len(pdf_files)} PDF files...")
        
        for i, pdf_file in enumerate(pdf_files, 1):
            try:
                print(f"  [{i}/{len(pdf_files)}] Adding: {pdf_file.name}")
                
                with open(pdf_file, 'rb') as file:
                    reader = PdfReader(file)
                    
                    # Add all pages from this PDF
                    for page_num in range(len(reader.pages)):
                        page = reader.pages[page_num]
                        writer.add_page(page)
                        
            except Exception as e:
                print(f"  ⚠️  Warning: Could not process {pdf_file.name}: {e}")
                continue
        
        # Write the merged PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        # Add metadata
        try:
            writer.add_metadata({
                '/Title': output_path.stem,
                '/Creator': 'PDMUGGY',
                '/Producer': 'PDMUGGY',
                '/CreationDate': datetime.datetime.now().strftime("D:%Y%m%d%H%M%S")
            })
        except:
            pass  # Metadata is optional
        
        return True
        
    except Exception as e:
        print(f"Error during merge: {e}")
        return False

def get_user_input() -> tuple[str, str, str]:
    """
    Get input directory, output directory, and filename from user
    """
    print("=== PDMUGGY ===")
    print("This tool merges all PDFs in a directory into a single PDF file\n")
    
    # Get input directory
    while True:
        input_dir = input("Enter the directory containing PDF files to merge: ").strip()
        if not input_dir:
            print("Please enter a valid path")
            continue
        
        # Remove quotes if user added them
        input_dir = input_dir.strip('"').strip("'")
        
        input_path = Path(input_dir)
        if input_path.exists() and input_path.is_dir():
            # Check if directory contains PDFs
            pdf_files = get_pdf_files(input_path)
            if pdf_files:
                print(f"Found {len(pdf_files)} PDF files to merge")
                break
            else:
                print("No PDF files found in this directory. Please try another directory.")
        else:
            print(f"Directory '{input_dir}' does not exist. Please try again.")
    
    # Get output directory
    while True:
        output_dir = input("Enter the output directory (where to save merged PDF): ").strip()
        if not output_dir:
            print("Please enter a valid path")
            continue
        
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
    
    # Get output filename
    while True:
        filename = input("Enter the name for merged PDF (without .pdf extension): ").strip()
        if not filename:
            print("Please enter a valid filename")
            continue
        
        # Remove any existing .pdf extension if user added it
        if filename.lower().endswith('.pdf'):
            filename = filename[:-4]
        
        # Check for invalid characters
        invalid_chars = '<>:"/\\|?*'
        if any(char in filename for char in invalid_chars):
            print(f"Filename cannot contain these characters: {invalid_chars}")
            continue
        
        break
    
    return input_dir, output_dir, filename

def preview_merge_operation(input_dir: str, output_dir: str, filename: str) -> bool:
    """
    Show user what will be merged and ask for confirmation
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir) / f"{filename}.pdf"
    pdf_files = get_pdf_files(input_path)
    
    print(f"\n{'='*60}")
    print("MERGE PREVIEW")
    print(f"{'='*60}")
    print(f"Input Directory:  {input_dir}")
    print(f"Output File:      {output_path}")
    print(f"Files to merge:   {len(pdf_files)} PDFs")
    print(f"\nFiles will be merged in this order:")
    
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"  {i:2d}. {pdf_file.name}")
    
    print(f"\n{'='*60}")
    
    # Ask for confirmation
    while True:
        confirm = input("Proceed with merge? (y/n): ").strip().lower()
        if confirm in ['y', 'yes']:
            return True
        elif confirm in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no")

def main():
    """
    Main function - handles the PDF merging process
    """
    try:
        # Check if command line arguments were provided
        if len(sys.argv) >= 4:
            # Use command line arguments: input_dir output_dir filename
            input_directory = sys.argv[1]
            output_directory = sys.argv[2] 
            output_filename = sys.argv[3]
            print(f"Using command line arguments:")
            print(f"Input: {input_directory}")
            print(f"Output: {output_directory}/{output_filename}.pdf")
        else:
            # Get input interactively
            input_directory, output_directory, output_filename = get_user_input()
        
        # Preview the operation
        if not preview_merge_operation(input_directory, output_directory, output_filename):
            print("Operation cancelled by user.")
            return
        
        # Get PDF files
        input_path = Path(input_directory)
        pdf_files = get_pdf_files(input_path)
        
        if not pdf_files:
            print("No PDF files found in the specified directory.")
            return
        
        # Create output path
        output_path = Path(output_directory) / f"{output_filename}.pdf"
        
        print(f"\n{'='*60}")
        print("STARTING MERGE PROCESS")
        print(f"{'='*60}")
        
        # Perform the merge
        if merge_pdfs(pdf_files, output_path):
            print(f"\n✅ SUCCESS!")
            print(f"Merged {len(pdf_files)} PDFs into: {output_path}")
            
            # Show file size
            try:
                file_size = output_path.stat().st_size
                size_mb = file_size / (1024 * 1024)
                print(f"Output file size: {size_mb:.2f} MB")
            except:
                pass
        else:
            print(f"\n❌ FAILED!")
            print("Could not complete the merge operation.")
    
    except KeyboardInterrupt:
        print("\n\nOperation interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()