import streamlit as st
import os
from utils import set_page_config, create_sidebar, load_text

set_page_config()
create_sidebar()

st.title('Characters')

def load_character_info(name):
    try:
        return load_text(f'text/character_descriptions/{name}.txt')
    except FileNotFoundError:
        try:
            return load_text(f'text/character_descriptions/{name.replace("_", " ")}.txt')
        except FileNotFoundError:
            return "Character description not available."

def get_file_name(character):
    if character == 'Xavier "Bitjammer" Voss':
        return "Xavier Bitjammer Voss"
    return character.replace(" ", "_")

characters = ["Nisha Nakamura", "Ren Hayashi", "Gabriel Thorn", "Amelia Rivers", 'Xavier "Bitjammer" Voss', 'Jackson', 'Max', 'Lena', 'Tatiana']

for character in characters:
    with st.expander(character):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            image_path = f'images/character_headshots/{get_file_name(character)}.jpg'
            if os.path.exists(image_path):
                st.image(image_path, use_column_width=True)
            else:
                st.write("Character image not available.")
        
        with col2:
            info = load_character_info(get_file_name(character))
            sections = info.split("###")
            for section in sections:
                if section.strip():
                    parts = section.split(":", 1)
                    if len(parts) == 2:
                        title, content = parts
                        st.subheader(title.strip())
                        st.write(content.strip())
                    else:
                        st.write(section.strip())
        
        if character == "Nisha Nakamura":
            st.video('video/Nisha.mp4')
            st.video('video/87a2237a-4b3f-4775-9e0d-7655c0c0b273.mp4')

        if character == "Amelia Rivers":
            st.image('images/DreamShaper_v5_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_di_0 (3).jpg')
            st.write('Sitting at the bar is a young girl with captivating eyes, lost in thought.')
            st.image('images/PXL_20230702_065835869.PORTRAIT.jpg', width=300)
            st.write("Thank you for letting me use your image. I was so focused on what I was doing I forgot to get your name - say hi in the comments and I'll add your name to the character. :-).")

        if character == 'Xavier "Bitjammer" Voss':
            st.image('images/SDXL_09_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_sunlight_0.jpg')
            st.write('Bitjammer sits at the entrance, he is wearing his AI image rig mounted to his chest to capture images of the patrons.')
            st.image('images/PXL_20230716_050909165.jpg', width=300)
            st.write("Once again, thank you for letting me use your image.")

