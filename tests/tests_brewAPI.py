from _pytest import unittest
import requests


class TestBrewAPI(unittest.TestCase):
    def test_all_meta_data_success(self):
        response = requests.get("https://api.openbrewerydb.org/v1/breweries/meta")

        assert response.status_code == 200, f'Actual status code is {response.status_code}'

    def test_get_brewery_by_city(self):
        response = requests.get("https://api.openbrewerydb.org/v1/breweries?by_city=new_york")

        assert response.status_code == 200, f'Actual status code is {response.status_code}'
        assert response.json()[0]["city"] == "New York"

    def test_get_specific_brewery(self):
        obdb_id = requests.get("https://api.openbrewerydb.org/v1/breweries?by_city=new_york").json()[0]["id"]
        response = requests.get(f"https://api.openbrewerydb.org/v1/breweries/{obdb_id}")

        assert response.status_code == 200, f'Actual status code is {response.status_code}'
        assert response.json()["id"] == obdb_id, f'Actual id is {response.json()["id"]}'

    def test_get_random_brewery(self):
        url = requests.get("https://api.openbrewerydb.org/v1/breweries/random")
        response = url.json()

        assert url.status_code == 200, f'Actual status code is {url.status_code}'
        assert all(isinstance(item, dict) for item in response), "There are not objects in this list"


