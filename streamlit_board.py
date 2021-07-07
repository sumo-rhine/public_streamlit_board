import streamlit as st
import pandas as pd
import os
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
#import plotly.express as px
from plotly.subplots import make_subplots
#import contextily as ctx
#import geopandas as gp
#from shapely import wkt
import plotly
import numpy as np

BASEPATH = os.path.abspath(os.path.dirname(__file__))

long_names = {#'area_km2': 'area [km2]',
            'Municipality': 'Municipality',
            'Country': 'Country',
            'Population': 'Population',
            'noise_rail_night': 'Rail Noise Exposure Night >55dB [%]',
            'noise_rail_day': 'Rail Noise Exposure Day >55dB [%]',
            'noise_road_day': 'Road Noise Exposure Day >55dB [%]',
            'noise_road_night': 'Road Noise Exposure Night >55dB [%]',
            '30kmh_speed_limit': 'Speed Limit <= 30 kmh [%]',
            'pedest_street_dens': 'streets accessible by pedestrians [%]',
            'low_traffic_vol': 'Streets with low traffic volumn [%]',
            'green_area': 'green area with NDVI >0.7 [%]',
            'park_area': 'urban park area [%]',
            'walk_stim_fac': 'facilities stimulating walking [no/km2]',
            'heavy_vehicles': 'streets accessible for heavy vehicles [%]',
            'serv_freq': 'mean trips per day and station [trips/day]',
            'serv_dur': 'mean time of service availabilty [% of day]',
            'stop_dens': 'Stop density [stops/km2]',
            'coverage': 'population in 5 min walking distance to public transport [%]',
            'fuel_stat': 'fuel stations per 1000 inhabitant',
            'carfree_streets': '[%] of car free streets',
            'onewaystr': '[%] of one way streets',
            'pop_near_park': 'population within walking distance to parks [%]',
            'n_bikesharing_bikes': 'bike sharing stations / 1000 inhabitants',
            'n_carsharing_cars': 'car sharing stations / 1000 inhabitants',
            'n_parking_places': 'Parking Places',
            'parking_price': 'parking price [Euro]',
            'pt_stations_mobility_impaired': 'handicap-accessible stations',
            'pt_stations_mobility_impaired_uncertainty': 'handicap-accessible stations uncertainty',
            'pollu_regul': 'Pollution regulation',
            'car_acc_d': 'deadly car accidents [%]',
            'car_acc': 'car accidents [No/1000 inhab.]',
            'bike_acc_d': 'deadly bike accidents [%]',
            'bike_acc': 'bike accidents [No/1000 inhab.]',
            'pedest_acc_d': 'deadly pedestrian accidents [%]',
            'pedest_acc': 'pedestrian accidents [No/1000 inhab.]'
            }

indicators = {
    'bikeability': ['30kmh_speed_limit', 'low_traffic_vol', 'heavy_vehicles', 'n_bikesharing_bikes'],
    'walkability': ['30kmh_speed_limit', 'pedest_street_dens', 'carfree_streets', 'low_traffic_vol', 'green_area', 'park_area', 'walk_stim_fac', 'pop_near_park'],
    'pollution': ['noise_rail_night', 'noise_rail_day', 'noise_road_day', 'noise_road_night'],
    'public transport': ['serv_freq', 'serv_dur', 'stop_dens', 'coverage', 'pt_stations_mobility_impaired', 'pt_stations_mobility_impaired_uncertainty'],
    'car transport': ['pollu_regul', '30kmh_speed_limit', 'parking_price', 'fuel_stat', 'carfree_streets', 'onewaystr', 'n_carsharing_cars', 'n_parking_places'],
    'traffic_safety': ['car_acc_d', 'car_acc', 'bike_acc_d', 'bike_acc', 'pedest_acc_d', 'pedest_acc']
}

def figure1(rows, cols, indices, df, sorter, colors):
    titles = [long_names[i] if i in long_names.keys() else i for i in indices]
    fig = make_subplots(rows=rows, cols=cols, 
                        shared_yaxes=True, 
                        row_heights = [0.8, 0.2], 
                        vertical_spacing=0.02, 
                        subplot_titles=titles)
    fig.update_layout(height=1000, showlegend=False)

    for i, sel in enumerate(indices):
        fig.add_trace(go.Bar(x=df.sort_values(sorter, na_position='first')[sel].values, 
                                    y=df.sort_values(sorter, na_position='first')[sel].index, 
                                    orientation='h'), row=1, col=i+1)
        fig.update_traces(row=1, col=i+1, marker_color=colors[i])
        fig.add_trace(go.Histogram(x=df[sel]), row=2, col=i+1)
        fig.update_traces(row=2, col=i+1, marker_color=colors[i])    
        
    return fig

st.set_page_config(layout="wide")

df = pd.read_csv(BASEPATH+'/results.csv')
df.index = df['Municipality']
df['pop_dens'] = df['Population'] / df['area_km2']

# df = df.rename(columns=long_names)
    

subind = list(df.columns)
for i in ['id', 'geom', 'Admin ID', 'Country', 'Population', 'pop_dens', 'area_km2', 'urban_share', 'Municipality', 'Survey on urban transport policy', 'park_ensas']:
    subind.remove(i)

info_columns = ['Population', 'pop_dens', 'area_km2', 'urban_share']

cols = plotly.colors.DEFAULT_PLOTLY_COLORS


st.write('''
# Sustainable Mobility in the Upper Rhine Region 
''')

st.sidebar.markdown('## Please select view')
mode = st.sidebar.selectbox('different data visualization can be selected', ['info', 'cities', 'indicators', 'subindicators'], help='compare cities or indicators')

if mode == 'info':
    st.write('''
    ## ** Data Board of Indicator System **
    ### This board is designed to inspect, compare, validate the latest results of the indicator system to make (sustainable) mobility measureable from remote data. The results are limited to 35 municipalities in the study area of the Upper Rhine region.
    
    ## What can you do here?
    - on the left sidebar you have the possibilty to select different views. These views are available:
        - this general information page
        - a page to select from all subindicators and compare them across indicators
        - a page to select all subindicators associated with an indicator
        - a page to compare cites

    ''')

    st.write('''
    # TO DOs
    - histograms
    - nicer horizontal bar chart
    - map
    ''')

if mode == 'indicators':
    st.sidebar.markdown('## Please select one indicator')
    indicator = st.sidebar.selectbox('select one indicator', tuple(indicators.keys()), help='wip')
    selection = [long_names[i] if i in long_names.keys() else i for i in indicators[indicator]]

    st.sidebar.markdown('## Sort by ...')
    sorter = st.sidebar.selectbox('to sort by one of the selected subindicators, please select:', selection+info_columns)
    
    checks = [True] * len(selection)
    for i, subind in enumerate(selection):
        if st.sidebar.checkbox(subind, value=True):
            checks[i] = True
        else:
            checks[i] = False

    selection = list(np.array(selection)[checks])
    
    selection = [{v: k for k, v in long_names.items()}[i] for i in selection]
    sorter = {v: k for k, v in long_names.items()}[sorter]
    
    if selection != None:
        fig1 = figure1(2,len(selection),selection, df, sorter, cols)
        st.plotly_chart(fig1, use_container_width=True)

    if sorter == None:
        sorter = 'Population'
    fig2 = figure1(2,5,info_columns, df, sorter, cols[4:])
    st.plotly_chart(fig2, use_container_width=True)

    if st.checkbox('View dataframe'):
        st.dataframe(df)

    if st.checkbox('View selection'):
        st.dataframe(df[selection])

if mode == 'subindicators':
    st.sidebar.markdown('## Please select subindicators')
    selectables = [long_names[i] if i in long_names.keys() else i for i in subind]
    selection = st.sidebar.multiselect('select up to 5 subindicators', tuple(selectables), default=None, help='selected subindicators will be displayed on screen. Selecting more than 5 subindicators will result in plotting error')

    st.sidebar.markdown('## Sort by ...')
    sorter = st.sidebar.selectbox('to sort by one of the selected subindicators, please select:', selection+info_columns)

    selection = [{v: k for k, v in long_names.items()}[i] for i in selection]
    sorter = {v: k for k, v in long_names.items()}[sorter]

    if selection != None:
        fig1 = figure1(2,5,selection, df, sorter, cols)
        st.plotly_chart(fig1, use_container_width=True)

    if sorter == None:
        sorter = 'Population'
    fig2 = figure1(2,5,info_columns, df, sorter, cols[4:])
    st.plotly_chart(fig2, use_container_width=True)

    if st.checkbox('View dataframe'):
        st.dataframe(df)

    if st.checkbox('View selection'):
        st.dataframe(df[selection])

if mode == 'cities':
    st.sidebar.markdown('## Please select cities')
    city_sel = st.sidebar.multiselect('up to 5 cities can be selected', df['Municipality'], help='more than 5 selected cities will result in plotting error')

    citydata = df.copy()
    st.write(city_sel)
    for col in subind:
        citydata[col] = citydata[col]/citydata[col].max()

    citydata.columns = [long_names[i] if i in long_names.keys() else i for i in citydata.columns]
    subind = [long_names[i] if i in long_names.keys() else i for i in subind]
    
    if city_sel != None:
        city_fig = make_subplots(rows=1, cols=5, shared_yaxes=True, subplot_titles=city_sel)
        city_fig.update_layout(height=800, showlegend=False)

        for i, city in enumerate(city_sel):
            city_fig.add_trace(go.Bar(x=citydata[subind].loc[city], 
                                    y=citydata[subind].columns, 
                                    orientation='h'), row=1, col=i+1)

        st.plotly_chart(city_fig, use_container_width=True)






# if st.button('sort plot 1'):
#     fig, ax = plt.subplots(1,3, sharey=True, figsize=(10,10))
#     df[selection[0]].sorted().plot.barh(ax=ax[0])


    # fig = make_subplots(rows=2, cols=5, 
    #                     shared_yaxes=True, 
    #                     row_heights = [0.8, 0.2], 
    #                     vertical_spacing=0.02, 
    #                     subplot_titles=selection)
    # fig.update_layout(height=1000, showlegend=False)
    # for i, sel in enumerate(selection):
    #     fig.add_trace(go.Bar(x=df.sort_values(sorter, na_position='first')[sel].values, 
    #                         y=df.sort_values(sorter, na_position='first')[sel].index, 
    #                         orientation='h', 
    #                         name=sel), row=1, col=i+1)
    #     fig.update_traces(row=1, col=i+1, marker_color=cols[i+4])
    #     #df.sort_values(sorter)[sel].plot.barh(ax=ax[i], title=sel)

    # # st.plotly_chart(fig)

    # #fig = make_subplots(rows=2, cols=3)
    # for i, sel in enumerate(selection):
    #     fig.add_trace(go.Histogram(x=df[sel], name=sel), row=2, col=i+1)
    #     fig.update_traces(row=2, col=i+1, marker_color=cols[i+4])
    # # Overlay both histograms
    # # fig.update_layout(barmode='overlay')
    # # Reduce opacity to see both histograms
    # # fig.update_traces(opacity=0.75)

    # st.plotly_chart(fig, use_container_width=True)

    # overview_fig = make_subplots(rows=2, cols=4, 
    #                             shared_yaxes=True, 
    #                             row_heights = [0.8, 0.2], 
    #                             vertical_spacing=0.02, 
    #                             subplot_titles=info_columns)
    # overview_fig.update_layout(height=1000, showlegend=False)

    # for i, sel in enumerate(info_columns):
    #     overview_fig.add_trace(go.Bar(x=df.sort_values(sorter, na_position='first')[sel].values, 
    #                                 y=df.sort_values(sorter, na_position='first')[sel].index, 
    #                                 orientation='h', name=sel), row=1, col=i+1)
    #     overview_fig.update_traces(row=1, col=i+1, marker_color=cols[i])
    #     overview_fig.add_trace(go.Histogram(x=df[sel], name=sel), row=2, col=i+1)
    #     overview_fig.update_traces(row=2, col=i+1, marker_color=cols[i])

    # st.plotly_chart(overview_fig, use_container_width=True)

