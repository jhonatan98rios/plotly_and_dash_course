import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff

class Distplots:
    
    @staticmethod
    def plot():
        
        snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
        twain = [.225,.262,.217,.240,.230,.229,.235,.217]

        hist_data = [snodgrass,twain]
        group_labels = ['Snodgrass','Twain']

        fig = ff.create_distplot(hist_data, group_labels, bin_size=[.005,.005]) # type: ignore
        pyo.plot(fig)
        