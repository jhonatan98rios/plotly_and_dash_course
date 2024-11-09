import random
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

class BarChartExercise:
    
    @staticmethod
    def plot():
        
        df = pd.read_csv('./data/mocksurvey.csv', index_col=0)
        print(df.head(10))
        
        # data = [
        #     go.Bar(x=QUESTIONS, y=df['Strongly Agree'], name='Strongly Agree', 
        #     go.Bar(x=QUESTIONS, y=df['Somewhat Agree'], name='Somewhat Agree', 
        #     go.Bar(x=QUESTIONS, y=df['Neutral'], name='Neutral'),
        #     go.Bar(x=QUESTIONS, y=df['Somewhat Disagree'], name='Somewhat Disagree'),
        #     go.Bar(x=QUESTIONS, y=df['Strongly Disagree'], name='Strongly Disagree'),
        # ]
        
        #data = [ go.Bar(x=df.index, y=df[column], name=column) for column in df.columns ]
        data = [ go.Bar(x=df[column], y=df.index, name=column, orientation='h') for column in df.columns ]
        
        
        layout = go.Layout(title='Mock Survey Results', barmode='stack', ) # 'stack', 'group', 'overlay', 'relative'
        fig = go.Figure(data=data, layout=layout)       
        
        pyo.plot(fig)
