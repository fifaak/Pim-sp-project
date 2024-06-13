import streamlit as st
import folium
from streamlit.components.v1 import html
from folium.features import CustomIcon

def init_map():
    def create_map():
        # Create a map centered around a specific location
        m = folium.Map(location=[14.54091974447683, 100.9098524064246], zoom_start=14)

        # Directory where the custom icons are stored
        icon_dir = './icons/'  # Ensure this directory contains your custom icons named according to marker names

        # Add markers with custom icons
        markers = {
            "A1": [14.538665933300948, 100.91024909968965],
            "A2": [14.537500683746611, 100.91053673075561],
            "A3": [14.53613094091651, 100.91083900127504],
            "A4": [14.534412789218553, 100.91122774653071],
            "B1": [14.53892358311632, 100.91029797653401],
            "B2": [14.539535489902878, 100.91015897249041],
            "B3": [14.540601104624443, 100.90990914806737],
            "B4": [14.541851267448662, 100.90963582835234]
        }

        for name, coordinates in markers.items():
            icon_path = f'{icon_dir}{name}.png'  # Generate the path dynamically based on the marker name
            folium.Marker(
                location=coordinates,
                tooltip=name,
                popup=name,
                icon=CustomIcon(icon_path, icon_size=(30, 30))  # Customize the icon size as needed
            ).add_to(m)

        # Add edges for A1 to A4
        a_coords = [markers[f"A{i}"] for i in range(1, 5)]
        folium.PolyLine(a_coords, color="blue", weight=2.5, opacity=1).add_to(m)

        # Add edges for B1 to B4
        b_coords = [markers[f"B{i}"] for i in range(1, 5)]
        folium.PolyLine(b_coords, color="red", weight=2.5, opacity=1).add_to(m)

        # Add different tile layers including the custom Google Satellite layer
        folium.TileLayer(
            tiles='http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',
            attr='Google',
            name='Google Satellite',
            subdomains=['mt0', 'mt1', 'mt2', 'mt3']
        ).add_to(m)
        folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)
        folium.TileLayer('Stamen Terrain', name='Terrain').add_to(m)
        folium.TileLayer('Stamen Toner', name='Toner').add_to(m)
        folium.TileLayer('Stamen Watercolor', name='Watercolor').add_to(m)
        folium.TileLayer('CartoDB positron', name='Positron').add_to(m)
        folium.TileLayer('CartoDB dark_matter', name='Dark Matter').add_to(m)

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

if __name__ == '__main__':
    init_map()
