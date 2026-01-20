🎬 Movie Recommendation System using Machine Learning & Streamlit

A content-based movie recommendation system built using Machine Learning, Python, and Streamlit.
The application recommends movies similar to the one selected by the user and displays their posters using the TMDB API.

🚀 Features

🎥 Content-based movie recommendations

🔍 Select a movie from a dropdown

🧠 Similarity-based recommendations using cosine similarity

🖼️ Movie posters fetched dynamically using TMDB API

❌ Graceful handling of missing posters

⚡ Fast performance using caching

🌐 Interactive web UI with Streamlit

🛠️ Tech Stack

Python

Pandas

Scikit-learn

Streamlit

TMDB API

Pickle

📂 Project Structure
movie-recommendation-system/
│
├── app.py                     # Streamlit application
├── model/
│   ├── movie_list.pkl         # Movie dataset
│   └── similarity.pkl         # Similarity matrix
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation

🧠 How It Works

Movie metadata is vectorized.

Cosine similarity is computed between movies.

When a user selects a movie:

The system finds the most similar movies.

Fetches posters using TMDB API.

Skips movies without posters.

Top 5 recommendations are displayed with posters.

🖼️ Poster Handling Logic

Some movies do not have posters on TMDB.

Such movies are skipped automatically.

A fallback poster is used if required.

This ensures a clean UI without broken images.

🔑 TMDB API Setup

Create an account on https://www.themoviedb.org/

Go to Settings → API

Generate an API Key (v3 auth)

Replace the API key in app.py:

API_KEY = "your_tmdb_api_key_here"

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py

📦 Requirements

Example requirements.txt:

streamlit
pandas
scikit-learn
requests

💡 Future Improvements

⭐ Show movie ratings

📝 Display movie overview

🎭 Genre-based filtering

☁️ Deploy on Streamlit Cloud

📱 Responsive UI

🧑‍💻 Author

Gurjas Singh
Machine Learning Enthusiast | Python Developer

📜 License

This project is for educational purposes.
Free to use and modify.
