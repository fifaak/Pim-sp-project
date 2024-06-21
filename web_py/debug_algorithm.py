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