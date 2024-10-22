import streamlit as st
import geojson



with open('local-authority-district.geojson') as f:
    gj=geojson.load(f)

st.write(gj['features'][1])
st.title("🎈 My new app")
st.write(
'''hello_world''')
