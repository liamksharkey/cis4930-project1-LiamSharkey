import requests
from django.core.management.base import BaseCommand
from myapp.models import WeatherRecord
from datetime import datetime


class Command(BaseCommand):
        help = "Fetch weather data from Open-Meteo API and store in DB"

        def handle(self, *args, **kwargs):

                base_url = "https://api.open-meteo.com/v1/forecast"

                url_params = {
                "latitude": 41,
                "longitude": -74,
                "daily": [
                        "temperature_2m_max",
                        "temperature_2m_min",
                        "precipitation_sum",
                        "wind_speed_10m_max"
                ],
                "timezone": "auto"
                }

                self.stdout.write("Starting data fetch...")

                while url_params["latitude"] > 0:

                        try:
                                response = requests.get(base_url, params=url_params, timeout=10)
                                response.raise_for_status()

                        except requests.exceptions.Timeout:
                                self.stderr.write("Timeout error")
                                return

                        except requests.exceptions.RequestException as e:
                                self.stderr.write(f"Request failed: {e}")
                                return

                        data = response.json()

                        daily = data.get("daily", {})

                        dates = daily.get("time", [])
                        tmax = daily.get("temperature_2m_max", [])
                        tmin = daily.get("temperature_2m_min", [])
                        prec = daily.get("precipitation_sum", [])
                        wind = daily.get("wind_speed_10m_max", [])

                        for i in range(len(dates)):
                                WeatherRecord.objects.update_or_create(
                                latitude=url_params["latitude"],
                                longitude=url_params["longitude"],
                                date=datetime.strptime(dates[i], "%Y-%m-%d").date(),
                                defaults={
                                        "temp_max": tmax[i] if i < len(tmax) else None,
                                        "temp_min": tmin[i] if i < len(tmin) else None,
                                        "precipitation": prec[i] if i < len(prec) else None,
                                        "wind_speed": wind[i] if i < len(wind) else None,
                                }
                                )

                        self.stdout.write(f"Saved data for lat={url_params['latitude']}")

                        # pagination step (like your project)
                        url_params["latitude"] -= 20

                self.stdout.write(self.style.SUCCESS("Fetch complete"))