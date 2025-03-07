# PVR_Movie_Project
PVR Movie Dataset - Seat Prediction

This repository contains a dataset of PVR movie theater bookings, designed for building predictive models to estimate the number of seats booked for a given show. The dataset includes features such as movie name, show timing, theater location, past booking trends, day of the week, and special events.

🔹 Key Features:
Historical movie ticket booking data
Factors influencing seat occupancy (e.g., time, location, events)
Suitable for regression and time-series forecasting models
📌 Use this dataset to develop machine learning models for predicting seat availability and optimizing theater occupancy! 🎬🍿

# Challenges Faced
Data Collection – High-quality, publicly available data is scarce, requiring significant time and effort for data gathering.

Theatre Data: Indian movie theatre data was fetched using the IMDB API.
IMDB Data: Indian movie datasets were collected via the IMDB API.
Data Quality – Theatre-specific data is limited, making it difficult to design a robust business solution. Critical parameters and attributes are either missing or not recorded consistently at a single point in time.

Data Cleaning – Due to significant data quality issues, extensive cleaning was required to ensure accuracy and consistency.

Data Exploration & Understanding – No single source of truth exists for theatre and movie data, making it challenging to define business problems and solutions. We had to aggregate data from multiple sources to establish a viable use case.

Theatre & IMDB Data Integration – Theatre and movie-specific data are not synchronized across sources, making it difficult to join datasets. This lack of alignment complicates the data mining process and hinders the discovery of meaningful patterns.

# Problem Statement
Develop a predictive model to estimate the number of occupied seats in a theatre at any given time based on movie-specific and other relevant features. Using the available data, meaningful features were extracted to enhance prediction accuracy and identify patterns influencing seat occupancy.

# Solution - ML Prdicton model to predict #seats.
