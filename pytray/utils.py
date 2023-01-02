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
        

def bits_to_mb(size_bits):
    return round(size_bits / 8000000, 2)


def bits_to_mbit(size_bits):
    return round(size_bits * 0.000001, 2)