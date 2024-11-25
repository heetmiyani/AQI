# Air Quality Index (AQI) Prediction

This repository contains the implementation of an **Air Quality Index (AQI) Prediction** project using unsupervised machine learning techniques such as Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA). The project analyzes AQI data to understand emission distributions, identify influential gaseous components, and provide insights into air quality trends.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Data Preparation](#data-preparation)
- [Methodology](#methodology)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [References](#references)

---

## Introduction
Air pollution poses significant risks to human health and the environment. This project explores the relationship between pollutants and AQI through data-driven analysis. It compares PCA and LDA for dimensionality reduction and evaluates their effectiveness in understanding emission patterns and clustering AQI data.

---

## Features
1. Dimensionality reduction using PCA and LDA.
2. Exploratory Data Analysis (EDA) to visualize trends in pollutants and their correlations.
3. Insights into seasonal variations in AQI and its components.
4. Clustering based on emission characteristics.

---

## Data Preparation
The dataset used includes real-time AQI data. Key preparation steps include:
1. **Handling Missing Values:** Missing entries replaced with mean/median or dropped for highly sparse columns.
2. **Feature Engineering:** Splitting date columns into months/years for seasonal analysis.
3. **Data Cleaning:** Standardizing and normalizing data for consistency.

---

## Methodology
1. **Exploratory Data Analysis (EDA):**
   - Histogram plots to understand feature distributions.
   - Correlation heatmaps to identify relationships between pollutants.
   - Trend analysis using line and scatter plots.

2. **Dimensionality Reduction:**
   - PCA for maximizing variance while reducing dimensions.
   - LDA for maximizing class separability.

3. **Visualization:**
   - Visualizations of principal components and class clusters.

---

## Results
- **PCA:** Effective in preserving variance and identifying key components affecting AQI.
- **LDA:** Useful for class separation but less effective than PCA for this dataset.

Key findings:
- Temperature is inversely proportional to relative humidity.
- NO2 has the highest maximum concentration, while absolute humidity has the lowest.

---

## Technologies Used
- **Python**: For data processing and analysis.
- **Pandas, NumPy**: For handling datasets and numerical computations.
- **Matplotlib, Seaborn**: For visualization.
- **Scikit-learn**: For PCA and LDA implementations.

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/heetmiyani/AQI.git
   cd AQI
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Run the analysis:
   ```bash
   python main.py
