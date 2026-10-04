import pytest
import requests


class TestJSONplaceholder:
    @pytest.mark.parametrize("id", range(1,100))
    def test_get_posts_by_id(self, id):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts?id={id}')
        id_value = response.json()[0]['id']

        assert response.status_code == 200
        assert id_value == id

    @pytest.mark.parametrize("post", range(1, 100))
    def test_get_comments_for_every_post(self, post):
        response = requests.get(f'https://jsonplaceholder.typicode.com//comments?postId={post}')
        postId = response.json()[0]['postId']

        assert response.status_code == 200
        assert postId == post

    def test_get_all_users(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/users')

        assert response.status_code == 200
        assert response.json()[9]['username'] == "Moriah.Stanton"

    def test_get_title_in_photo_response(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/photos')
        title_value = response.json()[0]['title']

        assert response.status_code == 200
        assert isinstance(title_value, str) and title_value.strip()

    @pytest.mark.parametrize("todos_number", range(1, 200))
    def test_get_todos_and_check_completed_status(self, todos_number):
        response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{todos_number}')
        completed_status = response.json()['completed']

        assert response.status_code == 200
        assert isinstance(completed_status, bool), "Completed status must be boolean"
