import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import contextily as ctx
import geopandas as gp


BASEPATH = os.path.abspath(os.path.dirname(__file__))

st.set_page_config(layout="wide")

@st.cache
def load_df():
    df = pd.read_csv(BASEPATH+'/subindicator_results.csv')
    df.index = df['Municipality']
    return df

df = load_df()



st.write('''
# SuMo Board
## to explore the results ...
''')

if st.checkbox('View dataframe'):
    st.dataframe(df)

subind = list(df.columns)
for i in ['Unnamed: 0', 'geom', 'Admin ID', 'Country']:
    subind.remove(i)
st.markdown('## What subindicators to compare?')
selection = st.multiselect('What subindicators to compare?', tuple(subind), default='area_km2', help='only the first three selections can be displayed!')

if st.checkbox('View selection'):
    st.dataframe(df[selection])

sorter = st.selectbox('sort by:', selection)


fig = make_subplots(rows=1, cols=3, shared_yaxes=True)
#fig, ax = plt.subplots(1,3, sharey=True, figsize=(10,10))

for i, sel in enumerate(selection[:3]):
    fig.add_trace(go.Bar(x=df.sort_values(sorter)[sel].values, y=df.sort_values(sorter)[sel].index, orientation='h'), row=1, col=i+1)
    #df.sort_values(sorter)[sel].plot.barh(ax=ax[i], title=sel)

st.plotly_chart(fig)
#st.pyplot(fig)


#import plotly.figure_factory as ff
#fig = ff.create_distplot(df[selection], group_labels=df[selection].columns)
#st.plotly_chart(fig)




#fig = go.Figure()
#for i in selection[:2]:
#    fig.add_trace(go.Histogram(x=df[i]))

fig = make_subplots(rows=1, cols=3)
for i, sel in enumerate(selection):
    fig.add_trace(go.Histogram(x=df[sel], name=sel), row=1, col=i+1)

# Overlay both histograms
fig.update_layout(barmode='overlay')
# Reduce opacity to see both histograms
fig.update_traces(opacity=0.75)
st.plotly_chart(fig)



#df_trans = gp.GeoDataFrame(df, geometry='geom').to_crs(epsg=3857)
#ax = df_trans.plot(column='ndvi', figsize=(20,20), legend=True)#, vmax=50) #, alpha=0.7)
#ctx.add_basemap(ax)


st.write('''
# TO DOs
- histograms
- nicer horizontal bar chart
- map
''')

# if st.button('sort plot 1'):
#     fig, ax = plt.subplots(1,3, sharey=True, figsize=(10,10))
#     df[selection[0]].sorted().plot.barh(ax=ax[0])