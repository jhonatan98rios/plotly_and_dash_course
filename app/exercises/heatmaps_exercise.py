import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

class HeatmapExercise:
    
    @staticmethod
    def plot():
        
        # Create a DataFrame from  "flights" data
        df = pd.read_csv('./data/flights.csv')

        # Define a data variable
        data = [go.Heatmap(
            x=df['year'],
            y=df['month'],
            z=df['passengers']
        )]

        # Define the layout
        layout = go.Layout(
            title='Flights'
        )
        # Create a fig from data and layout, and plot the fig
        fig = go.Figure(data=data, layout=layout)
        pyo.plot(fig)