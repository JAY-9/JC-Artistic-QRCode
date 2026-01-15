import sys
print(f"Python Executable: {sys.executable}")
print(f"Path: {sys.path}")
try:
    import amzqr
    print("SUCCESS: amzqr imported")
except ImportError as e:
    print(f"FAILURE: amzqr not found: {e}")

try:
    import streamlit
    print("SUCCESS: streamlit imported")
except ImportError as e:
    print(f"FAILURE: streamlit not found: {e}")
