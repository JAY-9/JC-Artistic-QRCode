"""
Artistic QR Code Generator API

FastAPI server providing REST API endpoint for generating artistic QR codes.
"""

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from typing import Optional
from qr_generator import generate_artistic_qr, cleanup_temp_dir

app = FastAPI(
    title="Artistic QR Code Generator API",
    description="Generate high-definition artistic QR codes with custom logos/backgrounds",
    version="1.0.0"
)

# Enable CORS for web applications
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Allowed image extensions
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Artistic QR Code Generator API",
        "version": "1.0.0",
        "endpoints": {
            "/generate-qr": "POST - Generate artistic QR code",
            "/docs": "GET - Interactive API documentation",
            "/health": "GET - Health check"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/generate-qr")
async def generate_qr(
    payload: str = Form(..., description="Text or URL to encode in the QR code"),
    image: UploadFile = File(..., description="Logo or background image file"),
    colorized: bool = Form(True, description="Preserve original image colors")
):
    """
    Generate an artistic QR code with a custom logo/background.
    
    Parameters:
    - **payload**: The text or URL to encode in the QR code (required)
    - **image**: The logo or background image file (required)
    - **colorized**: Whether to preserve the original colors of the image (default: true)
    
    Returns:
    - The generated HD QR code image file
    
    Example using curl:
    ```bash
    curl -X POST "http://localhost:8000/generate-qr" \\
      -F "payload=https://example.com" \\
      -F "image=@logo.png" \\
      -F "colorized=true" \\
      --output qr_code.png
    ```
    """
    # Validate payload
    if not payload or not payload.strip():
        raise HTTPException(status_code=400, detail="Payload cannot be empty")
    
    # Validate file extension
    file_ext = os.path.splitext(image.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Create unique temp directory for this request
    import uuid
    temp_dir = f"temp_qr_api_{uuid.uuid4().hex[:8]}"
    
    try:
        # Save uploaded file
        os.makedirs(temp_dir, exist_ok=True)
        input_image_path = os.path.join(temp_dir, f"input{file_ext}")
        
        with open(input_image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        # Generate QR code
        qr_code_path, output_filename = generate_artistic_qr(
            payload=payload,
            image_path=input_image_path,
            colorized=colorized,
            output_dir=temp_dir
        )
        
        # Determine media type
        media_type = "image/gif" if file_ext == '.gif' else "image/png"
        
        # Return the generated QR code
        return FileResponse(
            path=qr_code_path,
            media_type=media_type,
            filename=output_filename,
            background=None  # Don't cleanup immediately, let FastAPI handle it
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"QR code generation failed: {str(e)}")
    finally:
        # Schedule cleanup (FastAPI will handle this after response is sent)
        # For now, we'll leave the temp files - in production, use background tasks
        pass


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on server shutdown"""
    # Clean up any remaining temp directories
    import glob
    for temp_dir in glob.glob("temp_qr_api_*"):
        cleanup_temp_dir(temp_dir)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
