# 🎬 Movie Recommender System

A content based movie recommendation system built using NLP techniques and cosine similarity with an interactive Streamlit interface.

## Project Overview

This is a content based Movie Recommender System that I built primarily to understand how machine learning models are created from raw data. After building the model and understanding the complete preprocessing and similarity pipeline, I extended the project by connecting it to a user interface so that the recommendations could be used interactively.

The application allows a user to select a movie and receive similar movie recommendations along with posters and IMDb ratings through a Streamlit interface.

---

## Problem Statement

Streaming platforms recommend movies based on similarity between content. I wanted to understand how such recommendations work internally without using user history or collaborative filtering.

The goal of this project was to recommend movies by analysing their content such as genres, keywords, cast, crew, production companies, and overview text. The system focuses on explainable recommendations using similarity between movie features.

---

## Features

* Movie search and selection interface
* Top 5 similar movie recommendations
* Poster display for recommended movies
* IMDb rating integration
* Clean Streamlit based UI
* Fallback handling when posters or ratings are missing
* Precomputed similarity for fast recommendations

---

## How It Works

I first focused on building the machine learning pipeline. The movies and credits datasets were merged and only the relevant columns were selected. From each movie I extracted genres, keywords, cast members, director, production companies, and overview.

These features were combined into a single text column called tags. The text was cleaned, converted to lowercase, and processed using Porter Stemming so that similar words map to the same root form.

The processed tags were converted into numerical vectors using CountVectorizer. After vectorization, cosine similarity was calculated between all movies to measure how closely they are related.

The similarity matrix and processed movie data were saved using pickle so the model does not need to be recomputed while running the application.

After understanding the model pipeline, I connected it to a Streamlit interface so users could interact with the recommender system directly.

When a user selects a movie:

1. The system finds its similarity scores.
2. The most similar movies are selected.
3. Posters and ratings are fetched using an external API.
4. Results are displayed in the Streamlit interface.

---

## Dataset and API Choice

I used the TMDB 5000 Movies dataset because it provides rich metadata such as cast, crew, keywords, and production details which are important for content based filtering. The dataset structure made it suitable for building meaningful similarity relationships between movies.

For posters and ratings, TMDB site was not accessible in my region, so I used the OMDb API by querying movie titles. This approach also helped me handle missing data cases properly by checking API responses and providing fallback images when poster data was unavailable.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* OMDb API
* Pickle
* uv (Python environment and dependency management)

---

## Project Structure

```
Movie-Recommender/

    data/
        tmdb_5000_credits.csv
        tmdb_5000_movies.csv

    model/

    notebooks/
        code.ipynb

    test/
        Assets/
            noImage.jpg
        model/
            movies_dict.pkl
            similarity.pkl
        Screenshots/
            Home.png
            Home-Search.png
        .gitignore
        .python-version
        main.py
        pyproject.toml
        README.md
        uv.lock

    README.md
```

---

## Installation

Make sure Python 3.12 or newer is installed.

Clone the repository:

```
git clone https://github.com/RutvikUpadhya/movie-recommender.git
cd movie-recommender/test
```

Install dependencies using uv:

```
pip install uv
uv sync
```

---

## Run Instructions

Run the Streamlit application:

```
uv run streamlit run main.py
```

Open the local URL shown in the terminal to use the application.

---

## Screenshots

* Home screen
![Home](test/Screenshots/Home.png)
![Home-2](test/Screenshots/Home-Search.png)


* Recommendation results page

---

## Future Improvements

* Add genre based filtering
* Improve ranking strategy beyond cosine similarity
* Deploy the application online
* Add user personalization features
* Improve caching for API requests

---

## Author

This project was developed as a hands on implementation to understand how recommendation models are built and then extended further to integrate the model into a usable interactive application.

Rutvik S Upadhya  
GitHub: https://github.com/RutvikUpadhya