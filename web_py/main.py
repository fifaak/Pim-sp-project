# main.py
import streamlit as st
import folium
from streamlit.components.v1 import html
import matplotlib.pyplot as plt
from Map import create_map

# Custom CSS for checkboxes with icons
st.markdown("""
    <style>
    .custom-checkbox {
        display: flex;
        align-items: center;
    }
    .custom-checkbox input {
        margin-right: 10px;
    }
    .custom-checkbox label {
        display: flex;
        align-items: center;
    }
    .custom-checkbox img {
        margin-right: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

def GET_TFL(A1,A2,A3,A4,B1,B2,B3,B4):
  def iff(condition1, condition2): #<->
      return condition1 == condition2
    
  def chain(condition1,condition2): #->
      if ((condition1==True) and (condition2==False)):
        return False
      else:
        return True
  def reject(condition1):
    if (condition1==True):
      return False
    else:
      return True
  count_A=sum([A1,A2,A3,A4])
  count_B=sum([B1,B2,B3,B4])
  if ((count_A==0) and (count_B==1)):

    AB = chain(((reject(A1) or B1) and (reject(A2) and reject(A3) and reject(A4))),(reject(B2) and reject(B3) and reject(B4)))
    if (((iff(AB,A1)==False) and (iff(AB,B1)==True)) and (AB==True)):
      return "RED","GREEN","NORMAL"
  
  elif ((count_A==1) and (count_B==0)):
    AB = chain(((reject(A1) or B1) and (reject(A2) and reject(A3) and reject(A4))),(reject(B2) and reject(B3) and reject(B4)))
    if (((iff(AB,A1)==True) and (iff(AB,B1)==False)) and (AB==True)):
      return "GREEN","RED","NORMAL"
  
  elif ((count_A==0) and (count_B==2)):
    AB = iff(((reject(A1)or B1) and (reject(A2) or B2) and (reject(A3) and reject(A4))),(reject(B3) and reject(B4)))
    if (((iff(AB,(A1 and A2))==False) and (iff(AB,(B1 and B2))==True)) and (AB==True)):
      return "RED","GREEN","NORMAL"
  
  elif ((count_A==2) and (count_B==0)):
    AB = iff(((A1 or reject(B1)) and (A2 or reject(B2)) and (reject(A3) and reject(A4))),(reject(B3) and reject(B4)))
    if (((iff(AB,(A1 and A2))==True) and (iff(AB,(B1 and B2))==False)) and (AB==True)):
      return "GREEN","RED","NORMAL"
  
  elif ((count_A==0) and (count_B==3)):
    AB = ((reject(A1) or B1) and (reject(A2) or B2) and (reject(A3) and B3) and (iff(reject(A4),reject(B4))))
    if (chain(AB,(A1 and A2 and A3))==False) and (chain(AB,(B1 and B2 and B3))==True) and (AB==True):
      return "RED","GREEN","ALERT"

  elif ((count_A==3) and (count_B==0)):
    AB = ((A1 or reject(B1)) and (A2 or reject(B2)) and (A3 and reject(B3)) and (iff(reject(A4),reject(B4))))
    if (chain(AB,(A1 and A2 and A3))==True) and (chain(AB,(B1 and B2 and B3))==False) and (AB==True):
      return "GREEN","RED","ALERT"

  elif ((count_A==0) and (count_B==4)):
    AB = ((reject(A1) or B1) and (reject(A2) or B2) and (reject(A3) or B3) and (reject(A4) or B4))
    if ((chain(AB,(A1 and A2 and A3 and A4))==False) and (chain(AB,(B1 and B2 and B3 and B4))==True)) and (AB==True):
      return "RED","GREEN","ALERT"

  elif ((count_A==4) and (count_B==0)):
    AB = ((A1 or reject(B1)) and (A2 or reject(B2)) and (A3 or reject(B3)) and (A4 or reject(B4)))
    if ((chain(AB,(A1 and A2 and A3 and A4))==True) and (chain(AB,(B1 and B2 and B3 and B4))==False)) and (AB==True):
      return "GREEN","RED","ALERT"

  elif ((count_A == 1) and (count_B==2)):
    AB = iff(((A1 or B1) and (reject(A2) or B2) and (reject(A3) and reject(A4))),(reject(A4) and reject(B4)))
    if ((chain(AB,(A1 and A2))==False) and (chain(AB,(B1 and B2))==True)) and (AB==True):
      return "RED","GREEN","NORMAL"
  
  elif ((count_A == 2) and (count_B==1)):
    AB = iff(((A1 or B1) and (A2 or reject(B2)) and (reject(A3) and reject(A4))),(reject(B3) and reject(B4)))
    if ((chain(AB,(A1 and A2))==True) and (chain(AB,(B1 and B2))==False)) and (AB==True):
      return "GREEN","RED","NORMAL"

  elif ((count_A==1) and (count_B==3)):
    AB = ((A1 or B1) and (reject(A2) or B2) and (reject(A3) and B3) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==False) and (chain(AB,(B1 and B2 and B3))==True)) and (AB==True):
      return "RED","GREEN","ALERT"
  
  elif ((count_A==3) and (count_B==1)):
    AB = ((A1 or B1) and (A2 or reject(B2)) and (A3 and reject(B3)) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==True) and (chain(AB,B1)==False)) and (AB==True):
      return "GREEN","RED","ALERT"

  elif ((count_A==1) and (count_B==4)):
    AB = ((A1 or B1) and (reject(A2) or B2) and (reject(A3) and B3) and ((reject(A4) or B4)))
    if (chain(AB,(A1 and A2 and A3 and A4)) == False) and (chain(AB,(B1 and B2 and B3 and B4)) == True)  and (AB==True):
      return "RED","GREEN","ALERT"

  elif ((count_A==4) and (count_B==1)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and reject(B3)) and ((A4 or reject(B4))))
    if (chain(AB,(A1 and A2 and A3 and A4)) == True) and (chain(AB,(B1 and B2 and B3 and B4)) == False)  and (AB==True):
      return "GREEN","RED","ALERT"

  elif ((count_A==2) and (count_B==3)):
    AB = ((A1 or B1) and (A2 or B2) and (reject(A3) and B3) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==False) and (chain(AB,(B1 and B2 and B3))==True))  and (AB==True):
      return "RED","GREEN","ALERT"

  elif ((count_A==3) and (count_B==2)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and reject(B3)) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==True) and (chain(AB,(B1 and B2 and B3))==False))  and (AB==True):
      return "GREEN","RED","ALERT"

  elif ((count_A==2) and (count_B==4)):
    AB = ((A1 or B1) and (A2 or B2) and (reject(A3) or (B3)) and ((reject(A4) or B4)))
    if (chain(AB,(A1 and A2 and A3 and A4))==False) and (chain(AB,(B1 and B2 and B3 and B4))==True) and (AB==True):
      return "RED","GREEN","ALERT"

  elif ((count_A==4) and (count_B==2)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and reject(B3)) and ((A4 or reject(B4))))
    if (chain(AB,(A1 and A2 and A3 and A4))==True) and (chain(AB,(B1 and B2 and B3 and B4))==False) and (AB==True):
      return "GREEN","RED","ALERT"

  elif ((count_A==3) and (count_B==4)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and B3) and ((reject(A4) or B4)))
    if (chain(AB,(A1 and A2 and A3 and A4))==False) and (chain(AB,(B1 and B2 and B3 and B4))==True) and (AB==True):
      return "RED","GREEN","ALERT"
  
  elif ((count_A==4) and (count_B==3)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 and B3) and ((A4 or reject(B4))))
    if (chain(AB,(A1 and A2 and A3 and A4))==True) and (chain(AB,(B1 and B2 and B3 and B4))==False) and (AB==True):
      return "GREEN","RED","ALERT"

  elif ((count_A==1) and (count_B==1)):
    AB = iff(((A1 or B1) and (reject(A2) and reject(A3) and reject(A4))),(reject(B2) and reject(B3) and reject(B4)))
    if ((chain(AB,A1)==True) and (chain(AB,reject(B1))==False)) and (AB==True):
      return "GREEN","RED","NORMAL"

  elif ((count_A==2) and (count_B==2)):
    AB = iff(((A1 or B1) and (A2 or B2) and (reject(A3) and reject(A4))),(reject(B3) and reject(B4)))
    if ((chain(AB,(A1 and A2))==True) and (chain(AB,reject(B1 and B2))==False)) and (AB==True):
      return "GREEN","RED","NORMAL"

  elif ((count_A==3) and (count_B==3)):
    AB = ((A1 or B1) and (A2 or B2) and  (A3 or B3) and (iff(reject(A4),reject(B4))))
    if ((chain(AB,(A1 and A2 and A3))==True) and (chain(AB,reject(B1 and B2 and B3))==False)) and (AB==True):
      return "GREEN","RED","NORMAL"

  elif ((count_A == 4) and (count_B == 4)):
    AB = ((A1 or B1) and (A2 or B2) and (A3 or B3) and (A4 or B4))
    if (chain(AB,(A1 and A2 and A3 and A4))==True) and (chain(AB,reject(B1 and B2 and B3 and B4))== False) and (AB==True):
      return "GREEN","RED","NORMAL"

  return "BLACK","BLACK","NORMAL"
def main():
    st.title("ระบบตรวจรถติดหน้าโรงเรียนของเรา")

    st.sidebar.header("VEHICLE DETECTION SENSOR")

    A1 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด A1", value=False)
    A2 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด A2", value=False)
    A3 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด A3", value=False)
    A4 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด A4", value=False)
    B1 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด B1", value=False)
    B2 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด B2", value=False)
    B3 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด B3", value=False)
    B4 = st.sidebar.checkbox("ตรวจพบรถบริเวณจุด B4", value=False)

    output = GET_TFL(A1, A2, A3, A4, B1, B2, B3, B4)
    st.write(f"Traffic Light A: {output[0]}, Traffic Light B: {output[1]}, Status: {output[2]}")



    # Prepare the states to pass to the map
    A_states = {"A1": A1, "A2": A2, "A3": A3, "A4": A4}
    B_states = {"B1": B1, "B2": B2, "B3": B3, "B4": B4}

    # Create the map with updated icon states
    my_map = create_map(A_states, B_states,output)

    # Display the map using an HTML iframe
    with open("map.html", "r") as f:
        map_html = f.read()

    # Embed the HTML in the Streamlit app
    st.components.v1.html(map_html, width=500, height=800)
    def show_debug_algo():
      fig, ax = plt.subplots(figsize=(15, 7))

      ax.plot([0.5, 0.8], [0.4, 0.4], color='black', linewidth=5)
      ax.plot([0.2, 0.5], [0.6, 0.6], color='black', linewidth=5)

      if output[0] == "GREEN":
          ax.plot(0.5, 0.6, 'go', markersize=20)  
      elif output[0] == "RED":
          ax.plot(0.5, 0.6, 'ro', markersize=20)  

      if output[1] == "GREEN":
          ax.plot(0.5, 0.4, 'go', markersize=20)  
      elif output[1] == "RED":
          ax.plot(0.5, 0.4, 'ro', markersize=20)  

      if A1:
          ax.plot(0.45, 0.6, 'ks', markersize=15)  
      if A2:
          ax.plot(0.4, 0.6, 'ks', markersize=15)  
      if A3:
          ax.plot(0.35, 0.6, 'ks', markersize=15)  
      if A4:
          ax.plot(0.3, 0.6, 'ks', markersize=15)  

      if B1:
          ax.plot(0.55, 0.4, 'ks', markersize=15)  
      if B2:
          ax.plot(0.6, 0.4, 'ks', markersize=15)  
      if B3:
          ax.plot(0.65, 0.4, 'ks', markersize=15)  
      if B4:
          ax.plot(0.7, 0.4, 'ks', markersize=15)  

      ax.axis('off') 
      st.pyplot(fig)

if __name__ == "__main__":
    main()