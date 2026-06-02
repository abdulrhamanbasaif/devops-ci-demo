from calculator import add, subtract, multiply, divide
from app import app
import pytest


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_add_negative():
    assert add(-1, -1) == -2


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_api_add(client):
    response = client.post(
        '/calculate',
        json={'a': 10, 'b': 5, 'operation': 'add'}
    )
    assert response.status_code == 200
    assert response.get_json()['result'] == 15


def test_api_divide_by_zero(client):
    response = client.post(
        '/calculate',
        json={'a': 5, 'b': 0, 'operation': 'divide'}
    )
    assert response.status_code == 400


def test_api_invalid_operation(client):
    response = client.post(
        '/calculate',
        json={'a': 5, 'b': 2, 'operation': 'power'}
    )
    assert response.status_code == 400