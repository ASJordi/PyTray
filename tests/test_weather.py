import requests
from pytray.utils import get_weather

def test_get_weather_success(mocker):
  mock_load_dotenv = mocker.patch("dotenv.load_dotenv")
  mock_os_environ = mocker.patch("os.environ", {'API_WEATHER': 'abc123', 'CITY_WEATHER': 'Buenos Aires'})
  mock_response = mocker.MagicMock()
  mock_response.status_code = 200
  mock_response.json.return_value = {"main": {"temp": 296.15}}
  mocker.patch("requests.get", return_value=mock_response)
  assert get_weather() == "Temperatura de 23.00 °C"


def test_get_weather_failure(mocker):
  mock_load_dotenv = mocker.patch("dotenv.load_dotenv")
  mock_os_environ = mocker.patch("os.environ", {'API_WEATHER': 'abc123', 'CITY_WEATHER': 'Buenos Aires'})
  mock_response = mocker.MagicMock()
  mock_response.status_code = 404
  mocker.patch("requests.get", return_value=mock_response)
  assert get_weather() == "Error: 404"


def test_get_weather_get_called(mocker):
  mocker.patch("requests.get", return_value=mocker.MagicMock())
  mocker.patch.dict("os.environ", {"API_WEATHER": "abc123", "CITY_WEATHER": "Paris"})
  get_weather()
  requests.get.assert_called_with("https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=abc123")
