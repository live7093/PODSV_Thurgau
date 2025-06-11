# app/municipality_data.py
import plotly 

municipalities_list = [
    "Aadorf", "Affeltrangen", "Altnau", "Amlikon-Bissegg", "Amriswil", "Appenzell", "Arbon", "Avegno Gordevio", "Basadingen-Schlattingen", "Bauma", "Bellinzona", "Berg (SG)", "Berg (TG)", "Berlingen", "Bettwiesen", "Bichelsee-Balterswil", "Birwinken", "Bischofszell", "Bottighofen", "Braunau", "Brütten", "Bussnang", "Bürglen (TG)", "Centovalli", "Diessenhofen", "Dinhard", "Dozwil", "Egnach", "Elgg", "Erlen", "Ermatingen", "Eschenz", "Eschlikon", "Felben-Wellhausen", "Fischingen", "Flums", "Frauenfeld", "Gachnang", "Gottlieben", "Güttingen", "Hagenbuch", "Hauptwil-Gottshaus", "Hefenhofen", "Herdern", "Herisau", "Hettlingen", "Hohentannen", "Homburg", "Horn", "Häggenschwil", "Hüttlingen", "Hüttwilen", "Kaltbrunn", "Kemmental", "Kesswil", "Kirchberg (SG)", "Kradolf-Schönenberg", "Kreuzlingen", "Langrickenbach", "Lengwil", "Locarno", "Lommis", "Lugano", "Mammern", "Matzingen", "Mosnang", "Muolen", "Märstetten", "Müllheim", "Münchwilen (TG)", "Münsterlingen", "Neckertal", "Nesslau", "Neunforn", "Niederbüren", "Niederhelfenschwil", "Nürensdorf", "Pfyn", "Porza", "Ramsen", "Raperswilen", "Rickenbach (TG)", "Roggwil (TG)", "Romanshorn", "Salenstein", "Salmsach", "Schlatt (TG)", "Schlatt (ZH)", "Schönholzerswilen", "Sirnach", "Sommeri", "St. Gallen", "Stammheim", "Steckborn", "Stein (AR)", "Stettfurt", "Stüsslingen", "Sulgen", "Teufen (AR)", "Thundorf", "Tobel-Tägerschen", "Truttikon", "Turbenthal", "Tägerwilen", "Tübach", "Uesslingen-Buch", "Uster", "Uttwil", "Wagenhausen", "Waldkirch", "Warth-Weiningen", "Weinfelden", "Wiesendangen", "Wigoltingen", "Wil (SG)", "Wila", "Wildberg", "Wilen (TG)", "Winterthur", "Wittenbach", "Wuppenau", "Wäldi", "Wängi", "Zihlschlacht-Sitterdorf"

]

coordinates = {
    "Aadorf": (47.5000, 8.9000), "Affeltrangen": (47.5167, 9.0167), "Altnau": (47.6167, 9.2500), "Amlikon-Bissegg": (47.5667, 9.0500), "Amriswil": (47.5500, 9.3000), "Appenzell": (47.3314, 9.4086), "Arbon": (47.5167, 9.4333), "Avegno Gordevio": (46.2833, 8.6833), "Basadingen-Schlattingen": (47.6667, 8.7500), "Bauma": (47.3667, 8.8333), "Bellinzona": (46.1950, 9.0231), "Berg (SG)": (47.4833, 9.3167), "Berg (TG)": (47.5667, 9.2167), "Berlingen": (47.6500, 8.9833), "Bettwiesen": (47.4667, 8.9500), "Bichelsee-Balterswil": (47.4833, 8.8833), "Birwinken": (47.6000, 9.1167), "Bischofszell": (47.5000, 9.2167), "Bottighofen": (47.6500, 9.2500), "Braunau": (47.4833, 9.0333), "Brütten": (47.4500, 8.6333), "Bussnang": (47.5167, 9.1333), "Bürglen (TG)": (47.5667, 9.1667), "Centovalli": (46.2333, 8.6333), "Diessenhofen": (47.6833, 8.6833), "Dinhard": (47.5833, 8.7167), "Dozwil": (47.5667, 9.3333), "Egnach": (47.5500, 9.4000), "Elgg": (47.4833, 8.7833), "Erlen": (47.5667, 9.2167), "Ermatingen": (47.6667, 9.1000), "Eschenz": (47.6333, 8.8833), "Eschlikon": (47.4333, 8.9833), "Felben-Wellhausen": (47.5667, 8.7333), "Fischingen": (47.4167, 8.8667), "Flums": (47.0667, 9.4667), "Frauenfeld": (47.5500, 8.9000), "Gachnang": (47.5500, 8.9667), "Gottlieben": (47.6667, 9.1667), "Güttingen": (47.6333, 9.2667), "Hagenbuch": (47.5167, 8.8000), "Hauptwil-Gottshaus": (47.4833, 9.2000), "Hefenhofen": (47.5833, 9.2833), "Herdern": (47.6667, 8.7833), "Herisau": (47.3833, 9.2833), "Hettlingen": (47.4833, 8.6167), "Hohentannen": (47.4500, 9.0833), "Homburg": (47.6167, 8.9167), "Horn": (47.5333, 9.4500), "Häggenschwil": (47.4500, 9.3667), "Hüttlingen": (47.5833, 8.9833), "Hüttwilen": (47.6333, 8.9333), "Kaltbrunn": (47.2167, 9.0000), "Kemmental": (47.6500, 8.9500), "Kesswil": (47.6333, 9.3000), "Kirchberg (SG)": (47.4167, 9.0833), "Kradolf-Schönenberg": (47.5167, 9.1667), "Kreuzlingen": (47.6500, 9.1833), "Langrickenbach": (47.5833, 9.3167), "Lengwil": (47.6333, 9.2000), "Locarno": (46.1667, 8.7833), "Lommis": (47.4667, 9.0500), "Lugano": (46.0100, 8.9600), "Mammern": (47.6667, 8.8333), "Matzingen": (47.5167, 8.9500), "Mosnang": (47.3667, 9.0000), "Muolen": (47.4833, 9.4000), "Märstetten": (47.6000, 9.1333), "Müllheim": (47.5833, 9.0167), "Münchwilen (TG)": (47.4833, 8.9333), "Münsterlingen": (47.6333, 9.2167), "Neckertal": (47.3500, 9.1667), "Nesslau": (47.2500, 9.1667), "Neunforn": (47.6833, 8.6500), "Niederbüren": (47.4667, 9.2167), "Niederhelfenschwil": (47.4500, 9.2333), "Nürensdorf": (47.4667, 8.6167), "Pfyn": (47.6000, 8.9833), "Porza": (46.0281, 8.9483), "Ramsen": (47.7167, 8.7333), "Raperswilen": (47.6500, 8.9333), "Rickenbach (TG)": (47.4500, 9.0167), "Roggwil (TG)": (47.5167, 9.3833), "Romanshorn": (47.5667, 9.3667), "Salenstein": (47.6667, 9.0333), "Salmsach": (47.5500, 9.3500), "Schlatt (TG)": (47.6833, 8.7167), "Schlatt (ZH)": (47.4833, 8.5333), "Schönholzerswilen": (47.4333, 9.1500), "Sirnach": (47.4167, 8.9833), "Sommeri": (47.5833, 9.3000), "St. Gallen": (47.4239, 9.3747), "Stammheim": (47.6333, 8.7667), "Steckborn": (47.6667, 8.9667), "Stein (AR)": (47.3667, 9.3833), "Stettfurt": (47.5000, 8.9833), "Stüsslingen": (47.3667, 7.9667), "Sulgen": (47.5333, 9.1167), "Teufen (AR)": (47.3833, 9.3333), "Thundorf": (47.5333, 8.9833), "Tobel-Tägerschen": (47.4833, 9.0000), "Truttikon": (47.6167, 8.6333), "Turbenthal": (47.4167, 8.7500), "Tägerwilen": (47.6667, 9.1500), "Tübach": (47.4833, 9.4667), "Uesslingen-Buch": (47.6333, 8.7833), "Uster": (47.3500, 8.7167), "Uttwil": (47.6000, 9.3333), "Wagenhausen": (47.6667, 8.8500), "Waldkirch": (47.4167, 9.2833), "Warth-Weiningen": (47.6167, 8.8167), "Weinfelden": (47.5667, 9.1000), "Wiesendangen": (47.5333, 8.6333), "Wigoltingen": (47.6167, 9.0667), "Wil (SG)": (47.4600, 9.0400), "Wila": (47.3833, 8.8000), "Wildberg": (47.4167, 8.7833), "Wilen (TG)": (47.4333, 9.0667), "Winterthur": (47.5000, 8.7333), "Wittenbach": (47.4500, 9.3333), "Wuppenau": (47.4167, 9.0667), "Wäldi": (47.6500, 9.0000), "Wängi": (47.5000, 8.8667), "Zihlschlacht-Sitterdorf": (47.5333, 9.2500),

}

def get_municipality_map_data(selected=None):
    from plotly import graph_objects as go

    if selected is None:
        selected = municipalities_list

    latitudes = [coordinates[mun][0] for mun in selected if mun in coordinates]
    longitudes = [coordinates[mun][1] for mun in selected if mun in coordinates]
    labels = [mun for mun in selected if mun in coordinates]

    fig = go.Figure(go.Scattermapbox(
    lat=latitudes,
    lon=longitudes,
    mode='markers+text',
    text=labels,
    textposition="bottom center",  # << Move this inside Scattermapbox
    marker=go.scattermapbox.Marker(
        size=12,
        color='#C9B037',  # Gold color
        opacity=1.0,
        symbol="circle"  # Optional: You can try 'star' or 'diamond'
    )
))

    fig.update_layout(
        title_text='Selected Municipalities',
        mapbox=dict(
            accesstoken=None,
            style="open-street-map",
            center=go.layout.mapbox.Center(lat=47.55, lon=9.0),
            pitch=0,
            zoom=8
        ),
        margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig