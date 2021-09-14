sind_map = [
    {
        "ind": "bikeability",
        "sind": "30kmh_speed_limit",
        "sql": "30kmh_speed_limit_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "bikeability",
        "sind": "slope",
        "sql": "slope_urban_func.sql",
        "rank_ascending": False,
    },
    {
        "ind": "bikeability",
        "sind": "n_bikesharing_bikes",
        "sql": "n_bikesharing_bikes_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "bikeability",
        "sind": "low_traffic_vol",
        "sql": "low_traffic_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "bikeability",
        "sind": "heavy_vehicles",
        "sql": "ratio_truckacc_urban_func.sql",
        "rank_ascending": False,
    },
    # {
    #     "ind": "bikeability",
    #     "sind": "bike_service_stations",
    #     "sql": "bike_service_stations_func.sql",
    #     "rank_ascending": True,
    # },
    {
        "ind": "walkability",
        "sind": "30kmh_speed_limit",
        "sql": "30kmh_speed_limit_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "walkability",
        "sind": "pedest_street_dens",
        "sql": "dens_pedest_street_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "walkability",
        "sind": "low_traffic_vol",
        "sql": "low_traffic_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "walkability",
        "sind": "green_area",
        "sql": "green_area_urban_func.sql",
        "rank_ascending": True,
    },
    # {"ind": "walkability", "sind": "park_area", "sql": "ratio_parks_urban_func.sql"},
    {
        "ind": "walkability",
        "sind": "walk_stim_fac",
        "sql": "walk_stimul_fac_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "walkability",
        "sind": "carfree_streets",
        "sql": "share_carfree_streets.sql",
        "rank_ascending": True,
    },
    # {"ind": "walkability", "sind": "pop_near_park", "sql": "pop_near_parks.sql"},
    # {
    #     "ind": "walkability",
    #     "sind": "park_ensas",
    #     "sql": "park_pop_share_urban_func.sql",
    #     "rank_ascending": True,
    # },
    {
        "ind": "public_transport",
        "sind": "serv_freq",
        "sql": "pt_mean_trips_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "public_transport",
        "sind": "serv_dur",
        "sql": "pt_mean_dur_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "public_transport",
        "sind": "stop_dens",
        "sql": "pt_stop_dens_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "public_transport",
        "sind": "coverage",
        "sql": "pt_cover_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "public_transport",
        "sind": "pop_near_pt",
        "sql": "pop_near_pt.sql",
        "rank_ascending": True,
    },
    # {"ind": "public_transport", "sind": "pt_impaired_uncertainty", "sql": "pt_impaired_uncertainty_func.sql"},
    {
        "ind": "public_transport",
        "sind": "pt_impaired",
        "sql": "pt_impaired_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "public_transport",
        "sind": "pt_price",
        "sql": "pt_price_func.sql",
        "rank_ascending": False,
    },
    {
        "ind": "public_transport",
        "sind": "pt_intermodal_connection",
        "sql": "pt_intermodal_connection_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "car",
        "sind": "pollu_regul",
        "sql": "environ_zone_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "car",
        "sind": "fuel_stat",
        "sql": "fuel_st_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "car",
        "sind": "onewaystr",
        "sql": "one_way_streets_urban_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "car",
        "sind": "n_carsharing_cars",
        "sql": "n_carsharing_cars_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "car",
        "sind": "n_parking_places",
        "sql": "n_parking_places_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "car",
        "sind": "parking_price",
        "sql": "parking_price_func.sql",
        "rank_ascending": False,
    },
    {
        "ind": "car",
        "sind": "traffic_jam",
        "sql": "traffic_jam_func.sql",
        "rank_ascending": False,
    },
    {
        "ind": "car",
        "sind": "ev_charging_station_density",
        "sql": "ev_charging_station_density_func.sql",
        "rank_ascending": True,
    },
    # {"ind": "pollution", "sind": "noise_rail_night", "sql": "noise_rail_night_urban_func.sql"},
    # {"ind": "pollution", "sind": "noise_rail_day", "sql": "noise_rail_day_urban_func.sql"},
    # {"ind": "pollution", "sind": "noise_road_night", "sql": "noise_road_night_urban_func.sql"},
    # {"ind": "pollution", "sind": "noise_road_day", "sql": "noise_road_day_urban_func.sql"},
    {
        "ind": "pollution",
        "sind": "streets_length",
        "sql": "streets_length_per_inhabitants_func.sql",
        "rank_ascending": True,
    },
    # {"ind": "pollution", "sind": "noise_rail", "sql": "noise_rail_urban_func.sql", "rank_ascending": False},
    # {"ind": "pollution", "sind": "noise_road", "sql": "noise_road_urban_func.sql", "rank_ascending": False,},
    {"ind": "traffic_safety", "sind": "car_acc_d", "sql": "car_deadly_traffic_accidents.sql", "rank_ascending": False},
    {"ind": "traffic_safety", "sind": "car_acc", "sql": "car_traffic_accidents.sql", "rank_ascending": False},
    {
        "ind": "traffic_safety",
        "sind": "bike_acc_d",
        "sql": "bike_deadly_traffic_accidents.sql",
        "rank_ascending": False,
    },
    {"ind": "traffic_safety", "sind": "bike_acc", "sql": "bike_traffic_accidents.sql", "rank_ascending": False},
    {
        "ind": "traffic_safety",
        "sind": "pedest_acc_d",
        "sql": "pedest_deadly_traffic_accidents.sql",
        "rank_ascending": False,
    },
    {"ind": "traffic_safety", "sind": "pedest_acc", "sql": "pedest_traffic_accidents.sql", "rank_ascending": False},
    {"ind": "emission", "sind": "pm10", "sql": "pm10_per_inhabitant_func.sql", "rank_ascending": False},
    {"ind": "emission", "sind": "pm25", "sql": "pm25_per_inhabitant_func.sql", "rank_ascending": False},
    {"ind": "emission", "sind": "nox", "sql": "nox_per_inhabitant_func.sql", "rank_ascending": False},
    # {"ind": "accessibility", "sind": "accessibility_poi_sum", "sql": "accessibility_weighted_poi_sum_func.sql"},
    # {"ind": "accessibility", "sind": "accessibility_poi_share", "sql": "accessibility_weighted_poi_share_func.sql"},
    {
        "ind": "commuting",
        "sind": "travel_time_regional_centers_pt",
        "sql": "travel_time_centers_pt_func.sql",
        "rank_ascending": False,
    },
    {
        "ind": "commuting",
        "sind": "travel_time_regional_centers_car",
        "sql": "travel_time_centers_car_func.sql",
        "rank_ascending": False,
    },
    {
        "ind": "commuting",
        "sind": "travel_speed_regional_centers_pt",
        "sql": "travel_speed_centers_pt_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "commuting",
        "sind": "travel_speed_regional_centers_car",
        "sql": "travel_speed_centers_car_func.sql",
        "rank_ascending": True,
    },
    # {
    #     "ind": "functional_diversity",
    #     "sind": "distance_to_business",
    #     "sql": "distance_to_business_func.sql",
    #     "rank_ascending": False,
    # },
    {
        "ind": "functional_diversity",
        "sind": "density_business",
        "sql": "density_business_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "functional_diversity",
        "sind": "density_education",
        "sql": "density_education_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "functional_diversity",
        "sind": "density_medical_services",
        "sql": "density_medical_services_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "functional_diversity",
        "sind": "density_shopping",
        "sql": "density_shopping_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "functional_diversity",
        "sind": "density_leisure",
        "sql": "density_leisure_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "accessibility",
        "sind": "accessible_functions_by_bike",
        "sql": "accessible_functions_by_bike_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "accessibility",
        "sind": "accessible_functions_by_pt",
        "sql": "accessible_functions_by_pt_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "accessibility",
        "sind": "accessible_functions_by_walk",
        "sql": "accessible_functions_by_walk_func.sql",
        "rank_ascending": True,
    },
    {
        "ind": "accessibility",
        "sind": "accessible_functions_by_car",
        "sql": "accessible_functions_by_car_func.sql",
        "rank_ascending": True,
    },
    {"ind": "info", "sind": "urban_share", "sql": "urban_share_func.sql", "rank_ascending": True},
    {
        "ind": "info",
        "sind": "population_density_urban_area",
        "sql": "urban_pop_density_func.sql",
        "rank_ascending": True,
    }
    # {"ind": "behavior", "sind": "walk_trips", "sql": None},
    # {"ind": "behavior", "sind": "bike_trips", "sql": None},
    # {"ind": "behavior", "sind": "electricfic", "sql": None},
    # {"ind": "behavior", "sind": "motori", "sql": None},
    # {"ind": "walkability", "sind":"paved_streets", "sql": None},
]


def get_all_sind():
    return list(set([i.get("sind") for i in sind_map]))


def get_sql_file(sind):
    try:
        return [i.get("sql") for i in sind_map if i.get("sind") == sind][0]
    except:
        print(sind, "not found")
        return None


def get_sind_of_ind(ind):
    return [i.get("sind") for i in sind_map if i.get("ind") == ind]


def get_all_ind():
    return list(set([i.get("ind") for i in sind_map if not i.get("ind") == "info"]))


def get_is_ascending(sind):
    return [i.get("rank_ascending") for i in sind_map if i.get("sind") == sind][0]


# dict = {

#     'walkability': ['30kmh_speed_limit', 'pedest_street_dens', 'low_traffic_vol',
#                     'green_area', 'park_area', 'walk_stim_fac', 'buildHeight_streetWidth', 'carfree_area'],
#     'bikeability': ['30kmh_speed_limit', 'bike_street_dens', 'low_traffic_vol',
#                     'heavy_vehicles', 'slope', 'bike_fac', 'paved_streets', 'bike_share_st', 'bike_share_no'],
#     'public_transport': ['serv_freq', 'serv_dur', 'stop_dens', 'coverage',
#                          'cost', 'crowded_st', 'intermod_int'],
#     'urban_func_div': ['urban_func_div', 'business', 'commercial', 'gen_serv',
#                        'soc_elder', 'res_fam', 'hosp_med', 'educa_serv', 'entertain',
#                        'sport_park_out', 'touri_cult'],
#     'mobil_behav': ['walk_trips', 'bike_trips', 'electricfic', 'motori', 'pt_shareOtrips']
#     'car_transp': ['30kmh_speed_limit', 'poll_regul', 'parking_price', 'fuel_st', 'echarge_st', 'onewaystr', 'traf_light', 'congest_road', 'car_share']

#     'innov_mobil': ['car_share', 'bike_share', 'intermodal'],
#     'mobil_behav': ['pub_trans_mod_share', 'bike_mod_share', 'walk_mod_share',
#                     'no_e_car', 'no_car'],
#     'ind_motor_trans_int': ['pollu_regul', 'speed_limit', 'parking_cost', 'fuel_stat',
#                             'park+ride', 'e_charge_st']
#     }
