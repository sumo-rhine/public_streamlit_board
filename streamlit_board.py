import streamlit as st
import pandas as pd
import os
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
#import contextily as ctx
#import geopandas as gp
#from shapely import wkt
import plotly
import numpy as np
import json
from pathlib import Path
import itertools
import indicator_map as im

BASEPATH = os.path.abspath(os.path.dirname(__file__))

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

test = read_markdown_file(BASEPATH+'/docs/test.md')

with open(BASEPATH+'/names_dict.json', 'r') as file:
    long_names = json.load(file)

indicators = {
    'bikeability': ['30kmh_speed_limit', 'low_traffic_vol', 'heavy_vehicles', 'n_bikesharing_bikes'],
    'walkability': ['30kmh_speed_limit', 'pedest_street_dens', 'carfree_streets', 'low_traffic_vol', 'green_area', 'park_area', 'walk_stim_fac', 'pop_near_park'],
    'pollution': ['noise_rail_night', 'noise_rail_day', 'noise_road_day', 'noise_road_night', 'pm10', 'pm25', 'nox', 'streets_length'],
    'public transport': ['serv_freq', 'serv_dur', 'stop_dens', 'coverage', 'pt_stations_mobility_impaired', 'pt_stations_mobility_impaired_uncertainty', 'pt_price', 'pt_intermodal_connection'],
    'car transport': ['pollu_regul', '30kmh_speed_limit', 'parking_price', 'fuel_stat', 'carfree_streets', 'onewaystr', 'n_carsharing_cars', 'n_parking_places', 'traffic_jam'],
    'traffic safety': ['car_acc_d', 'car_acc', 'bike_acc_d', 'bike_acc', 'pedest_acc_d', 'pedest_acc'],
    'accessibility': ['accessibility_poi_sum_restrnts_iso_bicycle_600sec', 'accessibility_poi_sum_shopping_iso_bicycle_600sec', 'accessibility_poi_sum_business_iso_bicycle_600sec',
                      'accessibility_poi_sum_eduinsts_iso_bicycle_600sec', 'accessibility_poi_sum_restrnts_iso_walk_600sec', 'accessibility_poi_sum_shopping_iso_walk_600sec',
                      'accessibility_poi_sum_business_iso_walk_600sec', 'accessibility_poi_sum_eduinsts_iso_walk_600sec', 'accessibility_poi_sum_restrnts_iso_drive_600sec',
                      'accessibility_poi_sum_shopping_iso_drive_600sec', 'accessibility_poi_sum_business_iso_drive_600sec', 'accessibility_poi_sum_eduinsts_iso_drive_600sec',
                      'accessibility_poi_sum_restrnts_iso_approximated_transit_600sec', 'accessibility_poi_sum_shopping_iso_approximated_transit_600sec', 'accessibility_poi_sum_business_iso_approximated_transit_600sec',
                      'accessibility_poi_sum_eduinsts_iso_approximated_transit_600sec']
}

indicators = {}
for i in im.get_all_ind():
    indicators[i] = im.get_sind_of_ind(i)


def figure1(rows, cols, indices, df, sorter):
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
        fig.update_traces(row=1, col=i+1, marker_color='rgb(49, 173, 230)')
        fig.add_trace(go.Histogram(x=df[sel]), row=2, col=i+1)
        fig.update_traces(row=2, col=i+1, marker_color='rgb(49, 173, 230)')    
        
    return fig

st.set_page_config(layout="wide")

df = pd.read_csv(BASEPATH+'/results.csv')
df.index = df['Municipality']
df['pop_dens'] = df['Population'] / df['area_km2']

df_ind = pd.read_csv(BASEPATH+'/ind_results.csv')
df_ind.index = df_ind['Municipality']
df_ind_pure = df_ind[list(df_ind.columns[8:])]
# df = df.rename(columns=long_names)
    

subind = list(df.columns)
for i in ['id', 'geom', 'Admin ID', 'Country', 'Population', 'pop_dens', 'area_km2', 'urban_share', 'Municipality', 'Survey on urban transport policy', 'park_ensas']:
    subind.remove(i)

# info_columns = ['Population', 'pop_dens', 'area_km2', 'urban_share']
info_columns = ['Population', 'Population density', 'Area', 'Urban Area']

# cols = ['rgb(49, 173, 230)'] #plotly.colors.DEFAULT_PLOTLY_COLORS


# st.write('''
# # Sustainable Mobility in the Upper Rhine Region 
# ''')

# st.markdown(test, unsafe_allow_html=True)

st.sidebar.markdown('## Please select view')
mode = st.sidebar.selectbox('different data visualization can be selected', ['info', 'indicators', 'cities', 'subindicators'], help='compare cities or indicators')

if mode == 'info':

    intro_page = read_markdown_file(BASEPATH+'/docs/intro_page.md')
    st.write(intro_page)

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    sorter = st.radio('', options=info_columns)
    sorter = {v: k for k, v in long_names.items()}[sorter]
    selection = [{v: k for k, v in long_names.items()}[i] for i in info_columns]
    fig2 = figure1(2,5,selection, df, sorter)
    st.plotly_chart(fig2, use_container_width=True)

    # st.write('''
    # # TO DOs
    # - histograms
    # - nicer horizontal bar chart
    # - map
    # ''')

if mode == 'indicators':
    ind = list(indicators.keys())
    ind_sel = ind.append('all')
    ind_selection = ind_sel #[long_names[i] if i in long_names.keys() else i for i in indicators[indicator]]

    st.sidebar.markdown('## Please select one indicator')
    indicator = st.sidebar.selectbox('select one indicator to have a closer look at the subindicators', ind, index=10, help='wip')

    if indicator == 'all':
        st.write('# Overview of all indicators')
        with st.expander('indicator calculation'):
            #st.write('here will be displayed the content of file {}.md'.format(i))
            st.write('the indicators are calculated on a rank based approach')        
        st.sidebar.markdown('## Sort by ...')
        # info_columns_raw = [{v: k for k, v in long_names.items()}[i] for i in info_columns]
        ind_sorter = st.sidebar.selectbox('to sort by one of the selected subindicators, please select:', ind) #+info_columns_raw)
        # ind_sorter = {v: k if k in long_names.keys() else for k, v in long_names.items()}[ind_sorter]
        standard_ind = figure1(2,len(df_ind_pure.columns),df_ind_pure.columns, df_ind_pure, ind_sorter)
        st.plotly_chart(standard_ind, use_container_width=True)
    else:
        st.sidebar.markdown('## Sort by ...')
        selection = [long_names[i] if i in long_names.keys() else i for i in indicators[indicator]]

        # selection = [i if i in long_names.keys() selection 
        sorter = st.sidebar.selectbox('to sort by one of the selected subindicators, please select:', selection+info_columns)

        st.sidebar.write("**here you can check/uncheck which of the indicators' subindicators should be displyed**")
        checks = [True] * len(selection)
        for i, subind in enumerate(selection):
            if st.sidebar.checkbox(subind, value=True):
                checks[i] = True
            else:
                checks[i] = False

        selection = list(np.array(selection)[checks])
        selection = [{v: k for k, v in long_names.items()}[i] for i in selection]
        sorter = {v: k for k, v in long_names.items()}[sorter]

        try:
            ind_template = read_markdown_file(BASEPATH+'/docs/{}.md'.format(indicator))
        except FileNotFoundError:
            ind_template = read_markdown_file(BASEPATH+'/docs/template_ind.md')
        st.write(ind_template)
        # st.write('# here is the definition of indicator {}'.format(indicator))

        col1, col2 = st.columns(2)
        for no, i in enumerate(selection):
            # titles = [long_names[i] if i in long_names.keys() else i for i in indices]
            try:
                template = read_markdown_file(BASEPATH+'/docs/{}.md'.format(i))
            except FileNotFoundError:
                template = read_markdown_file(BASEPATH+'/docs/template_sind.md')
            
            if (no%2)==0:
                with col1:
                    with st.expander('definition for subindicator {}'.format(long_names[i])):
                        #st.write('here will be displayed the content of file {}.md'.format(i))
                        st.write(template)
            else:
                with col2:
                    with st.expander('definition for subindicator {}'.format(long_names[i])):
                        #st.write('here will be displayed the content of file {}.md'.format(i))
                        st.write(template)
        
        if selection != None:
            fig1 = figure1(2,len(selection),selection, df, sorter)
            st.plotly_chart(fig1, use_container_width=True)

        if sorter == None:
            sorter = 'Population'


        if st.checkbox('View dataframe'):
            st.dataframe(df)

        if st.checkbox('View selection'):
            st.dataframe(df[selection])

if mode == 'subindicators':
    st.sidebar.markdown('## Please select subindicators')
    selectables = [long_names[i] if i in long_names.keys() else i for i in subind]
    selection = st.sidebar.multiselect('select up to 5 subindicators', tuple(selectables), default=None, 
                                       help='selected subindicators will be displayed on screen. Selecting more than 5 subindicators will result in plotting error')

    st.sidebar.markdown('## Sort by ...')
    sorter = st.sidebar.selectbox('to sort by one of the selected subindicators, please select:', selection+info_columns)

    selection = [{v: k for k, v in long_names.items()}[i] for i in selection]
    sorter = {v: k for k, v in long_names.items()}[sorter]

    if selection != None:
        fig1 = figure1(2,5,selection, df, sorter)
        st.plotly_chart(fig1, use_container_width=True)

    # if sorter == None:
    #     sorter = 'Population'
    # fig2 = figure1(2,5,info_columns, df, sorter)
    # st.plotly_chart(fig2, use_container_width=True)

    if st.checkbox('View dataframe'):
        st.dataframe(df)

    if st.checkbox('View selection'):
        st.dataframe(df[selection])

if mode == 'cities':
    st.sidebar.markdown('## Please select cities')
    city_sel = st.sidebar.multiselect('up to 5 cities can be selected', tuple(df_ind_pure.index), 
                                      default=['Strasbourg', 'Basel', 'Colmar', 'Karlsruhe', 'Freiburg im Breisgau'], 
                                      help='more than 5 selected cities will result in plotting error')

    if city_sel != None:
        if st.sidebar.checkbox('all in one plot'):
                fig = go.Figure()
                for city in city_sel:
                    r = df_ind_pure.loc[[city]].T[city].to_list()
                    r.append(r[0])
                    theta = df_ind_pure.loc[[city]].T.index.tolist()
                    theta.append(theta[0])
                    fig.add_trace(go.Scatterpolar(r=r, theta=theta, mode='lines', name=city))
                st.plotly_chart(fig, use_container_width=True)
        else:
            cols = st.columns(3) #st.columns(len(city_sel) // 2 +1)
            counter=0
            for city, col in zip(city_sel, itertools.cycle(cols)):
                with col:
                    fig = px.line_polar(df_ind_pure.loc[[city]].T, r=df_ind_pure.loc[[city]].T[city], theta=df_ind_pure.loc[[city]].T.index, line_close=True, title=city, range_r=[0,10])
                    st.plotly_chart(fig)


    # citydata = df.copy()

    # for col in subind:
    #     citydata[col] = citydata[col]/citydata[col].max()

    # citydata.columns = [long_names[i] if i in long_names.keys() else i for i in citydata.columns]
    # subind = [long_names[i] if i in long_names.keys() else i for i in subind]
    
    # if city_sel != None:
    #     city_fig = make_subplots(rows=1, cols=5, shared_yaxes=True, subplot_titles=city_sel)
    #     city_fig.update_layout(height=800, showlegend=False)

    #     for i, city in enumerate(city_sel):
    #         city_fig.add_trace(go.Bar(x=citydata[subind].loc[city], 
    #                                 y=citydata[subind].columns, 
    #                                 orientation='h'), row=1, col=i+1)

    #     st.plotly_chart(city_fig, use_container_width=True)






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

