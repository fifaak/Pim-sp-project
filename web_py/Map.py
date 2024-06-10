import streamlit as st
import folium
from streamlit.components.v1 import html
def init_map():
    def create_map():
        # Create a map centered around a specific location
        m = folium.Map(location=[14.54091974447683, 100.9098524064246], zoom_start=14)

        # Add markers
        markers = {
            "sbwnearest": [14.54091974447683, 100.9098524064246],
            "fromsbwnearest": [14.537275846646647, 100.91070490674878],
            "sbwnear": [14.54091974447683, 100.9098124064246],
            "fromsbwnear": [14.538722548004861, 100.91032770112835],
            "sbw": [14.54090974447683, 100.9097524064246],
            "fromsbw": [14.538712548004861, 100.91025770112835]
        }

        for name, coordinates in markers.items():
            folium.Marker(coordinates, tooltip=name, popup=name).add_to(m)

        # Add different tile layers including the custom Google Satellite layer
        folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)
        folium.TileLayer('Stamen Terrain', name='Terrain').add_to(m)
        folium.TileLayer('Stamen Toner', name='Toner').add_to(m)
        folium.TileLayer('Stamen Watercolor', name='Watercolor').add_to(m)
        folium.TileLayer('CartoDB positron', name='Positron').add_to(m)
        folium.TileLayer('CartoDB dark_matter', name='Dark Matter').add_to(m)
        folium.TileLayer(
            tiles='http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',
            attr='Google',
            name='Google Satellite',
            subdomains=['mt0', 'mt1', 'mt2', 'mt3']
        ).add_to(m)

        # Add layer control to toggle between layers
        folium.LayerControl().add_to(m)

        # Save map as HTML file
        m.save("map.html")

        return m

    # Streamlit app
    st.title("Leaflet Map in Streamlit")

    st.write("This is a Leaflet map embedded in a Streamlit app using Folium.")

    # Create the map
    my_map = create_map()

    # Display the map using an HTML iframe
    with open("map.html", "r") as f:
        map_html = f.read()

    # Embed the HTML in the Streamlit app
    st.components.v1.html(map_html, width=700, height=500)
