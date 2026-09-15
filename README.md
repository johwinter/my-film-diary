# my-film-diary
A personal film diary built with Python and Streamlit. Final Assignment for Technical Basics I, Sem 2, 2026

## About the Project

**My Film Diary** is a personal digital film diary created with Python and Streamlit.

---

## Features
- search for films
- add films to a wishlist
- mark films as watched, with a personal rating and written review
- all watched films are in a diary
- statistics with total films watched, average rating, genre breakdown
- all data saved locally between sessions (films.json)
- duplicate films are automatically prevented 

### Film Wishlist

* Search for films using the OMDb API.
* Preview film information before adding it.
* Add films to a personal wishlist.
* View film posters and information such as genre, director, plot and IMDb rating.
* Filter the wishlist by genre.
* Prevent the same film from being added twice.

### Mark as Watched

* Select a film from the wishlist.
* Mark it as watched.
* Give the film a personal rating from 1–5 stars.
* Write a personal review.

### Film Diary

* View all films that have been watched.
* See personal ratings and reviews.
* View film information and posters.
* Filter watched films by genre.

### Statistics

* See the total number of films watched.
* Calculate the average personal rating.
* View films grouped by genre.
* View films watched per month when watch dates are available.

### Data Storage

Film information is stored locally in a JSON file called `films.json`. This allows the application to keep the saved films between sessions.

---

## Technologies

The project was created using:

* **Python**: main programming language.
* **Streamlit**: used to create the web application and user interface.
* **OMDb API**: used to retrieve information about films.
* **Requests**: used to send requests to the OMDb API.
* **JSON**: used for storing film data locally.

---


The main Python file contains the application logic. The `films.json` file stores the film data, while the `documentation` folder contains information about the development process and references.

---

## Requirements:

- Python 3.9+
- OMDb API key (free, accessible on https://www.omdbapi.com/apikey.aspx)


## Setup

### 1. Install Python

### 2. Install the required libraries

Open the terminal in the project folder and run:


pip install streamlit requests

### 3. Add OMDb API key
Open app.py and replace the placeholder in this line near the top of the file with your own file:
API_KEY = "your_api_key_here"

### 3. Start Streamlit

Run:

streamlit run app.py

If everything works, the application should now open in the browser (😌😌)

---

## OMDb API

The application uses the OMDb API to retrieve film information.
When a user searches for a film, the application sends the film title to OMDb. If the film is found, information such as its title, year, genre, director, plot, IMDb rating and poster can be returned to the application.
The API requires an API key to make requests!! (That means you have to request your own API key first. That is free, if you have under a 1000 films that you look up per day).

---

## Documentation

The `documentation` folder contains additional information about the project, including:

* The development process.
* Problems encountered and how they were solved.
* AI assistance and other references.
* Planning and design.
* Testing.
* Reflection and possible future developments.

---

## Future Development

Possible future improvements include:

* Improving the search tab:
  * Currently, if you don't type in the correct name of the film, it cannot be found.
  * Another issue is that if there is two films that have the same name, you will only get one suggestion.
* Adding more ways to sort and filter films.
* Adding favourite films.
* Recording more information about individual viewing experiences.
* Further improving the visual design, user interface and overall experience.

---

## Project Context

This application was created as a final programming project for **Tech Basics 1**.

The project was developed as an opportunity to apply programming concepts learned during the course while also learning new concepts independently, including working with an external API and building a Streamlit web application.
Author: Johanna Winter
