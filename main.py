# Libraries Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset Load
df = pd.read_csv("data/netflix_titles.csv")
print(df.head())

# Basic Dataset Info
print("\nDataset Info:")
print(df.info())
print("\nShape of Dataset:")
print(df.shape)

# Missing Values Check
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")

# Movies vs TV Shows
content_type = df["type"].value_counts()
print("\nMovies vs TV Shows:")
print(content_type)

# Bar Chart
content_type.plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Top 10 Countries
top_countries = df["country"].value_counts().head(10)
print("\nTop 10 Countries:")
print(top_countries)

# Countries Chart
top_countries.plot(kind="bar")
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Shows")
plt.xticks(rotation=45)
plt.show()

# Top Genres
genres = df["listed_in"].str.split(", ")
all_genres = []
for genre_list in genres:
    all_genres.extend(genre_list)
genre_series = pd.Series(all_genres)
top_genres = genre_series.value_counts().head(10)
print("\nTop Genres:")
print(top_genres)

# Genre Chart
top_genres.plot(kind="bar")
plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Content Added Per Year
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year
yearly_content = df["year_added"].value_counts().sort_index()
print("\nContent Added Per Year:")
print(yearly_content)

# Year-wise Trend Chart
yearly_content.plot(kind="line")
plt.title("Netflix Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# Longest Movies
movies = df[df["type"] == "Movie"].copy()
movies["duration"] = movies["duration"].str.replace(" min", "")
movies["duration"] = pd.to_numeric(movies["duration"], errors="coerce")
longest_movies = movies.sort_values(by="duration", ascending=False)
print("\nTop 10 Longest Movies:")
print(longest_movies[["title", "duration"]].head(10))