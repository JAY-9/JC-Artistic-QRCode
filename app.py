import streamlit as st
import os
from qr_generator import generate_artistic_qr

# Page config
st.set_page_config(page_title="Artistic QR Code Generator", page_icon="🎨", layout="centered")

st.title("🎨 Artistic QR Code Generator")
st.markdown("Generate stunning QR codes with your own logo/background using the `amzqr` library.")

# Sidebar for instructions
with st.sidebar:
    st.header("Instructions")
    st.markdown("""
    1. Enter the URL you want the QR code to point to.
    2. Upload an image (Logo or Background).
    3. Choose if you want the QR code to be colorized.
    4. Click 'Generate' and wait for the magic!
    """)
    st.info("Note: Square images work best for logos.")

# Inputs
url = st.text_input("Enter URL/Text", "https://example.com")
uploaded_file = st.file_uploader("Upload Image (Logo/Background)", type=['jpg', 'png', 'jpeg', 'gif'])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

# Options
col1, col2 = st.columns(2)
with col1:
    colorized = st.checkbox("Colorized", value=True, help="Keep the original colors of the image")
with col2:
    # Future expansion: Level or version controls
    pass

if st.button("Generate QR Code", type="primary"):
    if not url:
        st.error("Please enter a URL first!")
    elif not uploaded_file:
        st.error("Please upload an image first!")
    else:
        with st.spinner("Generating Artistic QR Code..."):
            try:
                # Create a temporary directory for processing
                temp_dir = "temp_qr_gen"
                os.makedirs(temp_dir, exist_ok=True)
                
                # Save uploaded file
                file_ext = uploaded_file.name.split('.')[-1]
                input_image_path = os.path.join(temp_dir, f"input.{file_ext}")
                with open(input_image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Generate QR code using the reusable module
                qr_name, output_filename = generate_artistic_qr(
                    payload=url,
                    image_path=input_image_path,
                    colorized=colorized,
                    output_dir=temp_dir
                )
                
                # Display Result
                st.success("QR Code Generated!")
                st.image(qr_name, caption="Generated Artistic QR Code (HD)", use_container_width=True)
                
                # Download Button
                with open(qr_name, "rb") as file:
                    st.download_button(
                        label="Download HD QR Code",
                        data=file,
                        file_name=output_filename,
                        mime=f"image/{'gif' if file_ext.lower() == 'gif' else 'png'}"
                    )
                    
            except ValueError as e:
                st.error(f"Validation error: {str(e)}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
