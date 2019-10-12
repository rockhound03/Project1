# Project1
Johnny 5 Team Repo


########################################################################
Project Title: Solar Flares vs Mars Weather

Team Members: Veena Vinodkumar, Erica Frisch, Jason Peterson, Andrew Eckes

Project Description: Looking at Solar Flare events and Mars Weather data and seeing if there is an affect

Research Questions to Answer:
    1. Do solar flares affect the wind?
    2. Do solar flares affectt the temperature?

Datasets to be used: https://api.nasa.gov/
    1. Solar Flares: DONKI Solar Flare (FLR)
        https://data.ivanstanojevic.me/api/tle/docs
        Demo API: https://api.nasa.gov/DONKI/FLR?startDate=2016-01-01&endDate=2016-01-30&api_key=DEMO_KEY
    2. Mars Weather: Insight API
        https://api.nasa.gov/assets/insight/InSight%20Weather%20API%20Documentation.pdf

Rough Breakdown of Tasks:
    Veena:
        Cleaning data (getting key features)

    Erica:
        Extract data from Insight Mars Weather API

    Jason:
        Extract data from Solar Flare API

    Andrew:
        Joining datasets with time offset (for light distance)