import streamlit as st
import json
import os
import requests

API_KEY = "your_api_key_here"  # Replace with your actual key

# ---------- DATA FUNCTIONS ----------

def load_films():
    if os.path.exists("films.json"):
        try:
            with open("films.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            st.warning("⚠️ Your saved film data appears to be corrupted. Starting with an empty list.")
            return []
    return []

def save_films(films):
    with open("films.json", "w") as file:
        json.dump(films, file)

def search_film(title):
    """
    Searches OMDb for a film.
    Returns the film data if found, None if not found,
    or the string "connection_error" if OMDb couldn't be reached.
    """
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return "connection_error"

    data = response.json()

    if data.get("Response") == "True":
        return data
    return None

def get_unique_genres(films):
    genres = set()  # a "set" automatically ignores duplicates
    for film in films:
        for genre in film.get("genre", "").split(","):
            genre = genre.strip()
            if genre and genre != "Unknown":
                genres.add(genre)
    return sorted(genres)  # alphabetical order

# ---------- PAGE FUNCTIONS ----------

def page_wishlist(films):
        st.header("🎬 My Wishlist")

        # --- Add a film section ---
        st.subheader("Add a Film")
        title = st.text_input("Enter a film title:")

        if st.button("Search"):
            if title == "":
                st.warning("Please enter a film title first!")
            else:
                with st.spinner(f"Searching for '{title}'..."):
                    data = search_film(title)

                if data == "connection_error":
                    st.error("⚠️ Couldn't reach the film database. Please check your internet connection and try again.")
                    st.session_state["search_result"] = None
                elif data is None:
                    st.error("❌ Film not found. Please check the title and try again.")
                    st.session_state["search_result"] = None
                else:
                    st.session_state["search_result"] = data  # remember the result

        # --- Show a preview if we have a search result waiting ---
        if st.session_state.get("search_result"):
            data = st.session_state["search_result"]

            st.divider()
            st.subheader("Preview")

            col1, col2 = st.columns([1, 2])
            with col1:
                if data.get("Poster") and data["Poster"] != "N/A":
                    st.image(data["Poster"], width=150)
            with col2:
                st.write(f"**{data.get('Title')}** ({data.get('Year')})")
                st.write(f"**Director:** {data.get('Director', 'Unknown')}")
                st.write(f"**Genre:** {data.get('Genre', 'Unknown')}")
                st.write(f"**IMDb Rating:** ⭐ {data.get('imdbRating', 'N/A')}")

            col_confirm, col_discard = st.columns(2)

            with col_confirm:
                if st.button("✅ Add to Wishlist"):
                    already_exists = any(f["title"].lower() == data["Title"].lower() for f in films)
                    if already_exists:
                        st.warning(f"'{data['Title']}' is already in your list!")
                    else:
                        film = {
                            "title": data.get("Title", title),
                            "year": data.get("Year", "Unknown"),
                            "genre": data.get("Genre", "Unknown"),
                            "director": data.get("Director", "Unknown"),
                            "plot": data.get("Plot", "Unknown"),
                            "imdb_rating": data.get("imdbRating", "N/A"),
                            "poster": data.get("Poster", ""),
                            "watched": False,
                            "review": "",
                            "rating": 0
                        }
                        films.append(film)
                        save_films(films)
                        st.success(f"✅ '{film['title']}' ({film['year']}) added to your wishlist!")
                        st.session_state["search_result"] = None  # clear the preview

            with col_discard:
                if st.button("❌ Discard"):
                    st.session_state["search_result"] = None

        st.divider()

        # --- View wishlist section ---
        st.subheader("Your Wishlist")
        unwatched = [f for f in films if not f.get("watched", False)]

        # --- Genre filter ---
        genre_options = ["All"] + get_unique_genres(unwatched)
        selected_genre = st.selectbox("Filter by genre:", genre_options, key="wishlist_genre_filter")

        if selected_genre != "All":
            unwatched = [f for f in unwatched if selected_genre in f.get("genre", "")]

        if len(unwatched) == 0:
            st.info("Your wishlist is empty — add a film above!")
        else:
            for film in unwatched:
                with st.expander(f"🎥 {film['title']} ({film['year']})"):
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        if film["poster"] and film["poster"] != "N/A":
                            st.image(film["poster"], width=150)
                    with col2:
                        st.write(f"**Director:** {film['director']}")
                        st.write(f"**Genre:** {film['genre']}")
                        st.write(f"**IMDb Rating:** ⭐ {film['imdb_rating']}")
                        st.write(f"**Plot:** {film['plot']}")


def page_mark_watched(films):
    st.header("✅ Mark as Watched")
    unwatched = [f for f in films if not f.get("watched", False)]

    if len(unwatched) == 0:
        st.info("No films in your wishlist yet!")
        return

    film_titles = [f["title"] for f in unwatched]
    selected_title = st.selectbox("Which film did you watch?", film_titles)
    selected_film = next(f for f in unwatched if f["title"] == selected_title)

    st.write(f"**Director:** {selected_film['director']}")
    st.write(f"**Genre:** {selected_film['genre']}")

    review = st.text_area("Write your review:")
    rating = st.slider("Your star rating:", min_value=1, max_value=5, value=3)
    st.write("⭐" * rating)

    if st.button("Mark as Watched"):
        if review == "":
            st.warning("Please write a short review first!")
        else:
            selected_film["watched"] = True
            selected_film["review"] = review
            selected_film["rating"] = rating
            save_films(films)
            st.success(f"🎉 '{selected_film['title']}' marked as watched!")
            st.balloons()

def page_diary(films):
    st.header("📖 My Film Diary")
    watched = [f for f in films if f.get("watched", False)]

    # --- Genre filter ---
    genre_options = ["All"] + get_unique_genres(watched)
    selected_genre = st.selectbox("Filter by genre:", genre_options)

    if selected_genre != "All":
        watched = [f for f in watched if selected_genre in f.get("genre", "")]

    if len(watched) == 0:
        st.info("You haven't marked any films as watched yet!")
    else:
        for film in watched:
            with st.expander(f"⭐ {film['title']} ({film['year']}) — {'⭐' * film.get('rating', 0)}"):
                col1, col2 = st.columns([1, 2])
                with col1:
                    if film["poster"] and film["poster"] != "N/A":
                        st.image(film["poster"], width=150)
                with col2:
                    st.write(f"**Director:** {film['director']}")
                    st.write(f"**Genre:** {film['genre']}")
                    st.write(f"**IMDb Rating:** ⭐ {film['imdb_rating']}")
                    st.write(f"**Your Rating:** {'⭐' * film.get('rating', 0)}")
                    st.write(f"**Your Review:** {film['review']}")
                    st.write(f"**Plot:** {film['plot']}")

def page_statistics(films):
    st.header("📊 My Statistics")
    watched = [f for f in films if f.get("watched", False)]

    if len(watched) == 0:
        st.info("Watch and rate some films first to see your statistics!")
        return

    # --- Overview numbers ---
    total_watched = len(watched)
    average_rating = sum(f.get("rating", 0) for f in watched) / total_watched

    col1, col2 = st.columns(2)
    col1.metric("🎬 Films Watched", total_watched)
    col2.metric("⭐ Average Rating", f"{average_rating:.1f}")

    st.divider()

    # --- Genre breakdown ---
    st.subheader("Films by Genre")
    genre_counts = {}
    for film in watched:
        genres = film.get("genre", "Unknown").split(",")  # genres are comma-separated
        for genre in genres:
            genre = genre.strip()  # remove extra spaces
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    st.bar_chart(genre_counts)

    st.divider()

    # --- Films watched per month ---
    st.subheader("Films Watched Per Month")
    month_counts = {}
    for film in watched:
        date_str = film.get("watched_date")
        if date_str:  # only count films that have a saved date
            month = date_str[:7]  # e.g. "2026-09" from "2026-09-07"
            month_counts[month] = month_counts.get(month, 0) + 1

    if month_counts:
        st.bar_chart(month_counts)
    else:
        st.caption("No watch dates recorded yet — this will fill in as you watch more films.")
# ---------- MAIN APP ----------

def main():
    st.set_page_config(page_title="My Film Diary", page_icon="🎬", layout="centered")
    st.title("🎬 My Film Diary")
    st.caption("Your personal film wishlist and diary")

    films = load_films()

    page = st.sidebar.radio(
        "Navigate",
        ["🎬 Wishlist", "✅ Mark as Watched", "📖 My Diary", "📊 Statistics"]
    )

    if page == "🎬 Wishlist":
        page_wishlist(films)
    elif page == "✅ Mark as Watched":
        page_mark_watched(films)
    elif page == "📖 My Diary":
        page_diary(films)
    elif page == "📊 Statistics":
        page_statistics(films)



main()

