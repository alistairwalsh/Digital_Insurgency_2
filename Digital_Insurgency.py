import streamlit as st
from utils import set_page_config, load_text

set_page_config()

st.title('Digital Insurgency')
st.markdown("#### Unleashing the System's Edge")
st.image('images/Digital_Insurgency.jpg')

st.header('The World', divider='grey')
st.write(load_text('text/the_world.txt'))

st.header('Storyline', divider='grey')
st.write(load_text('text/storyline.txt'))
