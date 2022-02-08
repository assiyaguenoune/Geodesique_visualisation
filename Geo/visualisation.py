from re import template
from turtle import bgcolor, color, width
from matplotlib import colors
from numpy import *
from math import radians
import plotly.graph_objs as go
from plotly.offline import plot

def geodetic_to_geocentric(ellipsoid, latitude, longitude, height):

    φ = latitude
    λ = longitude
    sin_φ = sin(φ)
    a, rf = ellipsoid           
    e2 = 1 - (1 - 1 / rf) ** 2 
    n = a / sqrt(1 - e2 * sin_φ ** 2)
    r = (n + height) * cos(φ) 
    x = r * cos(λ)
    y = r * sin(λ)
    z = (n * (1 - e2) + height) * sin_φ
    return x, y, z

def plot3d(a, b, arr):
    phi = linspace(0, 2*pi,100)
    theta = linspace(0, pi,100)
    phi, theta=meshgrid(phi, theta)


    fig = go.Figure(go.Surface(
    x = cos(phi)*cos(theta)*7,
    y = cos(phi)*sin(theta)*7,
    z = 5 *sin(phi)))


    layout = go.Layout(
        title='Visualisation de la géodésique',
        title_font_family="Courier New",
        title_font_size=36,
        autosize=True,
        width=1520,
        height=680,
        template='plotly_dark',
        paper_bgcolor="#000000",
        title_font_color="#b2ffff"
           
    )
    fig = go.Figure(go.Surface(
    x = cos(phi)*cos(theta)*a,
    y = cos(phi)*sin(theta)*a,
    z = b *sin(phi),colorscale='Blues'), layout=layout,
    )

    spheroid = a,a/(a-b)
    for i in range(400):
        arr[i].x, arr[i].y, arr[i].z = geodetic_to_geocentric(spheroid, arr[i].Lat, arr[i].Long, 0)

    fig.add_scatter3d(
    x=[arr[i].x for i in range(400)],
    y=[arr[i].y for i in range(400)],
    z=[arr[i].z for i in range(400)],
    mode="lines",
    line=dict(
        color="aqua",
        dash='solid',
        width=10
    )
)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div
  