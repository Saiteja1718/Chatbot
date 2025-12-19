[![DOI](https://zenodo.org/badge/582718021.svg)](https://zenodo.org/doi/10.5281/zenodo.12507163)

<h1 align="center">Diet Recommendation System</h1>
<div align= "center"><img src="Assets/logo_img1.jpg" />
  <h4>A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.</h4>
</div>

# Diet-Recommendation-System

## :bookmark_tabs:Table of contents
* [General info](#general-info)
* [Development](#development)
* [Technologies](#technologies)
* [Setup](#setup)

## :scroll: General info
### Motivation
People from all around the world are getting more concerned in their health and way of life in today's modern environment. However, avoiding junk food and exercising alone are insufficient; we also need to eat a balanced diet. We can live a healthy life with a balanced diet based on our height, weight, and age. Your diet can help you achieve and maintain a healthy weight, lower your chance of developing chronic diseases (including cancer and heart disease), and improve your general health when combined with physical activity. Nevertheless, there is a little SOTA project on food/diet recommendation system. Therefore I got the idea to build a content-based recommendation system for this purpose using machine learning. 
### What is a food recommendation engine?
A food recommendation engine using a content-based approach is an important tool for promoting healthy eating habits. This type of engine uses information about the nutritional content and ingredients of foods to make personalized recommendations to users. One of the key advantages of a content-based approach is that it takes into account an individual's dietary restrictions and preferences, such as allergies or food preferences. By providing users with tailored recommendations, a content-based food recommendation engine can help them make better choices about what to eat and improve their overall health. Additionally, by recommending a variety of healthy foods, it can also help users to discover new and nutritious options, expand their dietary horizons and overcome food boredom. All these can lead to a better and well-rounded diet, which can have a positive impact on long-term health outcomes.

### What is a content-based recommendation engine?
A content-based recommendation engine is a type of recommendation system that uses the characteristics or content of an item to recommend similar items to users. It works by analyzing the content of items, such as text, images, or audio, and identifying patterns or features that are associated with certain items. These patterns or features are then used to compare items and recommend similar ones to users.
<div align= "center"><img src="Assets/content_based_img.webp" /></div>

### Why content-based approach?

* No data from other users is required to start making recommendations.
* Recommendations are highly relevant to the user.
* Recommendations are transparent to the user.
* You avoid the “cold start” problem. 
* Content-based filtering systems are generally easier to create.

### Challenges of content-based approach
* There’s a lack of novelty and diversity.
* Scalability is a challenge.
* Attributes may be incorrect or inconsistent. 

## :computer:Development
### Model developement
The recommendation engine is built using Nearest Neighbors alogrithm which is an unsupervised learner for implementing neighbor searches. It acts as a uniform interface to three different nearest neighbors algorithms: BallTree, KDTree, and a brute-force algorithm based on routines in sklearn.metrics.pairwise. For our case, we used the brute-force algorithm using cosine similarity due to its fast computation for small datasets.

$$cos(theta) = (A * B) / (||A|| * ||B||)$$

### Dataset
I used Food.com kaggle dataset Data with over 500,000 recipes and 1,400,000 reviews from Food.com. Visit this [kaggle](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews?select=recipes.csv) link for more details.
### Backend Developement
The application is built using the FastAPI framework, which allows for the creation of fast and efficient web APIs. When a user makes a request to the API (user data,nutrition data...) the model is used to generate a list of recommended food similar/suitable to his request (data) which are then returned to the user via the API.

### Frontend Developement

The application's front-end is made with Streamlit. Streamlit is an open source app framework in Python language. It helps to create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc. For our case the front-end is composed of three web pages. The main page is Hello.py which is a welcoming page used to introduce you to my project. The side bar on the left allows the user to navigate too the automatic diet recommendation page and the custom food recommendation page. In the diet recommendation page the user can fill information about his age,weight,height.. and gets a diet recommendation based on his information. Besides, the custom food recommendation allows the user to specify more his food preferency using nutritional values.

### Deployement using Docker
#### Why Docker?
By using Docker, you can ensure that the environment in which the application is exactly the same as the environment in which it was built, which can help prevent unexpected issues and improve model performance. Additionally, Docker allows for easy scaling and management of the deployment, making it a great choice for larger machine learning projects.
#### Docker-Compose
My project is composed of different services (frontend,API). Therefore, our application should run on multiple containers. With the help of Docker-compose we can share our application using the yaml file that define the services that runs together.

### Project Architecture

<div align= "center"><img src="Assets/Architecture_diagram.png" width="600" height="400"/></div>


## :rocket: Technologies
The project is created with:

- **Language & Core**
  - **Python**: 3.10.8
- **Frontend**
  - **Streamlit**: 1.16.0
  - **streamlit-echarts**: 1.24.1
- **Machine Learning & Data**
  - **scikit-learn**: 1.1.3 (Nearest Neighbors recommender)
  - **Pandas**: 1.5.1
  - **NumPy**: 1.24.1
- **APIs & Backend**
  - **FastAPI**: 0.88.0 (optional REST API layer)
  - **Uvicorn**: 0.20.0 (ASGI server)
- **LLM & NLP**
  - **transformers** (Hugging Face)
  - **PyTorch (torch)**
  - **accelerate**
- **Web & Utilities**
  - **requests**
  - **beautifulsoup4** (for recipe image lookup)
- **DevOps**
  - **Docker** & **docker-compose** (optional containerized deployment)

![](https://img.icons8.com/color/48/null/python--v1.png)![](https://img.icons8.com/color/48/null/numpy.png)![](Assets/streamlit-icon-48x48.png)![](Assets/fastapi.ico)![](Assets/scikit-learn.ico) ![](https://img.icons8.com/color/48/null/pandas.png)

## :whale: Setup

### Run it locally (Python)

#### 1. Clone the repo

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd Diet-Recommendation-System-main
```

#### 2. Create and activate a virtual environment (recommended)

Windows (PowerShell):

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

#### 3. Install dependencies

From the project root:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs Streamlit, scikit-learn, the local recommendation engine, and the LLM helpers.

#### 4. Start the Streamlit application

```bash
cd Streamlit_Frontend
streamlit run Hello.py
```

Then open `http://localhost:8501` in your browser and use:

- `💪 Diet Recommendation` for automatic diet plans
- `🔍 Custom Food Recommendation` for macro-targeted recipes
- `🍽️ Meal Planner` for multi-day AI meal plans with budgets and shopping lists

> Note: The recommendation engine loads recipes from `Data/dataset_enhanced.csv`.  
> This file is included in the repo and is required for recommendations to work.

### Optional: Run with Docker Compose

If you prefer containers, you can still run the original multi-service setup:

```bash
docker-compose up -d --build
```

Then open `http://localhost:8501`. You need Docker Desktop and docker‑compose installed for this option.

## Dynamic images (deployment note)

This project supports **dynamic recipe images**.

- **Recommended (reliable on Streamlit Cloud + Docker/VPS)**: Set an Unsplash API key so the server can fetch images and embed them directly.
  - Create an Unsplash app and get an access key: `https://unsplash.com/developers`
  - Set `UNSPLASH_ACCESS_KEY`:
    - **Docker/VPS**: export it on the server before starting compose (or add it to your compose env).
    - **Streamlit Cloud**: add it in the app’s **Secrets**.

If `UNSPLASH_ACCESS_KEY` is not set, the app falls back to `source.unsplash.com`, which may be rate-limited/blocked in some deployments.

## Citation
```
@software{narjis_2024_12507829,
  author       = {Narjis, Zakaria},
  title        = {Diet recommendation system},
  month        = jun,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v1.0.1},
  doi          = {10.5281/zenodo.12507829},
  url          = {https://doi.org/10.5281/zenodo.12507829}
}
```
