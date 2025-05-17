# Iris Dataset: Exploratory Data Analysis and Visualization

This Python project provides an in-depth **Exploratory Data Analysis (EDA)** of the classic **Iris dataset**. It calculates statistics and generates insightful visualizations such as **box plots**, **histograms**, and a **scatter plot matrix** to help understand the distribution, relationships, and variation across flower measurements.

This is a great starting point for beginners interested in data science, statistics, or machine learning using Python, `pandas`, and `matplotlib`.

---

## Project Files

| File               | Description |
|--------------------|-------------|
| `IrisDataStats.py` | Python script that loads the dataset, prints summary stats, and generates plots |
| `iris.csv`         | Raw dataset (without headers) with measurements and species class |
| `box.png`          | Generated box plots for each feature |
| `hist.png`         | Generated histograms for feature distributions |
| `matrix.png`       | Generated scatter plot matrix showing feature relationships |

---

## About the Dataset

The **Iris dataset** is one of the most well-known datasets in data science and was first introduced by **Ronald A. Fisher** in 1936. It contains measurements for **150 iris flowers** from three different species:

- *Iris setosa*
- *Iris versicolor*
- *Iris virginica*

Each row (sample) contains:
1. **Sepal length** (cm)
2. **Sepal width** (cm)
3. **Petal length** (cm)
4. **Petal width** (cm)
5. **Class** (species name)

This dataset is widely used for **classification**, **clustering**, and **visualization** tutorials.

---

## What the Script Does (`IrisDataStats.py`)

### 1. Load the Dataset

- The script reads `iris.csv` using `pandas.read_csv()`.
- It assigns column names manually since the dataset lacks headers.

### 2. Display Dataset Summary

The script prints:
- Shape (rows × columns)
- First 20 rows of the dataset (`head`)
- Descriptive statistics (`mean`, `min`, `max`, `std`, quartiles, etc.)
- Class distribution (how many samples per species)

### 3. Generate Visualizations

Each visualization helps answer different questions:

#### Box Plots (`box.png`)
- Purpose: Examine **spread**, **center**, and **outliers** for each feature.
- Subplots: 4 (one per numeric feature)
- Insight: Quickly detect data skew and compare variance across features.

#### Histograms (`hist.png`)
- Purpose: Understand the **distribution** of values (normal, skewed, bimodal).
- Subplots: 4 (one per numeric feature)
- Insight: Reveals feature shapes, clustering, and separability potential.

#### Scatter Matrix (`matrix.png`)
- Purpose: Explore **pairwise correlations** between all numeric features.
- Layout: 4x4 grid with scatter plots and histograms on the diagonal.
- Insight: Helps spot which features are strongly correlated (good for ML).

---

## How to Run the Project

### Requirements

Make sure you have the following Python packages installed:

```bash
pip install pandas matplotlib
