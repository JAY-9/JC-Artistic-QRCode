import streamlit as st
from amzqr import amzqr
import os
import shutil

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
                
                # Define output path
                # amzqr usually appends '_qrcode.png' or similar, but we specify save_name
                output_filename = "artistic_qrcode.png"
                if file_ext.lower() == 'gif':
                    output_filename = "artistic_qrcode.gif"
                
                output_path = os.path.join(temp_dir, output_filename)
                
                # Run amzqr
                # version, level, qr_name = amzqr.run(words, version=1, level='H', picture=None, colorized=False, contrast=1.0, brightness=1.0, save_name=None, save_dir=os.getcwd())
                # specific args:
                # words: str
                # picture: str (path)
                # colorized: bool
                # save_name: str (filename)
                # save_dir: str (path)
                
                version, level, qr_name = amzqr.run(
                    words=url,
                    picture=input_image_path,
                    colorized=colorized,
                    save_name=output_filename,
                    save_dir=temp_dir
                )
                
                # --- High Definition Upscaling ---
                from PIL import Image
                
                # Open the generated low-res QR code
                img = Image.open(qr_name)
                
                # Desired HD size (e.g., 2000x2000 or simply 4x larger)
                # Let's target a standardized high resolution like 2048px width
                target_width = 2048
                w_percent = (target_width / float(img.size[0]))
                target_height = int((float(img.size[1]) * float(w_percent)))
                
                # Upscale using High Quality LANCZOS filter
                img_hd = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                
                # Overwrite the original file or save as new
                img_hd.save(qr_name)
                # ---------------------------------
                
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
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            finally:
                # Cleanup is tricky if we want to allow download, 
                # but Streamlit re-runs scripts so we shouldn't delete immediately if we want to serve the file?
                # Actually, reading the file into memory for the download button allows us to delete it from disk if we want, 
                # but for simplicity in this session we can leave the temp dir or clean it up on next run.
                # For now, let's just leave it or clean it up at the START of the script.
                pass

# Cleanup block at start could be better, but for single user local app this is fine.
