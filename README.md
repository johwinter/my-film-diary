# my-film-diary
A personal film diary built with Python and Streamlit. Final Assignment for Technical Basics I, Sem 2, 2026

## About the Project

**My Film Diary** is a personal digital film diary created with Python and Streamlit.

My project is a personal film diary. It is a Streamlit application where I can search for films, save films I want to watch, and keep track of films I have already watched. Additionally, I can give reviews and ratings. The application uses the OMBd API to automatically retrieve information about films. 
The idea for a personal film diary came to me in the first class, when we were introduced to the seminar and first spoke about the final assessment. Just a month before, I was able to work at the Berlinale, the International Film Festival in Berlin, in the Jury Office, where I got to not only watch films (with the International Jury) but also experienced how the jury discussed the films, what mattered to them and how they break down the different aspects of a „good“ film. 
I have previously used the platform Letterboxd to keep track of the films I consume. However, after a couple of years, it has yet become another social media platform for me, where I interact with friends. With the aim to reduce my social media consumption and trying to consume films in a more focused way, I started to think about keeping an analogue film diary. While that is a beautiful way to connect your thoughts after seeing a film, it sometimes comes a little unhandy. Furthermore, I soon realised that only one notebook is not going to contain enough pages. 
In our first class, I got the idea, that I can combat this problem myself by trying to build my own application.

---

## Features

### Film Wishlist

* Search for films using the OMDb API.
* Preview film information before adding it.
* Add films to a personal wishlist.
* View film posters and information such as genre, director, plot and IMDb rating.
* Filter the wishlist by genre.
* Prevent the same film from being added twice.

### ✅ Mark as Watched

* Select a film from the wishlist.
* Mark it as watched.
* Give the film a personal rating from 1–5 stars.
* Write a personal review.

### 📖 Film Diary

* View all films that have been watched.
* See personal ratings and reviews.
* View film information and posters.
* Filter watched films by genre.

### 📊 Statistics

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

## Project Structure

```text
my-film-diary/
│
├── app.py
├── films.json
├── requirements.txt
├── README.md
│
├── documentation/
│   ├── project_documentation.md
│   ├── development_log.md
│   └── ai_and_references.md
│   └── sketches/
│       ├── initial_idea.jpg
│       ├── wishlist_sketch.jpg
│       └── diary_sketch.jpg
│
└── screenshots/
```

The main Python file contains the application logic. The `films.json` file stores the film data, while the `documentation` folder contains information about the development process and references.

---

## How to Run the Application

### 1. Install Python

### 2. Install the required libraries

Open the terminal in the project folder and run:

```bash
pip install streamlit requests
```

### 3. Start Streamlit

Run:

```bash
streamlit run app.py
```

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
