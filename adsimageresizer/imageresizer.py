import streamlit as st
from PIL import Image
import io

st.subheader("MPG - Google Display Image Resizer - Testing Stage")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Standard ad sizes ads specs 
ad_sizes = {
    "300x250 – Medium Rectangle": (300, 250),
    "728x90 – Leaderboard": (728, 90),
    "160x600 – Wide Skyscraper": (160, 600),
    "300x600 – Half Page": (300, 600),
    "320x100 – Mobile Banner": (320, 100),
    "Custom": None
}

selected_size = st.selectbox("Choose target size", list(ad_sizes.keys()))


if selected_size == "Custom":
    width = st.number_input("Width (px)", min_value=50, value=300)
    height = st.number_input("Height (px)", min_value=50, value=250)
    target_size = (width, height)
else:
    target_size = ad_sizes[selected_size]

# Process button
if uploaded_file and st.button("Resize Image"):
    image = Image.open(uploaded_file)
    image.thumbnail(target_size, Image.Resampling.LANCZOS)

    # Create padded background
    background = Image.new("RGB", target_size, (255, 255, 255))
    offset = ((target_size[0] - image.width) // 2, (target_size[1] - image.height) // 2)
    background.paste(image, offset)

    st.image(background, caption="Resized Image", use_container_width=False)

    # Save to memory and downlaod
    img_bytes = io.BytesIO()
    background.save(img_bytes, format="JPEG")
    st.download_button("Download JPEG", img_bytes.getvalue(), file_name="resized_image.jpg", mime="image/jpeg")

    