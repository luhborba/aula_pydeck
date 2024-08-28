import streamlit as st
import pandas as pd
import pydeck as pdk
import json

st.title('Página de Dashboards de Mapas - Bonitinhos')
acidentes_Data = ("https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv")
df = pd.read_csv(acidentes_Data)

layer = pdk.Layer(
    'HexagonLayer',
    df,
    get_position='[lng, lat]',
    auto_hitglight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0,3000],
    extruded=True,
    coverage=1
)
st.pydeck_chart(pdk.Deck(layer))

dados_bicicleta = 'https://raw.githubusercontent.com/uber-common/deck.gl-data/master/website/sf-bike-parking.json'
df2 = pd.read_json(dados_bicicleta)

layer = pdk.Layer(
    'GridLayer',
    df2,
    pickable=True,
    extruded=True,
    cell_size=200,
    elevation_scale=4,
    get_position="COORDINATES",
)
view_state = pdk.ViewState(latitude=37.7749295, longitude=-122.4194155, zoom=11, bearing=0, pitch=40)
render = pdk.Deck(layers=[layer],initial_view_state=view_state,tooltip={"text":"{position}\nCount: {count}"})
st.pydeck_chart(render)


st.title("Mapa de Incidência de Acidentes no Brasil")

# Exibição da tabela com os dados
st.subheader('Dados de Incidentes')
df3 = pd.read_json('incidentes.json')

layer = pdk.Layer(
    'ScatterplotLayer',
    data=df3,
    get_position='coordinates',
    get_fill_color='[255, 0, 0, 150]',
    get_radius='incidents * 10000',
    pickable=True,
    auto_highlight=True
)
view_state = pdk.ViewState(
    latitude=-14.235004,
    longitude=-51.92528,
    zoom=3,
    pitch=50
)
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{region}\nIncidents: {incidents}"}
))

st.title('Atendimento na Paraíba')
dados_json = '''
[
    {"cidade": "João Pessoa", "coordinates": [-34.8781, -7.11532], "atendimentos": 111},
    {"cidade": "Campina Grande", "coordinates": [-35.8711, -7.23072], "atendimentos": 189},
    {"cidade": "Patos", "coordinates": [-37.2747, -7.02436], "atendimentos": 150},
    {"cidade": "Santa Rita", "coordinates": [-34.9787, -7.11348], "atendimentos": 62},
    {"cidade": "Bayeux", "coordinates": [-34.9296, -7.12543], "atendimentos": 120},
    {"cidade": "Sousa", "coordinates": [-38.2284, -6.75148], "atendimentos": 120},
    {"cidade": "Cajazeiras", "coordinates": [-38.5597, -6.88004], "atendimentos": 111},
    {"cidade": "Guarabira", "coordinates": [-35.4903, -6.8524], "atendimentos": 82},
    {"cidade": "Cabedelo", "coordinates": [-34.8389, -6.98192], "atendimentos": 32},
    {"cidade": "Pombal", "coordinates": [-37.8005, -6.76614], "atendimentos": 195},
    {"cidade": "Monteiro", "coordinates": [-37.1185, -7.88911], "atendimentos": 30},
    {"cidade": "Sapé", "coordinates": [-35.2286, -7.09318], "atendimentos": 47},
    {"cidade": "Mamanguape", "coordinates": [-35.1211, -6.83338], "atendimentos": 57},
    {"cidade": "Queimadas", "coordinates": [-35.9047, -7.35086], "atendimentos": 151},
    {"cidade": "Esperança", "coordinates": [-35.8653, -7.02256], "atendimentos": 132},
    {"cidade": "Solânea", "coordinates": [-35.6642, -6.75148], "atendimentos": 133},
    {"cidade": "Cuité", "coordinates": [-36.1564, -6.47658], "atendimentos": 118},
    {"cidade": "Alagoa Grande", "coordinates": [-35.6201, -7.03929], "atendimentos": 74},
    {"cidade": "Catolé do Rocha", "coordinates": [-37.7463, -6.34064], "atendimentos": 82},
    {"cidade": "Itabaiana", "coordinates": [-35.3315, -7.32811], "atendimentos": 96},
    {"cidade": "Alagoa Nova", "coordinates": [-35.7643, -7.05478], "atendimentos": 139},
    {"cidade": "Sumé", "coordinates": [-36.8822, -7.67278], "atendimentos": 101},
    {"cidade": "Areia", "coordinates": [-35.6974, -6.96372], "atendimentos": 198},
    {"cidade": "Remígio", "coordinates": [-35.8012, -6.94916], "atendimentos": 137},
    {"cidade": "Boqueirão", "coordinates": [-36.1303, -7.48535], "atendimentos": 130},
    {"cidade": "Piancó", "coordinates": [-37.9272, -7.19228], "atendimentos": 101},
    {"cidade": "Itaporanga", "coordinates": [-38.1508, -7.3021], "atendimentos": 174},
    {"cidade": "Soledade", "coordinates": [-36.3666, -7.058], "atendimentos": 86},
    {"cidade": "Belém", "coordinates": [-35.516, -6.74136], "atendimentos": 50},
    {"cidade": "Princesa Isabel", "coordinates": [-37.9888, -7.73693], "atendimentos": 34}
]
'''

dados = json.loads(dados_json)

# Criar um DataFrame a partir dos dados JSON
df = pd.DataFrame(dados)

# Ajustar o tamanho da elevação com base na quantidade de atendimentos
max_atendimentos = df["atendimentos"].max()
df["elevation"] = df["atendimentos"] / max_atendimentos * 1000  # Escalar a elevação para um valor visível

# Definir a camada do mapa utilizando Pydeck
column_layer = pdk.Layer(
    "ColumnLayer",
    data=df,
    get_position=["coordinates[0]", "coordinates[1]"],
    elevation_scale=100,  # Ajustar a escala de elevação
    radius=300,  # Raio da coluna
    get_fill_color=["255", "140", "0", "140"],  # Cor da coluna com transparência
    pickable=True,
    auto_highlight=True,
)

# Configurar a visualização inicial do mapa
view_state = pdk.ViewState(
    latitude=-7.12,
    longitude=-36.5,
    zoom=6,
    pitch=80,  # Ajustar a inclinação
    #bearing=60,  # Ajustar a direção
)

# Configurar o tooltip
tooltip = {
    "html": "<b>{cidade}</b><br>Atendimentos: <b>{atendimentos}</b>",
    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}

# Renderizar o mapa usando Streamlit e Pydeck
st.pydeck_chart(pdk.Deck(
    layers=[column_layer],
    initial_view_state=view_state,
    tooltip=tooltip
))