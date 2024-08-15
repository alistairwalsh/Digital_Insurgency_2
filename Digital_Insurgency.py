import streamlit as st

def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

st.title('Digital Insurgency')
st.markdown("#### Unleashing the System's Edge")
st.image('images/Digital_Insurgency.jpg')

st.header('The World', divider='grey')
st.write(load_text('text/the_world.txt'))

st.header('Storyline', divider='grey')
st.write(load_text('text/storyline.txt'))
