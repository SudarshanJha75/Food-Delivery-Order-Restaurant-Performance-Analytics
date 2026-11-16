FOOD DELIVERY ORDER & RESTAURANT PERFORMANCE ANALYTICS
======================================================

1. ABOUT THE PROJECT
--------------------
This project is about analysing food delivery orders and restaurant
performance in Bengaluru.

It uses Python to clean and analyse order data. It also includes charts,
a machine learning model to estimate delivery time, SQL files, and a
Streamlit dashboard.

Note: The sample dataset included with this project is synthetic
(sample data created for practice). It is not real Swiggy or Zomato
customer or order data.

2. PROJECT FEATURES
-------------------
- Load and clean food delivery data.
- Analyse orders, revenue, restaurants, cuisines, and delivery times.
- Create charts from the data.
- Train a machine learning model to estimate delivery time.
- View results in an interactive Streamlit dashboard.
- Find example database tables and SQL analysis queries.

3. TECHNOLOGIES USED
--------------------
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Streamlit
- Plotly
- MySQL (SQL files are provided)

4. PROJECT FOLDER
-----------------
Food_Delivery_Analytics/
    dashboard/       Dashboard application
    dataset/         Raw and processed datasets
    models/           Saved machine learning model
    notebooks/        Data exploration notes
    reports/          Project notes and documentation
    sql/              Database schema and SQL queries
    src/              Data cleaning, analysis, and ML code
    main.py           Main data processing and analysis file
    requirements.txt  Required Python libraries

5. REQUIREMENTS
---------------
- Python installed on your computer
- Visual Studio Code (recommended)
- Internet connection for installing Python libraries
- MySQL Server (only if you want to run the SQL database part)

6. HOW TO RUN THE PROJECT
-------------------------
Step 1: Open the Food_Delivery_Analytics folder in VS Code.

Step 2: Open the VS Code terminal.

Step 3: Create a virtual environment:

    python -m venv .venv

Step 4: Activate the virtual environment in Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Step 5: Install the required libraries:

    pip install -r requirements.txt

Step 6: Run the main project:

    python main.py

This runs the data processing and analysis code. It also creates
processed data and analysis charts.

7. HOW TO TRAIN THE MACHINE LEARNING MODEL
------------------------------------------
Run this command from the main project folder:

    python src/train_model.py

The script trains a model to estimate delivery time and saves it in
the models folder.

8. HOW TO OPEN THE DASHBOARD
----------------------------
Run:

    streamlit run dashboard/app.py

Streamlit will show a local address in the terminal, usually:

    http://localhost:8501

Open that address in your web browser to use the dashboard.

9. SQL FILES
------------
The sql folder contains:

- schema.sql: example database and table structure.
- analysis_queries.sql: example SQL queries for analysing orders,
  revenue, restaurants, and delivery information.

To run these SQL files, MySQL Server must be installed and running,
and you must be able to log in to your MySQL account. The SQL files
are provided separately; the Python dashboard does not require a
successful MySQL connection to run.

10. LIMITATIONS
---------------
- The included dataset is synthetic and is for learning and project
  demonstration.
- Results from sample data should not be treated as actual Bengaluru
  food delivery market statistics.
- The delivery-time model is trained on the included sample data.
  Its predictions are not guaranteed to represent real delivery times.

11. PROJECT PURPOSE
-------------------
This project was created for learning data science concepts such as
data cleaning, data analysis, data visualisation, SQL, machine learning,
and dashboard development.

12. AUTHOR
----------
Name:Sudarshan Kumar Jha
Course: B.Tech
Project: Food Delivery Order & Restaurant Performance Analytics
