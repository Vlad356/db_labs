from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey,
    Date, Time, Boolean, Enum
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

WIND_DIRECTIONS = (
    'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'
)

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    country = Column(String(50), nullable=False)
    last_updated = Column(Date, nullable=False)
    sunrise = Column(Time, nullable=False)
    
    # Зовнішні ключі для вітру та якості повітря
    wind_id = Column(Integer, ForeignKey('wind.id'))
    air_quality_id = Column(Integer, ForeignKey('air_quality.id'))

    # Встановлення зв'язків
    wind = relationship("Wind", back_populates="weather")
    air_quality = relationship("AirQuality", back_populates="weather")


class Wind(Base):
    __tablename__ = 'wind'

    id = Column(Integer, primary_key=True)
    wind_degree = Column(Integer, nullable=False)
    wind_kph = Column(Float, nullable=False)
    wind_mph = Column(Float, nullable=False)
    gust_kph = Column(Float, nullable=True)
    wind_direction = Column(Enum(*WIND_DIRECTIONS, name='wind_direction'), nullable=False)
    
    weather = relationship("Weather", back_populates="wind", uselist=False)


class AirQuality(Base):
    __tablename__ = 'air_quality'

    id = Column(Integer, primary_key=True)
    air_quality_carbon_monoxide = Column(Float, nullable=True)
    air_quality_ozone = Column(Float, nullable=True)
    air_quality_nitrogen_dioxide = Column(Float, nullable=True)
    air_quality_sulphur_dioxide = Column(Float, nullable=True)
    air_quality_pm2_5 = Column(Float, nullable=True)
    air_quality_pm10 = Column(Float, nullable=True)
    air_quality_us_epa_index = Column(Integer, nullable=True)
    air_quality_gb_defra_index = Column(Integer, nullable=True)

    weather = relationship("Weather", back_populates="air_quality", uselist=False)
