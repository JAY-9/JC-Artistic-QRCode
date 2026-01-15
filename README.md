# Artistic QR Code Generator

A web application that generates high-definition artistic QR codes with custom logos using Python and Streamlit.

## Features

- 🎨 **Custom Logo Integration**: Upload your own logo or background image
- 🖼️ **High Definition Output**: Automatically upscales to 2048px for crisp, sharp results
- 🎨 **Colorized Mode**: Preserve original colors from your logo
- 📥 **Instant Download**: Download your HD QR code immediately
- 📱 **Scannable**: All generated QR codes are fully functional and scannable

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python run_app.py
```

The app will open in your browser at `http://localhost:8501`

### How to Use

1. Enter the URL or text you want to encode
2. Upload an image (logo or background)
   - Square images work best
   - Supports JPG, PNG, JPEG, GIF
3. Choose colorized or black & white mode
4. Click "Generate QR Code"
5. Download your HD QR code!

## Files

- `app.py` - Main Streamlit application
- `run_app.py` - Wrapper script to launch the app
- `requirements.txt` - Python dependencies
- `test_import.py` - Import verification script

## Technical Details

- **Library**: Uses `amzqr` for QR code generation with artistic backgrounds
- **Upscaling**: Pillow (PIL) with LANCZOS resampling for HD quality
- **Output Resolution**: 2048px width (maintains aspect ratio)
- **Framework**: Streamlit for the web interface

## Tips

- Use high-quality logos for best results
- Square images integrate better than rectangular ones
- Shorter URLs create simpler QR patterns (easier to scan)
- Test scannability with your phone camera after generation

## License

Open source - feel free to use and modify!
