import pandas as pd
import random

# Load the existing dataset
file_path = "theatre_cleaned.csv"  # Update with your file path
df_existing = pd.read_csv(file_path)

# Define possible values for new columns
indian_movies = [
    "Jawan", "Pathaan", "RRR", "KGF 2", "Pushpa", "Dangal", "Baahubali", "Drishyam 2",
    "Brahmastra", "Vikram", "Kantara", "Shershaah", "Sooryavanshi", "3 Idiots", "Kabir Singh"
]
showtimes = ["Morning", "Afternoon", "Evening", "Night"]
weather_conditions = ["Cloudy", "Rainy", "Sunny", "Stormy", "Hot", "Humid"]
holiday_impact = ["Yes", "No"]

# Expand dataset to 5000 records
expanded_data = []
for _ in range(5000):
    row = df_existing.sample(n=1, replace=True).iloc[0].to_dict()  # Sample an existing row
    row["Indian Movie Name"] = random.choice(indian_movies)
    row["Showtime"] = random.choice(showtimes)
    row["IMDB Rating"] = round(random.uniform(1, 10), 1)  # Random IMDb rating between 1-10
    row["Weather"] = random.choice(weather_conditions)
    row["Holiday/Event Impact"] = random.choice(holiday_impact)
    
    # Ensure 'total_seats' is numeric and generate ticket_sold value
    total_seats = pd.to_numeric(row.get("total_seats", 0), errors="coerce")
    row["ticket_sold"] = random.randint(0, total_seats) if not pd.isna(total_seats) else 0

    expanded_data.append(row)

# Create new DataFrame
df_expanded = pd.DataFrame(expanded_data)

# Save the new dataset to CSV
df_expanded.to_csv("theatre_seat_prediction.csv", index=False)

print("CSV file generated successfully!")

