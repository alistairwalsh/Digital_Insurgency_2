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
        return "Character description not available."

characters = ["Nisha Nakamura", "Ren Hayashi", "Gabriel Thorn", "Amelia Rivers", 'Xavier "Bitjammer" Voss', 'Jackson', 'Max', 'Lena', 'Tatiana']

for character in characters:
    with st.expander(character):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            headshot_dir = f'images/character_headshots/{character.replace(" ", "_")}'
            if os.path.exists(headshot_dir):
                for image in os.listdir(headshot_dir):
                    if image.lower().endswith(('.png', '.jpg', '.jpeg')):
                        st.image(os.path.join(headshot_dir, image), use_column_width=True)
            else:
                st.write("Character image not available.")
        
        with col2:
            info = load_character_info(character.replace(" ", "_"))
            st.write(info)

