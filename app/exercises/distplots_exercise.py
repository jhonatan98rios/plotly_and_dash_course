import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd

class DistplotsExercise:
    
    @staticmethod
    def plot():
        
        # create a DataFrame from the .csv file:
        df = pd.read_csv('./data/iris.csv')

        # Define the traces
        trace0 = df[df['class']=='Iris-setosa']['petal_length']
        trace1 = df[df['class']=='Iris-versicolor']['petal_length']
        trace2 = df[df['class']=='Iris-virginica']['petal_length']

        # Define a data variable
        hist_data = [trace0, trace1, trace2]
        group_labels = ['Iris Setosa','Iris Versicolor','Iris Virginica']

        # Create a fig from data and layout, and plot the fig
        fig = ff.create_distplot(hist_data, group_labels)
        pyo.plot(fig)
        