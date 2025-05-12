from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Weather, Base

# Підключення до бази даних 
DATABASE_URL = "postgresql://postgres:Vv05091003@localhost/lab3"
# Створюємо підключення до бази даних
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

from datetime import datetime

def get_weather_by_country_and_date(country: str, date: str):
    try:
        search_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Невірний формат дати. Використовуйте формат YYYY-MM-DD.")
        return

    weather_data = session.query(Weather).filter(
        Weather.country == country,
        Weather.last_updated == search_date
    ).first()

    if weather_data:
        print(f"\nІнформація про погоду для країни {country} на дату {date}:")
        print(f"Країна: {weather_data.country}")
        print(f"Дата останнього оновлення: {weather_data.last_updated}")
        print(f"Час сходу сонця: {weather_data.sunrise}")

        if weather_data.wind:
            print(f"Швидкість вітру: {weather_data.wind.wind_kph} км/год")
            print(f"Напрямок вітру: {weather_data.wind.wind_direction}")
            print(f"Чи варто виходити на вулицю: {'Так' if weather_data.wind.should_go_outside else 'Ні'}")
        else:
            print("Дані про вітер відсутні.")

        if weather_data.air_quality:
            print(f"Якість повітря (CO): {weather_data.air_quality.air_quality_carbon_monoxide}")
            print(f"Якість повітря (Ozone): {weather_data.air_quality.air_quality_ozone}")
            print(f"Якість повітря (NO2): {weather_data.air_quality.air_quality_nitrogen_dioxide}")
            print(f"Якість повітря (SO2): {weather_data.air_quality.air_quality_sulphur_dioxide}")
            print(f"Якість повітря (PM2.5): {weather_data.air_quality.air_quality_pm2_5}")
            print(f"Якість повітря (PM10): {weather_data.air_quality.air_quality_pm10}")
            print(f"Індекс якості повітря (US EPA): {weather_data.air_quality.air_quality_us_epa_index}")
            print(f"Індекс якості повітря (GB DEFRA): {weather_data.air_quality.air_quality_gb_defra_index}")
        else:
            print("Дані про якість повітря відсутні.")
    else:
        print(f"\nНе знайдено даних для країни {country} на дату {date}.")

def main():
    print("Вітаємо у системі перегляду погодних даних!")
    country = input("Введіть країну: ")
    date = input("Введіть дату (формат: YYYY-MM-DD): ")

    get_weather_by_country_and_date(country, date)

if __name__ == "__main__":
    main()
