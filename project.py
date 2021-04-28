import pandas as pd
import plotly.express as px
df=pd.read_csv("C:/Users/dell/Desktop/Python\DataVisual/Copy+of+data+-+data.csv")
figure=px.scatter(df,x='date',y="cases",color="country")
figure.show()