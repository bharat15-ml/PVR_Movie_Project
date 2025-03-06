# PVR_Movie_Project
This repository contains movie data collected from Indian theaters from various sources. Also, it showcases state-of-the-art (POC) of applying advanced data analytics to building ML Models to optimize business processes and provide solutions.

# Challanges 
1. Data Collection
   As source data is not publicly available with good quality, Significant effort and time consumed on data collection.
     theatre_data -> Collected indian movie theatre movie data from source - https://github.com/HarshaDevulapalli/indian-movie-theatres
     imdb data -> Collected indian movie datasets using api from source - https://developer.imdb.com/non-commercial-datasets/

2. Data Quality -> Not much theatre specific data publicaly available to lay down solution appraoch for business use cases. Important parameters and attributes seems missing or not recorded at single instance of time.
3. Data Cleaning -> As it have significant data quality issues, significant efforts has been put on data cleaning.
4. Data Exploration/understnding -> As no single source of truth or information available to lay down business problem and solutions collected data from various sources to lay down business foundation.
5. Theatre and IMDB Data -> It doesn't captures theatre and movie specfic info at sync so joining various source info seems not possible. This makes data mining process more difficult to find insightful pattern.

# Problem Statements - 
Predict #seats in theatre at any point of time based on movies and other meaningful features. (Based on available data extracted meaningful features and tried to predict number of seates.)

# Solution - ML Prdicton model to predict #seats.
