# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:07:47 2024

@author: LEBOGANG
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
df.columns=df.columns.str.replace("","")

#Removing empty cells using dropna
df.dropna(inplace = True)

#Reset the index
df=df.reset_index(drop=True)

#Generate a descriptive statistics of a DF 
print(df.describe())
print(df['Rating'].max())
highest_rated_movie = df.loc[df['Rating'].idxmax()]
print(df['Revenue (Millions)'].mean())

# average_revenue = df['Revenue (Millions)'].mean()
av = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)] 
ar = av['Revenue (Millions)'].mean()

#Movies that were released in the year 2016
movies_released = len(df[df['Year'] == 2016])
print(movies_released)
# Movies that were directed by Christopher Nolan
directed_movies = len(df[df['Director'] =='Christopher Nolan'])
print(directed_movies)

#Movies in the dataset with a rating of at least 8.0
rating_of_at_least_eight_point_zero = len(df[df['Rating'] >= 8.0])
print(rating_of_at_least_eight_point_zero)

#The median rating of movies directed by Christopher Nolan
Christopher_Nolan = df[df['Director']=='Christopher Nolan']
median_rating = Christopher_Nolan['Rating'].median
print(median_rating)  

#The year with the highest average rating
average_rating_by_year = df.groupby('Year')['Rating'].mean()
print(average_rating_by_year)

#the percentage increase in number of movies made between 2006 and 2016
movies_2006 = len(df[df['Year'] == 2006])
movies_2016 = len(df[df['Year'] == 2016])
percentage_increase = ((movies_2016-movies_2006)/movies_2006)*100
print(percentage_increase)

#The most common actor in all the movies
actors = df['Actors'].str.split(',').explode()
actor_counts = actors.value_counts()
most_common_actor = actor_counts.idxmax()
print(most_common_actor)

#unique genres are there in the dataset
genres = df['Genre'].str.split(',').explode()
unique_genres_count = genres.nunique()
print(unique_genres_count)

df.to_csv("movie_dataset.csv")






















