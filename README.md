# Artistic QR Code Generator

A web application and REST API that generates high-definition artistic QR codes with custom logos using Python, Streamlit, and FastAPI.

## Features

- 🎨 **Custom Logo Integration**: Upload your own logo or background image
- 🖼️ **High Definition Output**: Automatically upscales to 2048px for crisp, sharp results
- 🎨 **Colorized Mode**: Preserve original colors from your logo
- 📥 **Instant Download**: Download your HD QR code immediately
- 📱 **Scannable**: All generated QR codes are fully functional and scannable
- 🚀 **REST API**: Programmatic access via FastAPI endpoint

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Interface (Streamlit)

Run the Streamlit application:
```bash
python run_app.py
```

The app will open in your browser at `http://localhost:8501`

#### How to Use the Web Interface

1. Enter the URL or text you want to encode
2. Upload an image (logo or background)
   - Square images work best
   - Supports JPG, PNG, JPEG, GIF
3. Choose colorized or black & white mode
4. Click "Generate QR Code"
5. Download your HD QR code!

### REST API

Run the API server:
```bash
python run_api.py
```

The API will be available at `http://localhost:8000`

#### API Endpoints

- **POST** `/generate-qr` - Generate artistic QR code
- **GET** `/` - API information
- **GET** `/health` - Health check
- **GET** `/docs` - Interactive API documentation (Swagger UI)

#### API Usage Examples

**Using curl:**
```bash
curl -X POST "http://localhost:8000/generate-qr" \
  -F "payload=https://example.com" \
  -F "image=@logo.png" \
  -F "colorized=true" \
  --output qr_code.png
```

**Using Python requests:**
```python
import requests

url = "http://localhost:8000/generate-qr"

with open("logo.png", "rb") as image_file:
    files = {"image": image_file}
    data = {
        "payload": "https://example.com",
        "colorized": "true"
    }
    
    response = requests.post(url, files=files, data=data)
    
    if response.status_code == 200:
        with open("qr_code.png", "wb") as f:
            f.write(response.content)
        print("QR code generated successfully!")
    else:
        print(f"Error: {response.json()}")
```

**Using JavaScript (fetch):**
```javascript
const formData = new FormData();
formData.append('payload', 'https://example.com');
formData.append('image', fileInput.files[0]);
formData.append('colorized', 'true');

fetch('http://localhost:8000/generate-qr', {
    method: 'POST',
    body: formData
})
.then(response => response.blob())
.then(blob => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'qr_code.png';
    a.click();
});
```

#### API Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `payload` | string | Yes | - | Text or URL to encode in the QR code |
| `image` | file | Yes | - | Logo or background image (JPG, PNG, JPEG, GIF) |
| `colorized` | boolean | No | true | Preserve original image colors |

#### API Response

- **Success (200)**: Returns the generated QR code image file
- **Error (400)**: Invalid parameters or file type
- **Error (500)**: QR code generation failed

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
