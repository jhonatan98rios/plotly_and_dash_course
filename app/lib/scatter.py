import plotly.offline as pyo
import numpy as np
import plotly.graph_objs as go


class Scatter:
    
    @staticmethod
    def plot():
        np.random.seed(42)

        # Generating random data
        random_x = np.random.randint(1, 101, 100)
        random_y = np.random.randint(1, 101, 100)

        # Structuing data on Plotly scatter graph
        markers_style = dict(size=12, color='rgb(51, 204, 153)', symbol='pentagon', line={'width': 2})
        data = [go.Scatter(x=random_x, y=random_y, mode="markers", marker=markers_style)]

        # Apply the layout atttributes such as title, and subtitles
        layout = go.Layout(title="Hello First Plot", xaxis={'title': 'My X Axis'}, yaxis=dict(title="My Y Axis"), hovermode='closest')

        # Create a image
        fig = go.Figure(data=data, layout=layout)

        # Run plotly on browser
        pyo.plot(fig, filename="scatter.html")