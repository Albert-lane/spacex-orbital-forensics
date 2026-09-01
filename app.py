import streamlit as st
from components.live_gauge import render_orbital_asset_freeze_gauge

st.set_page_config(page_title="Orbital Forensics Live Monitor", layout="wide")
st.title("🛰️ SpaceX Orbital Forensics & Compliance Dashboard")

col1, col2 = st.columns([1, 1])
with col1:
    render_orbital_asset_freeze_gauge()
with col2:
    st.subheader("System Status")
    st.success("Telemetry Exporter Active on Port 9101")
    st.info("Polling SQLite: orbital_forensics.db")
