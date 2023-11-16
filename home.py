import streamlit as st
import leafmap.foliumap as leafmap
import os

st.title("Project Canopy 🌲")

st.markdown(
    """
Project Canopy allows you to select any area of your choice and produces a comprehensive deforestation report on it.
Check out https://www.projectcanopy.org/ for more details. 

"""
)
# [21.920471,-0.556174]
m = leafmap.Map(locate_control=True)
m.add_basemap("ROADMAP")
m = leafmap.Map(center=[21.920471, -0.556174], zoom=2)

input_mask_folder = "output"
dir_values = os.listdir(input_mask_folder)
for i in range(len(dir_values)):
    if dir_values[i].endswith(".geojson"):
        in_geojson = "output/" + dir_values[i]
        m.add_geojson(in_geojson, layer_name=dir_values[i])

m.to_streamlit(height=700)
