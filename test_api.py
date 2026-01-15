"""
Test script for the Artistic QR Code Generator API

This script demonstrates how to use the API endpoint to generate QR codes.
"""

import requests
import os

# API endpoint
API_URL = "http://localhost:8000/generate-qr"

def test_api_with_sample_image():
    """
    Test the API with a sample image.
    Make sure the API server is running (python run_api.py) before running this test.
    """
    
    # Check if sample image exists
    if not os.path.exists("test_logo.png"):
        print("Error: test_logo.png not found!")
        print("Please create a test image or update the path in this script.")
        return
    
    print("Testing Artistic QR Code Generator API...")
    print(f"API URL: {API_URL}")
    
    # Prepare the request
    with open("test_logo.png", "rb") as image_file:
        files = {"image": image_file}
        data = {
            "payload": "https://github.com",
            "colorized": "true"
        }
        
        print("\nSending request...")
        print(f"   Payload: {data['payload']}")
        print(f"   Colorized: {data['colorized']}")
        
        try:
            response = requests.post(API_URL, files=files, data=data)
            
            if response.status_code == 200:
                # Save the generated QR code
                output_filename = "test_qr_code.png"
                with open(output_filename, "wb") as f:
                    f.write(response.content)
                
                print(f"\nSuccess! QR code generated and saved as '{output_filename}'")
                print(f"   File size: {len(response.content)} bytes")
                print(f"   Content-Type: {response.headers.get('content-type')}")
                
            else:
                print(f"\nError: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("\nConnection Error!")
            print("   Make sure the API server is running:")
            print("   Run: python run_api.py")
        except Exception as e:
            print(f"\nError: {str(e)}")


def test_api_error_handling():
    """Test API error handling with invalid inputs"""
    
    print("\n\nTesting API Error Handling...")
    
    # Test 1: Missing payload
    print("\nTest 1: Missing payload parameter")
    try:
        with open("test_logo.png", "rb") as image_file:
            files = {"image": image_file}
            data = {"colorized": "true"}
            response = requests.post(API_URL, files=files, data=data)
            print(f"   Status: {response.status_code} (Expected: 422)")
    except Exception as e:
        print(f"   Error: {str(e)}")
    
    # Test 2: Missing image
    print("\nTest 2: Missing image file")
    try:
        data = {"payload": "https://example.com", "colorized": "true"}
        response = requests.post(API_URL, data=data)
        print(f"   Status: {response.status_code} (Expected: 422)")
    except Exception as e:
        print(f"   Error: {str(e)}")


if __name__ == "__main__":
    print("=" * 60)
    print("Artistic QR Code Generator API - Test Script")
    print("=" * 60)
    
    # Run tests
    test_api_with_sample_image()
    # test_api_error_handling()  # Uncomment to test error handling
    
    print("\n" + "=" * 60)
    print("Test complete!")
    print("=" * 60)
