import streamlit as st
import pandas as pd
import pydeck as pdk
import webbrowser
    

st.write("## These are links to various sites with Realtime Cyber Threat Information ")
st.write(" ")

st.link_button(":yellow[Check Points ThreatCloud AI]", "https://threatmap.checkpoint.com/", use_container_width=True)
st.link_button(":yellow[Radwar's Live Threat Map]", "https://livethreatmap.radware.com/", use_container_width=True)
st.link_button(":yellow[Phenomenati's Resource Center]", "https://phenomenati.com/threat-intel-%26-dashboards", use_container_width=True)
st.link_button(":yellow[National Vulnerability Database]", "https://nvd.nist.gov/general/nvd-dashboard", use_container_width=True)
