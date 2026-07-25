# 📊 ETL Pipeline Project

## 📌 Project Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline using Python and Pandas.

### Technologies Used
- Python
- Pandas
- CSV
- VS Code

---

## 📂 Project Structure

```
ETL-Pipeline/
│── superstore_sales.csv
│── cleaned_superstore_sales.csv
│── etl_pipeline.py
│── requirements.txt
│── README.md
```

---

## 🚀 ETL Process

### Step 1: Extract
- Read Superstore Sales dataset using Pandas.

### Step 2: Transform
- Remove duplicate rows.
- Check missing values.
- Create a new column `Sales_per_Item`.

### Step 3: Load
- Save the cleaned dataset as `cleaned_superstore_sales.csv`.

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python etl_pipeline.py
```

---

## 📷 Output

![Output](output.png)


---

## 👨‍💻 Author

**Pranjal Dhamane**
