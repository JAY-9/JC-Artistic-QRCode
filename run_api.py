"""
Launch script for the Artistic QR Code Generator API
"""

import uvicorn

if __name__ == "__main__":
    print("Starting Artistic QR Code Generator API...")
    print("API Documentation: http://localhost:8000/docs")
    print("API Endpoint: http://localhost:8000/generate-qr")
    print("\nPress CTRL+C to stop the server\n")
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
