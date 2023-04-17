import requests
import json

def test_helloworld():
    response = requests.get('http://localhost:8080/helloworld')
    assert response.status_code == 200
    assert response.text == 'Hello Stranger'

def test_helloworld_with_name():
    response = requests.get('http://localhost:8080/helloworld?name=AlfredENeumann')
    assert response.status_code == 200
    assert response.text == 'Hello Alfred E Neumann'

def test_versionz():
    response = requests.get('http://localhost:8080/versionz')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    json_data = json.loads(response.text)
    assert 'git_hash' in json_data
    assert 'git_name' in json_data