import unittest
import requests
from unittest.mock import Mock

requests = Mock()


def get_weather(city):
   try:
      response = requests.get(f"https://api.weather.com/v1/weather?q={city}")
      if response.status_code == 200:
            return response.json()
      else:
            return None
   except requests.exceptions.RequestException:
      return None


class TestGetWeather(unittest.TestCase):

   def test_get_weatcher_request_made(self):
      response_mock = Mock()
      response_mock.status_code = 200
      response_mock.json.return_value = {"city": "test"}
      requests.get.return_value = response_mock


      assert get_weather("test") == {"city": "test"}

# To run the tests (note - it will run all defined tests):
unittest.main(argv=[''], exit=False)