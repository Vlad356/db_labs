import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Weather, Wind, AirQuality

# Параметри підключення до бази даних
# DATABASE_URL = "postgresql://postgres:Vv05091003@localhost/lab3"
DATABASE_URL = "mysql+pymysql://root:Vv05091003@localhost/lab3_mysql"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Завантаження CSV
df = pd.read_csv('GlobalWeatherRepository.csv')

# Завантаження даних у базу
for _, row in df.iterrows():
    # Створення об'єкта Wind
    wind = Wind(
        wind_degree=row['wind_degree'],
        wind_kph=row['wind_kph'],
        wind_mph=row['wind_mph'],
        gust_kph=row.get('gust_kph'),
        wind_direction=row['wind_direction'],
        should_go_outside=row['wind_kph'] <= 36.0
    )
    session.add(wind)
    session.flush()  # отримати wind.id

    # Створення об'єкта AirQuality
    air_quality = AirQuality(
        air_quality_carbon_monoxide=row.get('air_quality_Carbon_Monoxide'),
        air_quality_ozone=row.get('air_quality_Ozone'),
        air_quality_nitrogen_dioxide=row.get('air_quality_Nitrogen_dioxide'),
        air_quality_sulphur_dioxide=row.get('air_quality_Sulphur_dioxide'),
        air_quality_pm2_5=row.get('air_quality_PM2.5'),
        air_quality_pm10=row.get('air_quality_PM10'),
        air_quality_us_epa_index=row.get('air_quality_us-epa-index'),
        air_quality_gb_defra_index=row.get('air_quality_gb-defra-index')
    )
    session.add(air_quality)
    session.flush()  # отримати air_quality.id

    # Створення об'єкта Weather
    weather = Weather(
        country=row['country'],
        last_updated=pd.to_datetime(row['last_updated']).date(),
        sunrise=pd.to_datetime(row['sunrise']).time(),
        wind_id=wind.id,
        air_quality_id=air_quality.id
    )
    session.add(weather)

# Завершення сесії
session.commit()
session.close()
