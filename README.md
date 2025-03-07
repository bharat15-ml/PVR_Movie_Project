# PVR_Movie_Project
PVR Movie Dataset - Seat Prediction

This repository contains a dataset of PVR movie theater bookings, designed for building predictive models to estimate the number of seats booked for a given show. The dataset includes features such as movie name, show timing, theater location, past booking trends, day of the week, and special events.

🔹 Key Features:
Historical movie ticket booking data
Factors influencing seat occupancy (e.g., time, location, events)
Suitable for regression and time-series forecasting models
📌 Use this dataset to develop machine learning models for predicting seat availability and optimizing theater occupancy! 🎬🍿

# Challanges 
1. Data Collection
   As source data is not publicly available with good quality, Significant effort and time consumed on data collection.
     theatre_data -> Fetched indian movie theatre data from IMDB API. Source - https://github.com/HarshaDevulapalli/indian-movie-theatres
   
     imdb data -> Collected indian movie datasets using api from source - https://developer.imdb.com/non-commercial-datasets/

3. Data Quality -> Not much theatre specific data publicaly available to lay down solution appraoch for business use cases. Important parameters and attributes seems missing or not recorded at single instance of time.
4. Data Cleaning -> As it have significant data quality issues, significant efforts has been put on data cleaning.
5. Data Exploration/understnding -> As no single source of truth or information available to lay down business problem and solutions, So we tried collecting data from various sources to lay down business use case and problem/solution.

7. Theatre and IMDB Data -> It doesn't captures theatre and movie specfic info at sync, so joining various source info seems not possible. This makes data mining process more difficult to find insightful pattern.

# Problem Statements - 
Predict #seats in theatre at any point of time based on movies and other meaningful features. (Based on available data extracted meaningful features and tried to predict number of seates.)

# Solution - ML Prdicton model to predict #seats.
