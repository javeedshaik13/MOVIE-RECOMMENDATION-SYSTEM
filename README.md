# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System that uses **Content-Based Filtering** and **Natural Language Processing (NLP)** to recommend similar movies. The system analyzes movie metadata including overview, genres, keywords, cast, and crew to suggest movies with similar characteristics.

## 📋 Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Models & Algorithms](#models--algorithms)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [API Configuration](#api-configuration)
- [Screenshots](#screenshots)

## ✨ Features

- **Content-Based Recommendations**: Get 5 similar movie recommendations based on your selection
- **Movie Posters**: Visual display of recommended movies with posters fetched from TMDB API
- **Interactive UI**: User-friendly Streamlit web interface
- **Fast Performance**: Pre-computed similarity matrix for instant recommendations
- **Comprehensive Dataset**: Uses TMDB 5000 Movies dataset

## 🛠 Tech Stack

### Programming Language
- **Python 3.12.7**

### Libraries & Frameworks
- **Streamlit** - Web application framework for the UI
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning algorithms
- **Requests** - HTTP library for API calls
- **AST** - Abstract Syntax Trees for parsing string representations

### Data Source
- **TMDB API** - The Movie Database API for fetching movie posters
- **TMDB 5000 Movies Dataset** - Movie metadata from Kaggle

## 🤖 Models & Algorithms

### 1. **TF-IDF Vectorizer** (Term Frequency-Inverse Document Frequency)
- Converts text data into numerical vectors
- Parameters used:
  - `max_features=5000` - Limits vocabulary to top 5000 words
  - `stop_words='english'` - Removes common English stop words

### 2. **Cosine Similarity**
- Measures similarity between movie vectors
- Range: 0 (completely different) to 1 (identical)
- Formula: `cosine_similarity = (A · B) / (||A|| × ||B||)`

### 3. **Content-Based Filtering**
- Recommends items similar to what user likes
- Based on item features rather than user behavior

## 🔍 How It Works

### Step 1: Data Preprocessing
1. Load TMDB movies and credits datasets
2. Merge datasets on movie title
3. Select relevant features: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`
4. Handle missing values by dropping rows with null data

### Step 2: Feature Engineering
1. Parse JSON-like strings in columns using `ast.literal_eval()`
2. Extract genre names from genre objects
3. Extract top 3 cast members
4. Extract director name from crew
5. Remove spaces from multi-word entries (e.g., "Science Fiction" → "ScienceFiction")
6. Combine all features into a single `tags` column

### Step 3: Text Vectorization
1. Convert `tags` column into TF-IDF vectors
2. Create a 5000-dimensional feature space
3. Each movie is represented as a numerical vector

### Step 4: Similarity Computation
1. Calculate cosine similarity between all movie pairs
2. Create a similarity matrix (4806 × 4806)
3. Save the matrix for fast retrieval

### Step 5: Recommendation Generation
1. User selects a movie from dropdown
2. System finds the movie's index in the dataset
3. Retrieves similarity scores for that movie
4. Sorts movies by similarity score (descending)
5. Returns top 5 most similar movies (excluding the selected movie)
6. Fetches movie posters from TMDB API

### Step 6: Display Results
1. Shows recommended movie titles
2. Displays movie posters in a 5-column grid layout
3. Interactive web interface built with Streamlit

## 📁 Project Structure

```
MOVIE-RECOMMENDATION-SYSTEM/
│
├── app.py                          # Main Streamlit application (improved version)
├── main.py                         # Alternative Streamlit application
├── Movie_recommender_system.ipynb  # Jupyter notebook for model training
│
├── movie_dict.pkl                  # Pickled movie dataset with poster paths
├── movie_list.pkl                  # Pickled movie dataset (alternative)
├── similarity.pkl                  # Pre-computed similarity matrix
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # License file
├── .gitignore                      # Git ignore file
│
└── venv/                           # Virtual environment (not tracked in git)
```

### File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Enhanced Streamlit web application with caching and error handling |
| `main.py` | Alternative Streamlit app (basic version) |
| `Movie_recommender_system.ipynb` | Complete workflow: data preprocessing, feature engineering, model training |
| `movie_dict.pkl` | Serialized DataFrame containing movie data with poster paths |
| `movie_list.pkl` | Alternative serialized movie data |
| `similarity.pkl` | Pre-computed cosine similarity matrix (4806×4806) |
| `requirements.txt` | List of Python package dependencies |

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for TMDB API)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/MOVIE-RECOMMENDATION-SYSTEM.git
cd MOVIE-RECOMMENDATION-SYSTEM
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Get TMDB API Key
1. Visit [TMDB](https://www.themoviedb.org/)
2. Create a free account
3. Go to Settings → API → Create API Key
4. Copy your API key
5. Replace the API key in `app.py`:
   ```python
   API_KEY = "your_api_key_here"
   ```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 Usage

1. **Launch the Application**: Run `streamlit run app.py`
2. **Select a Movie**: Choose a movie from the dropdown menu
3. **Get Recommendations**: Click the "Get Recommendations" button
4. **View Results**: See 5 similar movies with their posters

### Example Workflow
```
1. Select "The Dark Knight" from dropdown
2. Click "Get Recommendations"
3. View recommendations:
   - The Dark Knight Rises
   - Batman Begins
   - Watchmen
   - Man of Steel
   - The Prestige
```

## 🔑 API Configuration

### TMDB API
- **Purpose**: Fetch movie poster images
- **Rate Limit**: Free tier allows 40 requests per 10 seconds
- **Implementation**: 
  - API calls are cached to reduce requests
  - Timeout set to 5 seconds
  - Fallback to placeholder image if API fails

### API Key Setup
Replace the API key in `app.py`:
```python
API_KEY = "df5d969bdb3fd702825dc3a59d32676e"  # Replace with your own
```

## 📊 Dataset Information

- **Source**: TMDB 5000 Movies Dataset (Kaggle)
- **Movies**: ~4,806 movies
- **Features Used**:
  - Title
  - Overview (plot summary)
  - Genres
  - Keywords
  - Cast (top 3 actors)
  - Crew (director)
  - Movie ID (for poster fetching)

## 🧪 Model Performance

- **Similarity Matrix Size**: 4806 × 4806
- **Feature Space**: 5000 dimensions (TF-IDF)
- **Preprocessing Time**: ~2-3 minutes
- **Recommendation Time**: < 100ms (instant)
- **Accuracy**: Content-based (no ground truth for evaluation)

## 🔄 Workflow Diagram

```
User Input (Movie Selection)
         ↓
Find Movie Index
         ↓
Retrieve Similarity Scores
         ↓
Sort by Similarity (Descending)
         ↓
Select Top 5 Movies
         ↓
Fetch Posters from TMDB API
         ↓
Display Results in UI
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: `FileNotFoundError: movie_dict.pkl not found`
- **Solution**: Ensure pickle files are in the same directory as `app.py`

**Issue**: Posters not loading
- **Solution**: Check your TMDB API key is valid and you have internet connection

**Issue**: `ModuleNotFoundError`
- **Solution**: Install all dependencies: `pip install -r requirements.txt`

**Issue**: Streamlit command not found
- **Solution**: Ensure streamlit is installed: `pip install streamlit`

## 📝 Future Enhancements

- [ ] Add collaborative filtering for hybrid recommendations
- [ ] Implement user ratings and favorites
- [ ] Add movie search functionality
- [ ] Include movie details (year, rating, runtime)
- [ ] Deploy to cloud (Heroku/Streamlit Cloud)
- [ ] Add more filtering options (genre, year, rating)
- [ ] Implement pagination for large result sets
- [ ] Add movie trailers integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- TMDB for providing the movie database and API
- Kaggle for the TMDB 5000 Movies dataset
- Streamlit for the amazing web framework
- Scikit-learn for machine learning tools

## 📧 Contact

For any queries or suggestions, please reach out:
- Email: your.email@example.com
- Project Link: [https://github.com/yourusername/MOVIE-RECOMMENDATION-SYSTEM](https://github.com/yourusername/MOVIE-RECOMMENDATION-SYSTEM)

---

⭐ If you found this project helpful, please give it a star!
