import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

class Histogram:
    
    @staticmethod
    def plot():
        
        df = pd.read_csv('./data/arrhythmia.csv')

        data = [
            go.Histogram(
                x=df[df['Sex']==0]['Height'],
                opacity=0.75,
                name='Male'
            ),
            go.Histogram(
                x=df[df['Sex']==1]['Height'],
                opacity=0.75,
                name='Female'
            )
        ]

        layout = go.Layout(
            barmode='overlay',
            title="Height comparison by gender"
        )
        fig = go.Figure(data=data, layout=layout)
        pyo.plot(fig)
        
    @staticmethod
    def _plot():
        
        df = pd.read_csv('./data/mpg.csv')

        data = [
            go.Histogram(
                x=df['mpg'],
                xbins=dict(start=8,end=50,size=1),
            )
        ]

        layout = go.Layout(
            title="Miles per Gallon Frequencies of<br>\
            1970's Era Vehicles"
        )
        fig = go.Figure(data=data, layout=layout)
        pyo.plot(fig, filename='narrow_histogram.html')
        