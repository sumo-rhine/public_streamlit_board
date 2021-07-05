import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import contextily as ctx
import geopandas as gp
from shapely import wkt
import plotly

BASEPATH = os.path.abspath(os.path.dirname(__file__))

st.set_page_config(layout="wide")

def load_df():
    df = pd.read_csv(BASEPATH+'/results.csv')
    df.index = df['Municipality']
    return df

df = load_df()

df['pop_dens'] = df['Population'] / df['area_km2']

subind = list(df.columns)
for i in ['id', 'geom', 'Admin ID', 'Country', 'Population', 'pop_dens', 'area_km2', 'urban_share', 'Municipality', 'Survey on urban transport policy']:
    subind.remove(i)


st.write('''
# Sustainable Mobility in the Upper Rhine Region 
## ** Data Board of Indicator System **
### This board is designed to inspect, compare, validate the latest results of the indicator system to make (sustainable) mobility measureable from remote data. The results are limited to 35 municipalities in the study area of the Upper Rhine region.
''')

st.sidebar.markdown('## Please select view')
mode = st.sidebar.selectbox('different data visualization can be selected', ['None', 'compare cities', 'compare indicators'], help='compare cities or indicators')

if mode == 'compare indicators':
    st.sidebar.markdown('## Please select subindicators')
    selection = st.sidebar.multiselect('select up to 5 subindicators', tuple(subind), default=None, help='selected subindicators will be displayed on screen. Selecting more than 5 subindicators will result in plotting error')

    st.sidebar.markdown('## Sort by ...')
    sorter = st.sidebar.selectbox('to sort by one of the selected subindicators, please select:', selection)

    cols = plotly.colors.DEFAULT_PLOTLY_COLORS

    fig = make_subplots(rows=2, cols=5, 
                        shared_yaxes=True, 
                        row_heights = [0.8, 0.2], 
                        vertical_spacing=0.02, 
                        subplot_titles=selection)
    fig.update_layout(height=1000, showlegend=False)
    for i, sel in enumerate(selection):
        fig.add_trace(go.Bar(x=df.sort_values(sorter)[sel].values, 
                            y=df.sort_values(sorter)[sel].index, 
                            orientation='h', 
                            name=sel), row=1, col=i+1)
        fig.update_traces(row=1, col=i+1, marker_color=cols[i+4])
        #df.sort_values(sorter)[sel].plot.barh(ax=ax[i], title=sel)

    # st.plotly_chart(fig)

    #fig = make_subplots(rows=2, cols=3)
    for i, sel in enumerate(selection):
        fig.add_trace(go.Histogram(x=df[sel], name=sel), row=2, col=i+1)
        fig.update_traces(row=2, col=i+1, marker_color=cols[i+4])
    # Overlay both histograms
    # fig.update_layout(barmode='overlay')
    # Reduce opacity to see both histograms
    # fig.update_traces(opacity=0.75)

    st.plotly_chart(fig, use_container_width=True)

    info_columns = ['Population', 'pop_dens', 'area_km2', 'urban_share']
    overview_fig = make_subplots(rows=2, cols=4, 
                                shared_yaxes=True, 
                                row_heights = [0.8, 0.2], 
                                vertical_spacing=0.02, 
                                subplot_titles=info_columns)
    overview_fig.update_layout(height=1000, showlegend=False)

    for i, sel in enumerate(info_columns):
        overview_fig.add_trace(go.Bar(x=df.sort_values(sorter)[sel].values, 
                                    y=df.sort_values(sorter)[sel].index, 
                                    orientation='h', name=sel), row=1, col=i+1)
        overview_fig.update_traces(row=1, col=i+1, marker_color=cols[i])
        overview_fig.add_trace(go.Histogram(x=df[sel], name=sel), row=2, col=i+1)
        overview_fig.update_traces(row=2, col=i+1, marker_color=cols[i])

    st.plotly_chart(overview_fig, use_container_width=True)


    if st.checkbox('View dataframe'):
        st.dataframe(df)

    if st.checkbox('View selection'):
        st.dataframe(df[selection])

if mode == 'compare cities':
    st.sidebar.markdown('## Please select cities')
    city_sel = st.sidebar.multiselect('upt ot 5 cities can be selected', df['Municipality'], help='more than 5 selected cities will result in plotting error')

    citydata = df.copy()
    
    for col in subind:
        citydata[col] = citydata[col]/citydata[col].max()

    city_fig = make_subplots(rows=1, cols=5, shared_yaxes=True, subplot_titles=city_sel)
    city_fig.update_layout(height=800, showlegend=False)

    for i, city in enumerate(city_sel):
        city_fig.add_trace(go.Bar(x=citydata[subind].loc[city], 
                                  y=citydata[subind].columns, 
                                  orientation='h'), row=1, col=i+1)

    st.plotly_chart(city_fig, use_container_width=True)


# # map

# #df['geom'] = df['geom'].apply(wkt.loads)
# df_trans = df.copy()
# df_trans['geom'] = df_trans['geom'].apply(wkt.loads)
# df_trans = gp.GeoDataFrame(df_trans, geometry='geom')
# df_trans = df_trans.set_crs('EPSG:3035')

# df_trans = df_trans.to_crs('epsg:3857')

# fig, ax = plt.subplots()
# df_trans.plot(column='ndvi', legend=True, ax=ax)#, vmax=50) #, alpha=0.7)
# ctx.add_basemap(ax)
# st.pyplot(fig)

# #go.Choroplethmapbox(
# # choro = px.choropleth(df_trans, geojson=df_trans['geom'], locations=df_trans.index, color='ndvi')
# # choro.update_geos(fitbounds='locations', visible=False)
# # st.plotly_chart(choro)

st.write('''
# TO DOs
- histograms
- nicer horizontal bar chart
- map
''')

# if st.button('sort plot 1'):
#     fig, ax = plt.subplots(1,3, sharey=True, figsize=(10,10))
#     df[selection[0]].sorted().plot.barh(ax=ax[0])