# Map.py
import folium
from folium.features import CustomIcon

def create_map(A_states, B_states, output):
    # Directory where the custom icons are stored
    icon_dir = './icons/'  # Ensure this directory contains your custom icons named according to marker names

    # Add the Google Satellite tile layer before creating the map
    google_satellite = folium.TileLayer(
        tiles='http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',
        attr='Google',
        name='Google Satellite',
        subdomains=['mt0', 'mt1', 'mt2', 'mt3']
    )

    # Create a map centered around a specific location with no initial tile layer
    m = folium.Map(location=[14.538365933300948, 100.91024909968965], zoom_start=16.5, tiles=None)

    # Add the Google Satellite layer first to make it the default
    google_satellite.add_to(m)

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

        if name in A_states and A_states[name]:
            color = 'green'
        elif name in B_states and B_states[name]:
            color = 'green'
        else:
            color = 'black'  # Default color

        # Assuming the custom icons are images with transparent backgrounds
        folium.Marker(
            location=coordinates,
            tooltip=name,
            popup=name,
            icon=folium.Icon(color=color, icon='info-sign')
        ).add_to(m)

    # Add edges for A1 to A4
    a_coords = [markers[f"A{i}"] for i in range(1, 5)]
    folium.PolyLine(a_coords, color=output[0], weight=7, opacity=1).add_to(m)

    # Add edges for B1 to B4
    b_coords = [markers[f"B{i}"] for i in range(1, 5)]
    folium.PolyLine(b_coords, color=output[1], weight=7, opacity=1).add_to(m)

    # Add different tile layers
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
