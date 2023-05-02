from streamlit_folium import st_folium
from pathlib import Path
import streamlit as st
import numpy as np
import pydeck as pdk
import folium
import folium.features
import pandas as pd
import requests


st.set_page_config(
    page_title="Folium",
    page_icon="👹",
)

st.title("The US Population Study case")
st.sidebar.success("Use case using folium library")

p = Path(__file__).parent / "./source/states.csv"
STATE_DATA = pd.read_csv(p)
biggest_population = STATE_DATA.nlargest(5, 'population')
data_biggest_population = dict(
    zip(biggest_population['population'], biggest_population['state']))

perm = np.random.permutation(3)


tab1, tab2, tab3 = st.tabs(["Map Diagram",  "Population Ranking", "Docs"])


with tab1:

    @st.cache_data
    def _get_all_state_bounds() -> dict:
        # url = "https://raw.githubusercontent.com/superpikar/indonesia-geojson/master/indonesia.geojson"
        url = "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
        data = requests.get(url).json()
        return data

    @st.cache_data
    def get_state_bounds(state: str) -> dict:
        data = _get_all_state_bounds()
        state_entry = [f for f in data["features"]
                       if f["properties"]["name"] == state][0]
        return {"type": "FeatureCollection", "features": [state_entry]}

    def get_state_from_lat_lon(lat: float, lon: float) -> str:
        state_row = STATE_DATA[
            STATE_DATA.latitude.between(lat - 0.000001, lat + 0.000001)
            & STATE_DATA.longitude.between(lon - 0.000001, lon + 0.000001)
        ].iloc[0]
        return state_row["state"]

    def get_population(state: str) -> int:
        return STATE_DATA.set_index("state").loc[state]["population"]

    def get_seal(state: str) -> int:
        return STATE_DATA.set_index("state").loc[state]["seal"]

    def get_income(state: str) -> int:
        return STATE_DATA.set_index("state").loc[state]["income"]

    def get_capital(state: str) -> int:
        return STATE_DATA.set_index("state").loc[state]["capital"]

    def main():
        if "last_object_clicked" not in st.session_state:
            st.session_state["last_object_clicked"] = None
        if "selected_state" not in st.session_state:
            st.session_state["selected_state"] = "California"

        bounds = get_state_bounds(st.session_state["selected_state"])

        st.write(f"## {st.session_state['selected_state']}")
        seal = get_seal(st.session_state["selected_state"])
        st.image(seal, width=150)

        value_mean = 70
        value_std = 5
        delta_mean = 1.2
        delta_std = 0.5

        value = np.random.normal(value_mean, value_std)
        delta = np.random.normal(delta_mean, delta_std)

        st.metric(label="Temperature",
                  value=f"{value:.1f} °F", delta=f"{delta:.1f} °F")

        population = get_population(st.session_state["selected_state"])
        st.text(f"Population: {population:,}")

        income = get_income(st.session_state["selected_state"])
        st.text(f"Median Household Income: ${income:,.2f}")

        capital = get_capital(st.session_state["selected_state"])
        st.text(f"Capital: {capital}")

        center = None
        if st.session_state["last_object_clicked"]:
            center = st.session_state["last_object_clicked"]

        m = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

        fg = folium.FeatureGroup(name="State bounds")
        fg.add_child(folium.features.GeoJson(bounds))

        capitals = STATE_DATA

        for capital in capitals.itertuples():
            fg.add_child(
                folium.Marker(
                    location=[capital.latitude, capital.longitude],
                    popup=f"{capital.capital}, {capital.state}",
                    tooltip=f"{capital.capital}, {capital.state}",
                    icon=folium.Icon(color="green")
                    if capital.state == st.session_state["selected_state"]
                    else None,
                )
            )

        out = st_folium(
            m,
            feature_group_to_add=fg,
            center=center,
            width=1200,
            height=500,
        )

        if (
            out["last_object_clicked"]
            and out["last_object_clicked"] != st.session_state["last_object_clicked"]
        ):
            st.session_state["last_object_clicked"] = out["last_object_clicked"]
            state = get_state_from_lat_lon(
                *out["last_object_clicked"].values())
            st.session_state["selected_state"] = state
            st.experimental_rerun()

    if __name__ == "__main__":
        main()

with tab2:
    st.header("Population Ranking")

    st.write(biggest_population)
    # st.line_chart(data_biggest_population)
    st.area_chart(
        biggest_population[['state', 'population']].set_index('state'))

    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.write("""
        Currently, California has the largest population among US states. Here's a diagram showing the population distribution in California:
    """)
    st.map(df)

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))


with tab3:
    st.write("""
        Objective: How to present the population and other information for US states. \n

        Source: pages/source/states.csv \n

        Brief Explanation: I'm using the folium library to create a map and integrating the latitudes 
        and longitudes provided in the source file with the polygon geometry of the geojson file found at 
        https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json.\n

        Using this approach, we can extract the data for the five states with the largest populations and present it using the streamlit map method.\n

        Below is the JSON format of our source. It consists of the following fields for each state: state, capital, latitude, longitude, population, seal, and income.\n


    """)

    json_str = STATE_DATA.to_json()

    st.caption("_states.csv_")
    st.json(json_str)
