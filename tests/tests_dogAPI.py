import pytest
import requests

BREEDS = {"affenpinscher","african","airedale","akita","appenzeller","australian","bakharwal","basenji"}

SUB_BREEDS = {"afghan","basset","blood","english","ibizan","plott","walker"}

class TestDogAPI:
    @pytest.mark.parametrize("breed", BREEDS)
    def test_success_status_random_dog_image(self, breed):
        response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')

        assert response.status_code == 200, f'Actual status code is {response.status_code}'
        assert response.json()['status'] == 'success'

    def test_error_get_unknown_dog_breed(self):
        response = requests.get('https://dog.ceo/api/breed/unknown/images')

        assert response.status_code == 404, f'Actual status code is {response.status_code}'
        assert response.json()['status'] == 'error'

    def test_get_random_breed(self):
        response = requests.get('https://dog.ceo/api/breeds/image/random')

        assert response.json()['message'].startswith(
            'https://images.dog.ceo/breeds/'
        ), f'Incorrect source in response, actual is {response.json()['message']}'


    @pytest.mark.parametrize("sub_breed", SUB_BREEDS)
    def test_get_sub_breed(self, sub_breed):
        response = requests.get(f'https://dog.ceo/api/breed/hound/{sub_breed}/images')

        assert response.status_code == 200, f'Actual status code is {response.status_code}'
        assert response.json()['message'][0].startswith(
            'https://images.dog.ceo/breeds/hound'
        ), f'Incorrect source in response, actual is {response.json()['message']}'

    def test_get_some_breed_in_all_list(self):
        response = requests.get('https://dog.ceo/api/breeds/list/all')

        assert response.json()['status'] == 'success', f'Actual status code is {response.status_code}'
        assert response.json()['message'] != ""
