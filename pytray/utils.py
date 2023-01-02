import os
import logging
import psutil
import speedtest
import http.client as httplib
import requests
from dotenv import load_dotenv


def test_speed():
    try:
        logging.info("Started speedtest")
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        logging.info("Finished speedtest with values: %s", res)
        return bits_to_mbit(res["download"]), bits_to_mbit(res["upload"]), round(res["ping"], 2)
    except Exception as e:
        logging.error(e)


def have_internet() -> bool:
    logging.info("Checking internet connection")
    conn = httplib.HTTPSConnection("8.8.4.4", timeout=5)
    try:
        conn.request("HEAD", "/")
        logging.info("Internet connection is available")
        return True
    except Exception as e:
        logging.error("Internet connection is not available %s", e)
        return False
    finally:
        conn.close()


def display_usage_cpu_ram(cpu_usage, mem_usage, bars=10):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    print(f"CPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"Memory Usage: |{mem_bar}| {mem_usage:.2f}%  ", end="\r")


def display_usage():
    logging.info("Started CPU & RAM usage")
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    logging.info("Finished CPU & RAM usage with values: %s", {"cpu_usage": cpu_usage, "memory_usage": memory_usage})
    return cpu_usage, memory_usage


def get_weather():
    load_dotenv()
    api_key = os.environ['API_WEATHER']
    city_name = os.environ['CITY_WEATHER']
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
    if response.status_code == 200:
        data = response.json()
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        logging.info("Finished weather with values: %s", {"temperature": temperature_celsius})
        return f"Temperatura de {temperature_celsius:.2f} °C"
    else:
        return f"Error: {response.status_code}"


def bits_to_mb(size_bits):
    return round(size_bits / 8000000, 2)


def bits_to_mbit(size_bits):
    return round(size_bits * 0.000001, 2)
