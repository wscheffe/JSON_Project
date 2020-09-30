import json

in_file = open('US_fires_9_1.json', 'r') 
open_data = json.load(in_file)

brights,lons,lats = [],[],[]

for fires in open_data:
    if fires['brightness'] > 450:
        bright = fires['brightness']
        brights.append(bright)
        lon = fires['longitude']
        lat = fires['latitude']
        lons.append(lon)
        lats.append(lat)


import plotly
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


fire_data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'color': brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'},
    },
}]


graph_layout = Layout(
    title='US Fires - 9/1/2020 through 9/13/2020',
    geo = dict(
        projection_scale=5.8,
        center=dict(lat=36.7783, lon=-115.4179)
        ),
    )
fig = {'data':fire_data, 'layout':graph_layout}

offline.plot(fig, filename='fires_9_1.html')
