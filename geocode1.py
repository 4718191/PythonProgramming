import pandas as pd
import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='Gyeongju v1.0')

# 지도 중심 → 경주
center = geolocator.geocode('Gyeongju South Korea')

df = pd.DataFrame()
df['이름'] = ['불국사', '석굴암', '첨성대', '동궁과 월지']
lat = []
lng = []

for _, row in df.iterrows():
    loc = geolocator.geocode(row['이름'] + ' 경주')
    
    if loc:  # None 체크 (중요 ⭐)
        lat.append(loc.latitude)
        lng.append(loc.longitude)
    else:
        lat.append(None)
        lng.append(None)

df['위도'] = lat
df['경도'] = lng

# None 제거 (지도 오류 방지)
df = df.dropna()
m = folium.Map(location=[center.latitude, center.longitude],
               zoom_start=12,
               tiles='cartodb positron',
               width=640,
               height=480
)

for _, row in df.iterrows():
    folium.Marker(
        [row['위도'], row['경도']],
        tooltip=row['이름']
    ).add_to(m)

m
