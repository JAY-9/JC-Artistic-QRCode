"""
Artistic QR Code Generator Module

This module provides the core functionality for generating artistic QR codes
with custom logos/backgrounds using the amzqr library and Pillow for HD upscaling.
"""

import os
import shutil
from typing import Tuple, Optional
from amzqr import amzqr
from PIL import Image


def generate_artistic_qr(
    payload: str,
    image_path: str,
    colorized: bool = True,
    output_dir: str = "temp_qr_gen",
    target_width: int = 2048
) -> Tuple[str, str]:
    """
    Generate an artistic QR code with a custom logo/background.
    
    Args:
        payload: The text/URL to encode in the QR code
        image_path: Path to the logo/background image file
        colorized: Whether to preserve the original colors of the image
        output_dir: Directory to save temporary and output files
        target_width: Target width for HD upscaling (default: 2048px)
    
    Returns:
        Tuple of (qr_code_path, output_filename)
        
    Raises:
        ValueError: If payload is empty or image_path doesn't exist
        Exception: If QR code generation fails
    """
    # Validation
    if not payload or not payload.strip():
        raise ValueError("Payload cannot be empty")
    
    if not os.path.exists(image_path):
        raise ValueError(f"Image file not found: {image_path}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Determine output filename based on input image extension
    file_ext = os.path.splitext(image_path)[1].lower()
    if file_ext in ['.gif']:
        output_filename = "artistic_qrcode.gif"
    else:
        output_filename = "artistic_qrcode.png"
    
    try:
        # Generate QR code using amzqr
        version, level, qr_name = amzqr.run(
            words=payload,
            picture=image_path,
            colorized=colorized,
            save_name=output_filename,
            save_dir=output_dir
        )
        
        # HD Upscaling
        img = Image.open(qr_name)
        
        # Calculate target dimensions maintaining aspect ratio
        w_percent = (target_width / float(img.size[0]))
        target_height = int((float(img.size[1]) * float(w_percent)))
        
        # Upscale using high-quality LANCZOS filter
        img_hd = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        # Save the HD version
        img_hd.save(qr_name)
        
        return qr_name, output_filename
        
    except Exception as e:
        raise Exception(f"QR code generation failed: {str(e)}")


def cleanup_temp_dir(temp_dir: str = "temp_qr_gen") -> None:
    """
    Clean up temporary directory used for QR code generation.
    
    Args:
        temp_dir: Directory to clean up
    """
    if os.path.exists(temp_dir):
        try:
            shutil.rmtree(temp_dir)
        except Exception as e:
            print(f"Warning: Failed to cleanup temp directory: {str(e)}")
