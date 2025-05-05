import streamlit as st
import base64

def set_background(image_file):
    """Sets the background of the Streamlit app."""
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.write(style, unsafe_allow_html=True)

def main():
    """Main function to run the Streamlit app."""
    set_background("FONDO SIST CMM (CLARO).png") # Reemplaza con la ruta de tu imagen

    st.title("Soportes CMM")
    

if __name__ == "__main__":
    main()
