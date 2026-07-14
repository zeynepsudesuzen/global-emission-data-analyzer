# Global CO₂ Emission Data Analyzer

## Overview
This is a terminal-based Python application designed to analyze, manage, and visualize global CO₂ emissions and population datasets. It reads data from external CSV files and provides a fully functional interface for Database (CRUD) operations, advanced data analysis, and data visualization.

## Features 
* **CRUD Operations:** Create, read, update, and delete country-specific emission records directly through the terminal.
* **Advanced Data Analysis:**
  * Compare emissions between two different countries.
  * Perform year-to-year percentage change analysis for a specific country.
  * Calculate emission intensity (Per-capita CO₂) using population data.
  * Analyze emission trends (decrease/increase) over a 3-year period.
* **Data Visualization:** Generates bar charts to visualize a country's historical CO₂ emissions using `matplotlib`.
* **Robust Error Handling:** Includes `try-except` blocks to prevent system crashes during file loading (`FileNotFoundError`) and invalid user inputs (`ValueError`).

## Technologies & Tools
* **Language:** Python 3.x
* **Libraries:** `matplotlib` (for data visualization)
* **Concepts:** File I/O (CSV), CRUD, Error Handling, Algorithmic Data Filtering

## How to Run
1. Clone this repository to your local machine.
2. Ensure you have `matplotlib` installed:
   ```bash
   pip install matplotlib
   ```
3. Make sure the dataset files (`annual-co2-emissions-per-country.csv` and `population.csv`) are in the same directory as the script.
4. Run the Python script:
   ```bash
   python project.py
   ```
   
## Data Sources & Acknowledgements
The datasets used in this project are open-source and were provided as part of a university assignment. All rights and credits for the original datasets belong to their respective creators and organizations:

**CO₂ Emissions Data:** Global Carbon Budget (2024) – with major processing by Our World in Data. “Annual CO₂ emissions – GCB” [dataset]. Global Carbon Project, “Global Carbon Budget” [original data].

**Population Data:** HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World in Data. “Population (historical)” [dataset]. PBL Netherlands Environmental Assessment Agency, “History Database of the Global Environment 3.3”; Gapminder, “Population v7”; United Nations, “World Population Prospects”; Gapminder, “Systema Globalis” [original data].

## Author
Zeynep - *Software Engineering Student @ Karadeniz Technical University*
* Note: This project was independently developed and coded from scratch as part of my university coursework, demonstrating practical applications of data management and algorithm design.*
