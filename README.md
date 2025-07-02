# 🎬 Movie Recommender System

A content-based movie recommender app built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. This application helps users discover similar movies based on their selected or searched title. It features genre filtering, dark/light mode switching, and two ways to get recommendations: via dropdown or search bar.

---

## ✨ Features

- 🎭 **Genre Filtering** — Narrow recommendations to specific genres.
- 🎥 **Dropdown Selection** — Pick a movie from a list.
- 🔍 **Search by Title** — Type a movie name to get results.
- 📈 **Content-Based Filtering** — Uses TF-IDF vectorization and cosine similarity.
- ✅ **Clean & Responsive UI** — Powered by Streamlit.

---

##  How It Works

The app uses a TF-IDF vectorizer to convert movie overviews and genres into numerical form. Then, it calculates cosine similarity between movies to find and recommend the most similar titles.

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```
### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Download Dataset
```
Download the TMDB dataset from Kaggle:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Rename tmdb_5000_movies.csv to movies.csv and place it in the data/ folder:
project/
├── data/
│   └── movies.csv
```
### 5. Run the App
```bash
streamlit run app.py
```



📂 Project Structure
movie-recommender-system/
├── app.py
├── recommender.py
├── data/
│   └── movies.csv
├── requirements.txt
├── README.md
