import pytest
import requests

TYPES = {"micro","nano","regional","brewpub","large","planning","bar","contract","proprietor","closed"}
COUNTRIES = [
    ("France", 3),
    ("Isle of Man", 2),
    ("Italy", 4),
    ("Japan", 10),
    ("Poland", 34),
    ("Scotland", 10),
    ("Singapore", 33),
    ("Sweden", 36),
    ("Ukraine", 1),
]

class TestBrewAPI:
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

    @pytest.mark.parametrize("brewery_type", TYPES)
    def test_get_brewery_with_type(self, brewery_type):
        response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_type={brewery_type}")
        brewery_type_parameter = response.json()[0]["brewery_type"]

        assert response.status_code == 200, f'Actual status code is {response.status_code}'
        assert isinstance(brewery_type_parameter, str) and brewery_type_parameter.strip(), "Brewery type is not str or empty"

    @pytest.mark.parametrize("country, brewery_count", COUNTRIES)
    def test_get_brewery_count_of_each_country(self, country, brewery_count):
        response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_country={country}")
        brewery_response = response.json()

        assert response.status_code == 200, f'Actual status code is {response.status_code}'
        assert len(brewery_response) == brewery_count, f'Brewery count is incorrect for {country}, actual is {len(brewery_response)}'
