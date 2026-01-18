# 🇲🇦 Morocco E-Commerce Data Analysis

A professional **data cleaning and exploratory data analysis (EDA)** project using a real-world Moroccan e-commerce dataset.  
This project simulates the work of a **junior data analyst**, from raw data ingestion to cleaned datasets and business insights.

---

## 🚀 Project Objectives

- 🧹 Clean and prepare raw e-commerce data  
- 📊 Explore sales, revenue, and regional performance  
- 🕒 Analyze time-based trends (monthly revenue)  
- ⚠️ Detect outliers using statistical methods  
- 📦 Deliver a reusable and well-structured data analysis project  

---

## 📂 Dataset

The dataset is provided in **three formats** to simulate real-world scenarios:

- 📄 CSV (`morocco_ecommerce.csv`)  
- 📊 Excel (`morocco_ecommerce.xlsx`)  
- 🔗 JSON (`morocco_ecommerce.json`)  

**Main fields include:**
- Order ID  
- Order & shipping dates  
- Product ID  
- Quantity & unit price  
- Total amount  
- City & region  
- Payment method  

---

## 🧹 Data Cleaning Steps

- Handling missing values (categorical & numerical)
- Removing duplicated rows and duplicated `order_id`s
- Standardizing city names (e.g. *Casa → Casablanca*)
- Converting date columns to `datetime`
- Creating new features: **year, month, weekday**
- Saving a fully cleaned dataset for reuse

---

## 📊 Analysis & Insights

- 📍 Revenue comparison across Moroccan regions  
- 🏆 Top-selling products by total revenue  
- 📈 Monthly average revenue trends  
- ⚠️ Outlier detection using:
  - Interquartile Range (IQR)
  - Z-score method  

---

## 🧠 Concepts & Skills Demonstrated

This project showcases essential **data analysis and data engineering** skills:

- Pandas data manipulation  
- Data cleaning best practices  
- Exploratory Data Analysis (EDA)  
- Grouping & aggregation  
- Time-series analysis  
- Outlier detection  
- Modular Python code  
- Reproducible project structure  

---

## 🗂️ Project Structure

📁 morocco-ecommerce-analysis/
├── 📁 data/
│   ├── 📄 raw/                # Original datasets (CSV, Excel, JSON)
│   └── 📄 processed/          # Cleaned dataset
├── 📁 notebooks/
│   └── 📄 01_data_cleaning_and_eda.ipynb
├── 📁 src/
│   ├── 📄 __init__.py
│   ├── 📄 data_cleaning.py
│   └── 📄 analysis.py
├── 📁 outputs/
│   ├── 📷 figures/            # Saved plots
│   └── 📊 tables/             # Exported statistics
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 LICENSE


---

## 🛠️ Tools & Technologies

- Python 3.8+  
- Pandas  
- NumPy  
- Matplotlib  
- SciPy  
- Jupyter Notebook  

---

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hassan25dev/morocco-ecommerce-analysis.git
   ```
2. **Navigate to the project**
   ```bash
   cd morocco-ecommerce-analysis
    ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Hassan25dev/student-grade-analytics-system.git
   ```
2. Open Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Navigate to the folder:
   ```bash
   cd morocco-ecommerce-analysis\notebooks
   ```
4. Run the script:
   ```bash
   01_data_cleaning_and_eda.ipynb
   ```
5. The cleaned dataset will be saved automatically in:
   ```bash
   data/processed/
   ```

---

## 💡 Future Improvements

- This project demonstrates fundamental Python skills often used in **data analysis** and **backend scripting**:
- Add interactive dashboards with Streamlit
- Build automated data pipelines
- Add customer segmentation (RFM analysis)
- Perform predictive sales analysis  

---


## 👤 About

**Author:** HASSANE AMANAD  

**Context:**  
Academic & portfolio project developed as part of a Data Analysis practice assignment, 
focused on real-world data cleaning and exploration.

**Skills Highlighted:**  
- Data cleaning & preprocessing
- Exploratory data analysis 
- Time-series feature engineering 
- Professional project structuring 
- Clear technical documentation  

**License:** MIT  
**GitHub:** [@Hassan25dev](https://github.com/Hassan25dev)
