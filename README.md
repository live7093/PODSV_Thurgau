# Cultivated Animals & Plants in Thurgau — Dashboard

This project provides a Streamlit dashboard to explore cultivated animals and plants in the canton of Thurgau, Switzerland, based on official agricultural data for our project work in the Project-oriented Digital Storytelling and Visualisation FS25 AD23 module. 
This project was conducted by: Florian Vollmer, Ruben Schmid, Melanie Rohrbacher and Nicola Noger

The app allows you to:
- Filter by year and municipality (Gemeinde)
- View separate animal and plant statistics
- See summarized trends in an overview tab
- Geographical visualizations

## How to Run the App

### 1. Install required packages
Make sure Streamlit is installed:
```bash
pip install streamlit 
pip install plotly
```
The rest of the liberarys used should be in the installed and tested venv of the module podsv.

### 2. Adjust file paths
Open `App/streamlit_app.py` and set the correct local paths to your CSV files under the data loading section.

### 3. Run the app
In your terminal, navigate to the project folder and run:

```bash
streamlit run DataVisualization/App/streamlit_app.py
```

Then open the provided local URL (usually `http://localhost:8501`) in your browser.

## Project Structure

```
DataVisualization/
├── App/
│   ├── streamlit_app.py       # Main Streamlit app (UI)
│   ├── analysis_utils.py      # Reusable logic (data cleaning, filtering)
|   ├── municipality.py        # Data of all the municipality's with the coordinates
├── Daten/
│   ├── Thurgau_Animals2024.csv
│   ├── Thurgau_AnimalsOld.csv
│   ├── Thurgau_Trees.csv
├── Notebooks/
│   └── Exploration.ipynb      # Jupyter notebook for prototyping logic and explanation on what we did how
└── README.md
```
