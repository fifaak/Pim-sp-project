import streamlit as st
import datetime
import folium
from streamlit.components.v1 import html
from Map import create_map
from Logic import GET_TFL
from Sidebar import *
from math_logic import *
# Custom CSS for removing top margin or padding
# st.set_page_config(page_title="Traffic Monitoring App", page_config_layout="wide")

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
import requests

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




def main():
    st.title("ระบบตรวจรถติดหน้าบิ๊กซีเพลสสาขาสระบุรี")

    # Replace 'YOUR_TOKEN' with your Line Notify token
    token = '4bC9CyPGMlFdUfSLwTFL47TG1bccAEz3bSdh4hJ6upp'

    
    A1,A2,A3,A4,B1,B2,B3,B4 = show_sidebar()
    output = GET_TFL(A1, A2, A3, A4, B1, B2, B3, B4)
    st.write(f"ถนนฝั่งรร.อนุบาลสระบุรี: {output[0]}, ถนนสายรร.สระบุรีวิทยาคม: {output[1]}, สถานะ: {output[2]}")
    
    # Prepare the states to pass to the map
    A_states = {"A1": A1, "A2": A2, "A3": A3, "A4": A4}
    B_states = {"B1": B1, "B2": B2, "B3": B3, "B4": B4}

    # Create the map with updated icon states
    my_map = create_map(A_states, B_states, output)


    TEMP_STATE = "NORMAL"

    if (output[2]=="ALERT"):
        # status = send_line_notify_with_image(token, "มึงอะตัวปลอม กุอะตัวจริง","./asset/image.png")
        current_time = datetime.datetime.now()
        if (output[1]=="GREEN"):
            road = "โรงเรียนสระบุรีวิทยาคม"
        else:
            road = "โรงเรียนอนุบาลสระบุรี"
        TEMP_STATE = "ALERT"
        #send_line_notify(token, f'เตือน!!! ณ เวลา {current_time.strftime("%d/%m/%Y %H:%M น.")} \n ถนนฝั่ง {road} ตรวจพบการจราจรติดขัด')
        st.warning(f'เตือน!!! ณ เวลา {current_time.strftime("%d/%m/%Y %H:%M น.")} \n ถนนฝั่ง {road} ตรวจพบการจราจรติดขัด')
    elif (output[2]=="NORMAL") and (TEMP_STATE=="ALERT"):
        current_time = datetime.datetime.now()

        st.warning(f'ณ เวลา {current_time.strftime("%d/%m/%Y %H:%M น.")} การจราจรกลับมาเป็นปกติ')
        TEMP_STATE = "NORMAL"
    print("TEMP_STATE:",TEMP_STATE)


    # Display the map using an HTML iframe
    with open("map.html", "r") as f:
        map_html = f.read()
    map_html = f"""
    <div style="width: 100vw; height: 800px;">
        {map_html}
    </div>
    """

    st.components.v1.html(map_html,height=700)



if __name__ == "__main__":
    main()
