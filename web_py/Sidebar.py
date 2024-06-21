import streamlit as st
def show_sidebar():
    st.sidebar.header("VEHICLE DETECTION SENSOR")

    A1 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด A1", value=False)
    A2 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด A2", value=False)
    A3 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด A3", value=False)
    A4 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด A4", value=False)
    B1 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด B1", value=False)
    B2 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด B2", value=False)
    B3 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด B3", value=False)
    B4 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด B4", value=False)
    return A1,A2,A3,A4,B1,B2,B3,B4