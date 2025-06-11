# app/streamlit_app.py
import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import plotly.graph_objects as go

# Add App/ folder to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import utility functions from analysis_utils.py which was made to clean and prepare the data and not clutter the main app file
from analysis_utils import df_old_new, filter_by_years_and_gemeinden, rename_columns, plot_animal_chart_by_gemeinde, plot_plant_chart_by_gemeinde, cleanup_guggus
from municipality_data import get_municipality_map_data

# ----------------------------------------------------------- Title -------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Thurgau Cultivation Dashboard", layout="wide")

st.markdown(
    """
    <h1 style='color:#007a33; margin-bottom:0;'>Thurgau Agriculture Dashboard</h1>
    <p style='color:#4d4d4d;'>🌾 Cultivated Animals & Plants in 2023/2024</p>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------------- Visually Improvements -------------------------------------------------------------------------------------------------------------------------
st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Wappen_Thurgau_matt.svg/1200px-Wappen_Thurgau_matt.svg.png",
    width=300,
    
)


# ----------------------------------------------------------- Load data ------------------------------------------------------------------------------------------
# animals_2024 = pd.read_csv(
#     '/Users/rubenschmid/Desktop/ZHAW/4.Semester/PoSTV/Project/DataVisualization/Daten/Thurgau_Animals2024.csv',
#     delimiter=';'
# )
# animals_old = pd.read_csv(
#     '/Users/rubenschmid/Desktop/ZHAW/4.Semester/PoSTV/Project/DataVisualization/Daten/Thurgau_AnimalsOld.csv',
#     delimiter=';'
# )
# plants_df = pd.read_csv(
#     '/Users/rubenschmid/Desktop/ZHAW/4.Semester/PoSTV/Project/DataVisualization/Daten/Thurgau_Trees.csv',
#     delimiter=';'
# )

# Get the current directory (where streamlit_app.py is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the "Daten" folder (assumes it's one level above "app")
data_dir = os.path.join(current_dir, "..", "Daten")

# ----------------------------------------------------------- Load data ------------------------------------------------------------------------------------------
animals_2024 = pd.read_csv(os.path.join(data_dir, "Thurgau_Animals2024.csv"), delimiter=';')
animals_old = pd.read_csv(os.path.join(data_dir, "Thurgau_AnimalsOld.csv"), delimiter=';')
plants_df = pd.read_csv(os.path.join(data_dir, "Thurgau_Trees.csv"), delimiter=';')

# ----------------------------------------------------------- Clean & prepare -------------------------------------------------------------------------------------------------------------------------
animals_df = rename_columns(df_old_new(animals_2024, animals_old))
plants_df = rename_columns(plants_df)

# -----------------------------------------------------------Sidebar filters -------------------------------------------------------------------------------------------------------------------------
st.sidebar.header("🔍 Filter Data")

# Only allow selection of Gemeinden that are present in both datasets
common_gemeinden = sorted(set(animals_df["gemeinde"]) & set(plants_df["gemeinde"]))
years = st.sidebar.multiselect("Select Year(s)", sorted(animals_df["jahr"].unique()), default=[2024])
gemeinden = st.sidebar.multiselect("Select Gemeinde(n)", common_gemeinden)

# ----------------------------------------------------------- Filter both datasets -------------------------------------------------------------------------------------------------------------------------
filtered_animals = filter_by_years_and_gemeinden(animals_df, years, gemeinden)
filtered_plants = filter_by_years_and_gemeinden(plants_df, years, gemeinden)

# ----------------------------------------------------------- Cleanup Guggus -------------------------------------------------------------------------------------------------------------------------
filtered_animals = cleanup_guggus(filtered_animals, filtered_animals, filtered_plants)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------STREAMLIT DASHBOARD-------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------- Tabs -------------------------------------------------------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "🐄 Animals", "🌳 Plants", "Geograhpical overview"])
# ----------------------------------------------------------- Tab1 -------------------------------------------------------------------------------------------------------------------------

with tab1:
    st.subheader("Overview")
    st.write("This dashboard provides an overview of cultivated animals and plants in the selected municipalities and years.")
    st.write("Use the filters in the sidebar to select the desired years and municipalities for analysis.")

    if not years or not gemeinden:
        st.info("Please select at least one year and one Gemeinde in the sidebar.")
    else:
        for gemeinde in gemeinden:
            st.markdown(f"### 📍 {gemeinde}")
            col1, col2 = st.columns(2)
            with col1:
                plot_animal_chart_by_gemeinde(filtered_animals, gemeinde)
            with col2:
                plot_plant_chart_by_gemeinde(filtered_plants, gemeinde)

# ----------------------------------------------------------- Tab2 -------------------------------------------------------------------------------------------------------------------------
with tab2:
    st.subheader("Animal Stock")

    if not years or not gemeinden:
        st.info("Please select at least one year and one Gemeinde in the sidebar.")
    elif filtered_animals.empty:
        st.warning("No animal data for the selected filters.")
    else:
        for gemeinde in gemeinden:
            st.markdown(f"### 🐮 {gemeinde}")
            df_g = filtered_animals[filtered_animals["gemeinde"] == gemeinde]
            st.dataframe(
                df_g[["jahr", "gemeinde", "kategorie", "durchschnittsbestand_stueck"]],
                use_container_width=True
            )

# ----------------------------------------------------------- Tab3 -------------------------------------------------------------------------------------------------------------------------
with tab3:
    st.subheader("Plant Cultivation")

    if not years or not gemeinden:
        st.info("Please select at least one year and one Gemeinde in the sidebar.")
    elif filtered_plants.empty:
        st.warning("No plant data for the selected filters.")
    else:
        plant_df = filtered_plants.copy()
        plant_df["wert"] = plant_df["landw_nutzflaeche_in_aren"].fillna(
            plant_df["anzahl_baeume"]
        )

        for gemeinde in gemeinden:
            st.markdown(f"### 🌳 {gemeinde}")
            df_g = plant_df[plant_df["gemeinde"] == gemeinde]
            st.dataframe(
                df_g[["jahr", "gemeinde", "kultur_bezeichnung", "wert"]],
                use_container_width=True
            )

# ----------------------------------------------------------- Tab4 -------------------------------------------------------------------------------------------------------------------------
# Geopadas bullsh*tery (Yeah I am losing it)
with tab4:
    st.subheader("Geographical Overview")
    st.write("This map shows the municipalities based on coordinate data.")

    if not gemeinden:
        st.info("Please select at least one Gemeinde in the sidebar.")
    else:
        fig = get_municipality_map_data(gemeinden)
        st.plotly_chart(fig, use_container_width=True)