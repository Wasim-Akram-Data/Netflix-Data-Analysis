# 🎬 Netflix Data Analysis (EDA Project)

<img width="742" height="495" alt="netflix" src="https://github.com/user-attachments/assets/cdb1af13-3c24-4e77-afd7-940561be7737" />

## 📌 Project Overview
This project performs Exploratory Data Analysis (EDA) on the Netflix dataset using Python.  
The goal is to analyze Netflix movies and TV shows and extract useful insights using data visualization.

---

## 📊 Dataset Information
The dataset contains information about Netflix titles such as:
- Title
- Type (Movie / TV Show)
- Director
- Cast
- Country
- Date Added
- Rating
- Duration
- Genres

---

## 🎯 Objectives
- Handle missing values in dataset  
- Analyze Movies vs TV Shows distribution  
- Find top countries producing Netflix content  
- Identify most popular genres  
- Analyze yearly content addition trend  
- Find longest movies  

---

## 🛠️ Technologies Used
- Python 🐍  
- Pandas  
- NumPy  
- Matplotlib  

---

## 📈 Analysis Performed

### 1. Data Cleaning
Missing values filled in:
- director → "Unknown"  
- cast → "Not Available"  
- country → "Unknown"  
- rating → "Not Rated"  

---

### 2. Content Type Analysis
Compared number of Movies and TV Shows on Netflix.

---

### 3. Country Analysis
Identified top 10 countries producing Netflix content.

---

### 4. Genre Analysis
Extracted and analyzed most common genres.

---

### 5. Yearly Trend Analysis
Visualized how Netflix content was added over the years.

---

### 6. Movie Duration Analysis
Found top 10 longest movies.

---

## 📊 Visualizations
The project includes:
- Bar charts (Movies vs TV Shows, Countries, Genres)  
- Line chart (Yearly trend of content added)

---

## 🚀 How to Run This Project

```bash
pip install pandas numpy matplotlib
python main.py

📁 Project Structure
Netflix-Data-Analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── main.py
├── requirements.txt
├── README.md

📌 Conclusion
This project helps in understanding Netflix content distribution, trends, and patterns using basic data analysis techniques in Python.

⭐ Author
Wasim Akram
