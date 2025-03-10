import pandas as pd
import random

# Load the existing dataset
file_path = "PVR_Movie_Project/data/synthetic_data/theatre_cleaned.csv"  # Update with the correct file path if needed
df_existing = pd.read_csv(file_path)

# Define movie details with IMDb rating, genre, release date, production, cast, director, budget, and revenue
movie_details = {
    "3 Idiots": {"imdb_rating": 8.4, "genre": "Comedy, Drama", "release_date": "2009-12-25",
                 "production": "Vinod Chopra Films", "cast": "Aamir Khan, R. Madhavan, Sharman Joshi",
                 "director": "Rajkumar Hirani", "budget": 35000000, "revenue": 470000000},
    
    "Dangal": {"imdb_rating": 8.3, "genre": "Biography, Drama, Sport", "release_date": "2016-12-23",
               "production": "Walt Disney Pictures India", "cast": "Aamir Khan, Sakshi Tanwar, Fatima Sana Shaikh",
               "director": "Nitesh Tiwari", "budget": 70000000, "revenue": 2100000000},

    "Drishyam 2": {"imdb_rating": 8.2, "genre": "Crime, Drama, Thriller", "release_date": "2022-11-18",
                   "production": "Panorama Studios", "cast": "Ajay Devgn, Shriya Saran, Tabu",
                   "director": "Abhishek Pathak", "budget": 50000000, "revenue": 340000000},

    "RRR": {"imdb_rating": 7.8, "genre": "Action, Drama", "release_date": "2022-03-25",
            "production": "DVV Entertainment", "cast": "N.T. Rama Rao Jr., Ram Charan, Alia Bhatt",
            "director": "S.S. Rajamouli", "budget": 5500000000, "revenue": 12000000000},

    "Kantara": {"imdb_rating": 7.7, "genre": "Action, Adventure, Drama", "release_date": "2022-09-30",
                "production": "Hombale Films", "cast": "Rishab Shetty, Kishore Kumar G., Achyuth Kumar",
                "director": "Rishab Shetty", "budget": 160000000, "revenue": 4000000000},

    "KGF 2": {"imdb_rating": 7.3, "genre": "Action, Crime, Drama", "release_date": "2022-04-14",
              "production": "Hombale Films", "cast": "Yash, Sanjay Dutt, Raveena Tandon",
              "director": "Prashanth Neel", "budget": 1000000000, "revenue": 12500000000},

    "Vikram": {"imdb_rating": 7.3, "genre": "Action, Thriller", "release_date": "2022-06-03",
               "production": "Raaj Kamal Films International", "cast": "Kamal Haasan, Vijay Sethupathi, Fahadh Faasil",
               "director": "Lokesh Kanagaraj", "budget": 1500000000, "revenue": 4000000000},

    "Pushpa": {"imdb_rating": 7.4, "genre": "Action, Crime, Drama", "release_date": "2021-12-17",
               "production": "Mythri Movie Makers", "cast": "Allu Arjun, Fahadh Faasil, Rashmika Mandanna",
               "director": "Sukumar", "budget": 2500000000, "revenue": 3650000000},

    "Baahubali": {"imdb_rating": 8.0, "genre": "Action, Drama", "release_date": "2015-07-10",
                  "production": "Arka Media Works", "cast": "Prabhas, Rana Daggubati, Anushka Shetty",
                  "director": "S.S. Rajamouli", "budget": 1800000000, "revenue": 6500000000},

    "Shershaah": {"imdb_rating": 8.4, "genre": "Action, Biography, Drama", "release_date": "2021-08-12",
                  "production": "Dharma Productions", "cast": "Sidharth Malhotra, Kiara Advani, Shiv Panditt",
                  "director": "Vishnuvardhan", "budget": 550000000, "revenue": 1360000000},

    "Kabir Singh": {"imdb_rating": 7.1, "genre": "Drama, Romance", "release_date": "2019-06-21",
                    "production": "Cine1 Studios", "cast": "Shahid Kapoor, Kiara Advani, Soham Majumdar",
                    "director": "Sandeep Reddy Vanga", "budget": 600000000, "revenue": 3800000000},

    "Pathaan": {"imdb_rating": 6.3, "genre": "Action, Adventure, Thriller", "release_date": "2023-01-25",
                "production": "Yash Raj Films", "cast": "Shah Rukh Khan, Deepika Padukone, John Abraham",
                "director": "Siddharth Anand", "budget": 2500000000, "revenue": 10500000000},

    "Brahmastra": {"imdb_rating": 5.6, "genre": "Action, Adventure, Fantasy", "release_date": "2022-09-09",
                   "production": "Dharma Productions", "cast": "Ranbir Kapoor, Alia Bhatt, Amitabh Bachchan",
                   "director": "Ayan Mukerji", "budget": 4100000000, "revenue": 4300000000},

    "Jawan": {"imdb_rating": 7.0, "genre": "Action, Thriller", "release_date": "2023-06-02",
              "production": "Red Chillies Entertainment", "cast": "Shah Rukh Khan, Nayanthara, Vijay Sethupathi",
              "director": "Atlee Kumar", "budget": 2200000000, "revenue": 8000000000},

    "Sooryavanshi": {"imdb_rating": 6.5, "genre": "Action, Crime, Thriller", "release_date": "2021-11-05",
                     "production": "Reliance Entertainment", "cast": "Akshay Kumar, Katrina Kaif, Ajay Devgn",
                     "director": "Rohit Shetty", "budget": 1650000000, "revenue": 2900000000}
}

# Define possible values for other columns
showtimes = ["Morning", "Afternoon", "Evening", "Night"]
weather_conditions = ["Cloudy", "Rainy", "Sunny", "Stormy", "Hot", "Humid"]
holiday_impact = ["Yes", "No"]

# Expand dataset to 5000 records
expanded_data = []
for _ in range(5000):
    row = df_existing.sample(n=1, replace=True).iloc[0].to_dict()  # Sample an existing row
    selected_movie = random.choice(list(movie_details.keys()))
    
    row.update(movie_details[selected_movie])
    row["movie_name"] = selected_movie
    row["showtime"] = random.choice(showtimes)
    row["weather"] = random.choice(weather_conditions)
    row["holiday_event_impact"] = random.choice(holiday_impact)

    # Ensure 'total_seats' is numeric and generate ticket_sold value
    total_seats = pd.to_numeric(row.get("total_seats", 0), errors="coerce")
    row["ticket_sold"] = random.randint(0, total_seats) if not pd.isna(total_seats) else 0

    expanded_data.append(row)

# Create new DataFrame and save to CSV
df_expanded = pd.DataFrame(expanded_data)
df_expanded.to_csv("theatre_seat_prediction.csv", index=False)

print("CSV file generated successfully with complete movie details!")

