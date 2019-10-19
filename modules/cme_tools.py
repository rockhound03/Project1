from flr_tools import *

# query for cme activity by start/end date.  Includes linked events and start / end time.
def cme_query_all(start_date="2019-01-01", end_date="2019-10-13", nasa_time=False):
    query_cme_url = f"https://api.nasa.gov/DONKI/CME?startDate={start_date}&endDate={end_date}&api_key={api_key}"
    cme_json = requests.get(query_cme_url).json()
    cme_df = get_cme_all_df(cme_json, nasa_time)
    return cme_df

# ************************************************************************  
# Takes API JSON for CMEs and returns dataframe with data
def get_cme_all_df(api_json, nasa_time=False):
    cme_ids = []
    linked = []
    speeds = []
    types = []
    start_time_nasa = []

    for event in api_json:
        try:
            linked.append(event['linkedEvents'])
        except:
            linked.append('None Found')
        try:
            speeds.append(event["cmeAnalyses"][0]['speed'])
            types.append(event["cmeAnalyses"][0]['type'])
        except:
            speeds.append('NA')
            types.append('NA')

        cme_ids.append(event["activityID"])
        start_time_nasa.append(event["startTime"])

    start_time = [convert_date_time(time) for time in start_time_nasa]

    df = pd.DataFrame({
                "cme_id": cme_ids,
                "speed": speeds,
                "type": types,
                "linked_events": linked
    })
    
    if nasa_time:
        df['start time'] = start_time_nasa
        return df
    else:
        df['start time'] = start_time
        return df

# Takes in a datframe (ID column renamed to 'id') and event type, inputs should be opposite
# CME df with event_type = 'FLR' or Flare df with event_type = 'CME'
# Returns list of linked event ids, can be used to cross reference the two dataframes
def linked_events(df, event_type='FLR'):
    ids = []
    for i,row in df.iterrows():
        try:
            for each in row['linked_events']:
                if event_type in each['activityID']:
                    ids.append([row['id'],each['activityID']])
        except:
            pass
    return ids