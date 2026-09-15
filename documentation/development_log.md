# Development Log

This document records the development process of my Film Diary project.

## Development Stages
- First Prototype: first I built a very simple base using Streamlit with three pages (Wishlist, Mark as Watched and Diary).
- Class Presentation: I presented my project idea in class and got feedback, which I used to integrate and add an external API (OMDb API) to get film data automatically. This was probably the most important integration and step.
- JSON: Realized that the data was not stored in between sessions, so I consulted Chat GPT how I could handle that problem and it suggested adding a local JSON storage (films.json), which also helped with duplicate-prevention when adding films.
- Statistics Feature: I knew I had to make my application a bit stronger and wanted to add a statistics page, showing total films watched, average personal rating and a genre breakdown chart. This required adding a watched_date field, however that is still to be fixed properly.
- Styling: The white Streamlit seemed a bit boring and I wanted to give the app a cinematic aesthetic and used .streamlit/config.toml as well as custom CSS which I tried to inject via st.markdown(unsafe_allow_html=True), but that layer did not work out as intended and given the deadline and limited time, I decided to deprioritize it.
- Poster Preview: I noticed how when searching a film I always had to type in the title and then immediately searched AND added it to the wishlist. So with adding the Poster Preview I tried to give it an extra step so that before a film is added to the wishlist, you can confirm that that is the film you mean.
- Friends and Family: I let my friends and family try out the application and together we tested mostly if it is user-friendly. While the feedback was generally positive, I learned quite a lot what could be added in the future and be improved.
- Robustness Improvements: Added try/except error handling so that the app fails in a bit of a nicer way, instead of just crashing completely. With that there comes a clear message if the OMDb API cannot be reached and there is also a protection against a corrupted films.json file on startup.
