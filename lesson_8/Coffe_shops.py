import json
import requests
import os
from dotenv import load_dotenv
from geopy import distance
import folium
import branca


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def get_distance(cafe):
    return cafe['distance']


def main():
    with open('coffee.json', mode='r') as file:
        content = file.read()
    cafe_list = json.loads(content)

    load_dotenv()
    apikey = os.getenv("apikey")
    your_location = input('Где вы находитесь? ')
    my_coord = fetch_coordinates(apikey, your_location)
    my_coord_reversed = (my_coord[1], my_coord[0])

    cafe_list_cut = []

    for cafe in cafe_list:
        name = cafe.get('Name')
        geoData = cafe.get('geoData')
        coordinates = geoData.get('coordinates')
        longitude = coordinates[0]
        latitude = coordinates[1]
        coordinates_reversed = (coordinates[1], coordinates[0])
        dist = int(distance.distance(my_coord_reversed, coordinates_reversed).m)
        cafe_dict = {
            'title': name,
            'distance': dist,
            'latitude': latitude,
            'longitude': longitude,
        }
        cafe_list_cut.append(cafe_dict)

    cafe_list_sorted = sorted(cafe_list_cut, key=get_distance)

    m = folium.Map(location=(my_coord_reversed))
    folium.Marker(
        location=[my_coord_reversed[0], my_coord_reversed[1]],
        tooltip='Вы находитесь здесь!',
        popup='Ваше местоположение.',
        icon=folium.Icon(color="red"),
    ).add_to(m)

    for cafe in cafe_list_sorted[:5]:
        html = f"""
            <h3>{cafe['title']}</h3>
            <p style="font-size: 12px; color: #2c3e50;">
                Расстояние до кофейни примерно {cafe['distance']} метров
            </p>
        """
        iframe = branca.element.IFrame(html=html, width=180, height=100)
        popup = folium.Popup(iframe, max_width=150)
        folium.Marker(
            location=[cafe['latitude'], cafe['longitude']],
            tooltip=cafe['title'],
            popup=popup,
            icon=folium.Icon(icon="leaf"),
        ).add_to(m)

    m.save("index.html")


if __name__ == '__main__':
    main()
