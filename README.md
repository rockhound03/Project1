# Project1
Johnny 5 Team Repo


###############

# Project Title: Solar Flares, Coronal Mass Ejection (CME) relationships

Team Members: Veena Vinodkumar, Erica Frisch, Jason Peterson, Andrew Eckes

### Project Description: Look at Solar Flare and CME data to ...

### Research Questions to Answer:

    1. Do solar flares correlate to CME events?

    2. If the sun has a cycle of 11 years, can we determine where we are in this cycle based on the trend of CME events?

    3. Is there a correlation between power of a CME and speed of solar flares, when they happen at the same time.

    4. What does the "type" category for CME stand for? Can we infer a meaning based on some other category value?

### Hypothesis:  (Erica)
Do CMEs speed correlate to Solar Flare power?
 NULL: If a CME is faster,
       then a coinciding solar flare will not neccesarily be more powerful
 ALT: If a CME is faster,
       then a coinciding solar flare will be more powerful
### Statistical Test: (Erica)
Independent T-Test

### Datasets to be used: https://api.nasa.gov/
    DONKI Documnetation (for both APIs): https://ccmc.gsfc.nasa.gov/support/DONKI-webservices.php

    1. Solar Flares: DONKI Solar Flare (FLR)
    
        Demo API: https://api.nasa.gov/DONKI/FLR?startDate=2016-01-01&endDate=2016-01-30&api_key=DEMO_KEY


    2. Coronal Mass Ejection: DONKI (CME)
        Demo API: https://api.nasa.gov/DONKI/CME?startDate=2017-01-03&endDate=2017-01-03&api_key=DEMO_KEY
        
### Visualizations:

    1. Relationship between Solar Flares power & CME speeds (Jason)

    2. Trend of CMEs, Solare Flares, and Sunspots over the past five years (show 11 year cycle) (Andrew & Veena)

    3. How many of each (bar chart) (also include linked flr/cme ?) (Erica)

    4. Solar Flare power over time (Jason) 

    5. CME speeds over time (Erica)

    6. Sunspots north vs south (Veena)


### Rough Breakdown of Tasks:

    Veena:
        Cleaning data (getting key features)

    Erica:
        Extract data from Insight Mars Weather API

    Jason:
        Extract data from Solar Flare API

    Andrew:
        Correlation calculations