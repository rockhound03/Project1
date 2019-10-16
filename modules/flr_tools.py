if __name__ == "__main__":
    pass

import math
import numpy as np
import pandas as pd
import requests
from config import api_key
import time
from datetime import datetime
# convert flare classification to watts/square meter (m^2)
def flare_power(flr_class = "C3.5"):
    try:
        pwr_scale = flr_class[0]
        pwr_range = float(flr_class[1:len(flr_class)])
    except:
        print("Error.  Check Syntax.")

    scale_dict ={"A" : {"high" : 10**-7 , "low" : 10**-8},
    "B" : {"high" : 10**-6, "low" : 10**-7},
    "C" : {"high" : 10**-5, "low" : 10**-6},
    "M" : {"high" : 10**-4, "low" : 10**-5},
    "X" : {"high" : 10**-3, "low" : 10**-4},
    "Z" : {"high" : 10**-2, "low" : 10**-3}}
    pwr_convertered = pwr_range * scale_dict[pwr_scale]['low']
    return pwr_convertered

# Parses response from api json response string.
def get_flare_dframe(api_json, nasa_time=False):
    df_dict = []
    for event in api_json:
        if(nasa_time):
            df_dict.append({"flare_id" : event['flrID'], "peak_time(zulu)" : event['peakTime'], 
            "class_type" : event['classType'], "power(w/m^2)" : flare_power(event['classType'])})
        else:
            try:
                peak_time_holder = convert_date_time(event['peakTime'])
            except:
                peak_time_holder = "Invalid format / no data."
            df_dict.append({"flare_id" : event['flrID'], "peak_time(zulu)" : peak_time_holder, 
            "class_type" : event['classType'], "power(w/m^2)" : flare_power(event['classType'])})
    result_df = pd.DataFrame(df_dict)
    return result_df
# Parses response from api json response string.  Includes start / end time, when available.
def get_flare_all_df(api_json, nasa_time=False):
    df_dict = []
    for event in api_json:
        all_linked = []
        try:
            [all_linked.append(activity) for activity in event['linkedEvents']]
        except TypeError:
            all_linked.append("None Found.")

        if(nasa_time):
            df_dict.append({"flare_id" : event['flrID'], "start_time(zulu)" : event['beginTime'], "peak_time(zulu)" : event['peakTime'], 
            "end_time(zulu)" : event['endTime'], "class_type" : event['classType'], "power(w/m^2)" : flare_power(event['classType']), 
            "linked_events" : all_linked})
        else:
            try:
                start_time_holder = convert_date_time(event['beginTime'])
            except:
                start_time_holder = "Invalid format / no data."
            try:
                peak_time_holder = convert_date_time(event['peakTime'])
            except:
                peak_time_holder = "Invalid format / no data."
            try:
                end_time_holder = convert_date_time(event['endTime'])
            except:
                end_time_holder = "Invalid format / no data."
            df_dict.append({"flare_id" : event['flrID'], "start_time(zulu)" : start_time_holder, "peak_time(zulu)" : peak_time_holder, 
            "end_time(zulu)" : end_time_holder, "class_type" : event['classType'], "power(w/m^2)" : flare_power(event['classType']), 
            "linked_events" : all_linked})
    result_df = pd.DataFrame(df_dict)
    return result_df
# query for flare activity by start/end date.  Includes linked events and start / end time.  Return data in json format.
def flare_query_all(start_date="2019-01-01", end_date="2019-10-13", nasa_time=False):
    query_flr_url = f"https://api.nasa.gov/DONKI/FLR?startDate={start_date}&endDate={end_date}&api_key={api_key}"
    flare_json = requests.get(query_flr_url).json()
    flare_df = get_flare_all_df(flare_json, nasa_time)
    return flare_df
# query for flare activity by start/end date. Return data in json format.
def flare_query_small(start_date="2019-01-01", end_date="2019-10-13", nasa_time=False):
    query_flr_url = f"https://api.nasa.gov/DONKI/FLR?startDate={start_date}&endDate={end_date}&api_key={api_key}"
    flare_json = requests.get(query_flr_url).json()
    flare_df = get_flare_dframe(flare_json, nasa_time)
    return flare_df
# Works, mars portion no longer needed. ************************************************************************
def cme_compare(cme_id, start_date="2019-01-01", end_date="2019-10-13"):
    query_cme_url =f"https://kauai.ccmc.gsfc.nasa.gov/DONKI/WS/get/CME?startDate={start_date}&endDate={end_date}"
    cme_request = requests.get(query_cme_url).json()
    cme_link = []
    found_impact = "Event not found."
    arrival_time = "No data"
    for cme in cme_request:
        if cme['activityID'] == cme_id:
            try:
                if cme['cmeAnalyses'][0]['enlilList'][0]['impactList'] != "None":
                    for link in cme['cmeAnalyses'][0]['enlilList'][0]['impactList']:
                        if link['location'] == "Mars":
                            found_impact = "Found Mars event."
                            arrival_time = link['arrivalTime']
            except TypeError:
                pass
    cme_link.append({"Connection" : found_impact, "Arrival Time" : arrival_time})
    return cme_link
# pass cme json response, return data analysis group in dataframe format. ***************************************************
def cme_analysis_df(cme_json):
    analysis_data = []
    for cme in cme_json:
        try:
            analysis_group = cme['cmeAnalyses'][0]
            data_dict = {"activity_id" : cme['activityID'], "speed" : analysis_group['speed'], "data_level" : analysis_group['levelOfData'],
            "lat" : analysis_group['latitude'], "long" : analysis_group['longitude'], "type" : analysis_group['type'], "half_angle" : analysis_group['halfAngle'], 
            "is_most_accurate" : analysis_group['isMostAccurate'], "time21_5" : analysis_group['time21_5'], "note" : analysis_group['note']}
        except:
            data_dict = {"activity_id" : cme['activityID'], "speed" : "no data", "data_level" : "no data",
            "lat" : "no data", "long" : "no data", "type" : "no data", "half_angle" : "no data", 
            "is_most_accurate" : False, "time21_5" : "no data", "note" : "no data"}
        analysis_data.append(data_dict)

    analysis_dataframe = pd.DataFrame(analysis_data)
    return analysis_dataframe
# ************************************************************************            

# Reformat date / time from nasa format to be slightly more readable.
def convert_date_time(nasa_zulu="2017-01-21T07:26Z"):
    reformat_time = datetime.strptime(nasa_zulu,'%Y-%m-%dT%H:%MZ')
    date_time_out = reformat_time.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time_out