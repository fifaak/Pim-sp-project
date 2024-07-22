import streamlit as st
import datetime
import folium
from streamlit.components.v1 import html
from Map import create_map
from Logic import GET_TFL
from Sidebar import *
from math_logic import *
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time
import requests

# Force Streamlit to rerun the script and clear cache
st.set_page_config(page_title="Traffic Monitoring App", layout="wide")
st.cache_data.clear()

# Custom CSS for removing top margin or padding
st.markdown("""
    <style>
    /* Remove top margin or padding */
    body {
        margin: 0px;
        padding: 0px;
    }
    .main {
        padding-top: 0px !important;
        margin-top: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

def send_line_notify(token, message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code

def send_line_notify_with_image(token, message, image_path):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "message": message
    }
    files = {
        "imageFile": open(image_path, "rb")
    }
    response = requests.post(url, headers=headers, data=payload, files=files)
    return response.status_code, response.json()

def create_traffic_graph(times, sensor1_data, sensor2_data):
    fig = make_subplots(rows=1, cols=1)
    
    fig.add_trace(
        go.Scatter(x=times, y=sensor1_data, mode='lines+markers', name='Sensor 1', line=dict(color='blue')),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=times, y=sensor2_data, mode='lines+markers', name='Sensor 2', line=dict(color='red')),
        row=1, col=1
    )
    
    fig.update_layout(
        title='Real-time Traffic Data',
        xaxis_title='Time',
        yaxis_title='Traffic Amount',
        height=300,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    
    fig.update_xaxes(
        tickformat="%H:%M:%S",
        tickangle=45,
        tickmode='auto',
        nticks=5,
        rangeslider_visible=False
    )
    
    return fig

def main():
    st.title("ระบบตรวจรถติดหน้าบิ๊กซีเพลสสาขาสระบุรี")

    # Replace 'YOUR_TOKEN' with your Line Notify token
    token = '4bC9CyPGMlFdUfSLwTFL47TG1bccAEz3bSdh4hJ6upp'

    # Create a sidebar
    st.sidebar.title("Traffic Graph")
    
    # Create empty placeholders for the graph and data
    graph_placeholder = st.sidebar.empty()
    times = []
    sensor1_data = []
    sensor2_data = []
    
    TEMP_STATE = "NORMAL"
    
    # Main loop
    while True:
        current_time = datetime.datetime.now()
        
        A1, A2, A3, A4, B1, B2, B3, B4 = show_sidebar()
        output = GET_TFL(A1, A2, A3, A4, B1, B2, B3, B4)
        
        # Update sensor data and time
        times.append(current_time)
        sensor1_data.append(sum([A1, A2, A3, A4]))
        sensor2_data.append(sum([B1, B2, B3, B4]))
        
        # Keep only the last 50 data points
        times = times[-50:]
        sensor1_data = sensor1_data[-50:]
        sensor2_data = sensor2_data[-50:]
        
        # Update the graph
        fig = create_traffic_graph(times, sensor1_data, sensor2_data)
        graph_placeholder.plotly_chart(fig, use_container_width=True)
        
        st.write(f"ถนนฝั่งรร.อนุบาลสระบุรี: {output[0]}, ถนนสายรร.สระบุรีวิทยาคม: {output[1]}, สถานะ: {output[2]}")
        
        # Prepare the states to pass to the map
        A_states = {"A1": A1, "A2": A2, "A3": A3, "A4": A4}
        B_states = {"B1": B1, "B2": B2, "B3": B3, "B4": B4}

        # Create the map with updated icon states
        my_map = create_map(A_states, B_states, output)

        if (output[2] == "ALERT"):
            if (output[1] == "GREEN"):
                road = "โรงเรียนสระบุรีวิทยาคม"
            else:
                road = "โรงเรียนอนุบาลสระบุรี"
            TEMP_STATE = "ALERT"
            st.warning(f'เตือน!!! ณ เวลา {current_time.strftime("%d/%m/%Y %H:%M น.")} \n ถนนฝั่ง {road} ตรวจพบการจราจรติดขัด')
        elif (output[2] == "NORMAL") and (TEMP_STATE == "ALERT"):
            st.warning(f'ณ เวลา {current_time.strftime("%d/%m/%Y %H:%M น.")} การจราจรกลับมาเป็นปกติ')
            TEMP_STATE = "NORMAL"
        print("TEMP_STATE:", TEMP_STATE)

        # Display the map using an HTML iframe
        with open("map.html", "r") as f:
            map_html = f.read()
        map_html = f"""
        <div style="width: 100vw; height: 800px;">
            {map_html}
        </div>
        """

        st.components.v1.html(map_html, height=700)
        
        # Add a short delay to control the update frequency
        time.sleep(1)  # Update every second

if __name__ == "__main__":
    main()