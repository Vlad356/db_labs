from sqlalchemy import (
    Column, Integer, String, Float, Date, Time, Boolean, Enum
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Можливі напрямки вітру
WIND_DIRECTIONS = (
    'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'
)

class Weather(Base):
    __tablename__ = 'weather'

    # Ідентифікатор запису
    id = Column(Integer, primary_key=True)
    
    # Текстова колонка для країни
    country = Column(String(50), nullable=False)
    
    # Колонки для часу та дати
    last_updated = Column(Date, nullable=False)
    sunrise = Column(Time, nullable=False)
    
    # Колонки для вітру
    wind_degree = Column(Integer, nullable=False)  # Напрямок вітру
    wind_kph = Column(Float, nullable=False)  # Швидкість вітру в км/год
    wind_mph = Column(Float, nullable=False)  # Швидкість вітру в милях/год
    gust_kph = Column(Float, nullable=True)  # Пориви вітру в км/год
    wind_direction = Column(Enum(*WIND_DIRECTIONS, name='wind_direction'), nullable=False)  # Напрямок вітру
    
    # Колонка для оцінки чи варто виходити на вулицю
    should_go_outside = Column(Boolean, nullable=False)
    
    # Колонки для стану повітря
    air_quality_carbon_monoxide = Column(Float, nullable=True)
    air_quality_ozone = Column(Float, nullable=True)
    air_quality_nitrogen_dioxide = Column(Float, nullable=True)
    air_quality_sulphur_dioxide = Column(Float, nullable=True)
    air_quality_pm2_5 = Column(Float, nullable=True)
    air_quality_pm10 = Column(Float, nullable=True)
    air_quality_us_epa_index = Column(Integer, nullable=True)
    air_quality_gb_defra_index = Column(Integer, nullable=True)
