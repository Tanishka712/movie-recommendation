Here’s a clean and simple `README.md` file for your **Movie Recommendation System** GitHub repository:

---

## 🎬 Movie Recommendation System

This project is a **content-based movie recommender system** built using **Streamlit** and **Scikit-learn**. It recommends similar movies based on textual features like overview and genre, and displays movie posters fetched using the **TMDb API**.

---

### 🚀 Features

* Select a movie and get 5 similar recommendations.
* Displays movie posters using the TMDb API.
* Built using Streamlit for an interactive UI.
* Cosine similarity-based recommendations using movie tags (overview + genre).

---

### 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* TMDb API
* Pickle

---

### 📁 Project Structure

```
├── app.py                     # Streamlit app code
├── movies_list.pkl           # Preprocessed movie DataFrame with 'id', 'title', and 'tags'
├── similarity.pkl            # Cosine similarity matrix
├── data/
│   └── dataset.csv           # Raw dataset containing movie metadata
└── README.md                 # This file
```

---

### ▶️ How to Run

#### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie-recommendation-streamlit.git
cd movie-recommendation-streamlit
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Run the app

```bash
streamlit run app.py
```

---

### 🔑 Setup TMDb API Key

Replace the placeholder API key in `app.py` with your own from [TMDb](https://www.themoviedb.org/):

```python
API_KEY = "your_tmdb_api_key_here"
```

---

### 🧠 How It Works

1. Combines **overview + genre** to form a `tags` field for each movie.
2. Uses `CountVectorizer` with a limit of 10,000 features to vectorize the tags.
3. Computes cosine similarity between all movies.
4. On selecting a movie, retrieves top 5 most similar movies.
5. Fetches posters from TMDb using each movie's `id`.

---

### 📦 Dependencies (`requirements.txt`)

```txt
streamlit
pandas
scikit-learn
requests
```

---

### 📝 Example Dataset (`data/dataset.csv`)

Should contain at least these columns:

* `id` (TMDb movie ID)
* `title`
* `overview`
* `genre` (or combined genre string)

---

### 🧊 Output Example

![UI Screenshot](https://via.placeholder.com/800x400?text=Insert+your+Streamlit+UI+screenshot+here)

---

### 📌 Note

* Make sure your dataset has valid TMDb movie IDs for poster fetching.
* If no poster is available, a placeholder image is shown.

---

Let me know if you want the `requirements.txt` or instructions for deployment on **Streamlit Cloud** as well.
