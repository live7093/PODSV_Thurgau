# app/analysis_utils.py

import pandas as pd
import plotly.express as px
import streamlit as st

def df_old_new(df_new: pd.DataFrame, df_old: pd.DataFrame) -> pd.DataFrame:
    """
    Merge and clean animal data from two DataFrames (new + old).
    Only keeps rows from years 2023 and 2024.
    """
    df = pd.concat([df_new, df_old], ignore_index=True)
    df = df[df["jahr"].isin([2023, 2024])]
    return df

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize location column to 'gemeinde', depending on source format.
    """
    if "standortgemeinde" in df.columns:
        df = df.rename(columns={"standortgemeinde": "gemeinde"})
    elif "gemeindename" in df.columns:
        df = df.rename(columns={"gemeindename": "gemeinde"})
    return df

def filter_by_years_and_gemeinden(df: pd.DataFrame, years: list, gemeinden: list) -> pd.DataFrame:
    """
    Filter the DataFrame by selected years and Gemeinden.
    """
    if years:
        df = df[df["jahr"].isin(years)]
    if gemeinden:
        df = df[df["gemeinde"].isin(gemeinden)]
    return df

def cleanup_guggus(df, animals_df, plants_df):
    """
    Keeps only rows from df where 'gemeinde' exists in both animals_df and plants_df.
    """
    common_gemeinden = set(animals_df["gemeinde"]) & set(plants_df["gemeinde"])
    return df[df["gemeinde"].isin(common_gemeinden)].copy()

#----------------------------------------------------------------------- Plotting functions -------------------------------------------------------------------------------------------------------------------------

def plot_animal_chart_by_gemeinde(df: pd.DataFrame, gemeinde: str):
    sub_df = df[df["gemeinde"] == gemeinde]
    if sub_df.empty:
        return st.warning(f"No animal data for {gemeinde}")
    
    animal_agg = (
        sub_df.groupby(["kategorie", "jahr"])["durchschnittsbestand_stueck"]
        .sum()
        .reset_index()
    )
    animal_agg["jahr"] = animal_agg["jahr"].astype(str)
    max_display_value = 1.2 * animal_agg["durchschnittsbestand_stueck"].median()

    fig = px.bar(
        animal_agg,
        x="kategorie",
        y="durchschnittsbestand_stueck",
        color="jahr",
        barmode="group",
        title=f"🐄 Animal Stock in {gemeinde}",
        labels={"kategorie": "Category", "durchschnittsbestand_stueck": "Total Stock", "jahr": "Year"},
        text_auto=".2s",
        width=900,
        height=500
    )
    fig.update_layout(
        yaxis=dict(range=[0, max_display_value]),
        xaxis_tickangle=-45,
        legend_title_text="Year",
        legend=dict(x=1.02, y=1, xanchor="left", yanchor="top")
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_plant_chart_by_gemeinde(df: pd.DataFrame, gemeinde: str):
    sub_df = df[df["gemeinde"] == gemeinde].copy()
    if sub_df.empty:
        return st.warning(f"No plant data for {gemeinde}")
    
    sub_df["wert"] = sub_df.apply(
        lambda row: row["landw_nutzflaeche_in_aren"] if pd.notna(row["landw_nutzflaeche_in_aren"]) else row["anzahl_baeume"],
        axis=1
    )
    plant_agg = (
        sub_df.groupby(["kultur_bezeichnung", "jahr"])["wert"]
        .sum()
        .reset_index()
    )
    plant_agg["jahr"] = plant_agg["jahr"].astype(str)
    max_display_value = 1.2 * plant_agg["wert"].median()

    fig = px.bar(
        plant_agg,
        x="kultur_bezeichnung",
        y="wert",
        color="jahr",
        barmode="group",
        title=f"🌳 Plant Cultivation in {gemeinde}",
        labels={"kultur_bezeichnung": "Culture", "wert": "Area (aren) or Tree Count", "jahr": "Year"},
        text_auto=".2s",
        width=900,
        height=500
    )
    fig.update_layout(
        yaxis=dict(range=[0, max_display_value]),
        xaxis_tickangle=-45,
        legend_title_text="Year",
        legend=dict(x=1.02, y=1, xanchor="left", yanchor="top")
    )
    st.plotly_chart(fig, use_container_width=True)