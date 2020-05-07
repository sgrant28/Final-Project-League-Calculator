import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/LCS2019SummerChamps.csv')

# Preparing data
data = [go.Bar(x=df['Champion'], y=df['Games Played'])]


# Preparing layout
layout = go.Layout(title='League of Legends champions used in the 2019 Summer LCS', xaxis_title="Champions",
                   yaxis_title="Games Played")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Leaguebarchart.html')
