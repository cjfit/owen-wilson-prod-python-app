import pytest
import sys
from requests.exceptions import HTTPError
# set path
sys.path.append('../')
from app.main import get_account

@pytest.fixture
def example_json_data():
    return [{"movie":"Meet the Parents","year":2000,"release_date":"2000-10-06","director":"Jay Roach","character":"Kevin Rawley","movie_duration":"01:47:39","timestamp":"00:56:16","full_line":"Well, so was JC! Wow, you're in good company.","current_wow_in_movie":2,"total_wows_in_movie":2,"poster":"https://images.ctfassets.net/bs8ntwkklfua/3gZNaRP4IqEDG0Vs3ntCUc/ec3f5c9ce1e42e83a8dcbc9ed199d604/Meet_the_Parents_Poster.jpg","video":{"1080p":"https://videos.ctfassets.net/bs8ntwkklfua/511EVfdb0nnM1zlWeFTnuj/2df1ba6f8ddaf445b73a3103a88d8314/Meet_the_Parents_Wow_2_1080p.mp4","720p":"https://videos.ctfassets.net/bs8ntwkklfua/4CLvfbAWDOTyDHhZKvpflX/fbf41eefee905fea240283dafe3b64a0/Meet_the_Parents_Wow_2_720p.mp4","480p":"https://videos.ctfassets.net/bs8ntwkklfua/37w17u0kUUmg01hVZFXNud/17839fc0f87e00e2af79bfad7b36ef7f/Meet_the_Parents_Wow_2_480p.mp4","360p":"https://videos.ctfassets.net/bs8ntwkklfua/6OT1bszjJ8Lf3jtlVoRoHx/4d6eab3db8876c48e65978b31d24cd89/Meet_the_Parents_Wow_2_360p.mp4"},"audio":"https://assets.ctfassets.net/bs8ntwkklfua/2SgnPN23fk4EPQ7yuSQDiJ/3c0f409e7e775bebff2c526bd42dc159/Meet_the_Parents_Wow_2.mp3"}]

def test_get_account_http_error(requests_mock):
    requests_mock.get('https://owen-wilson-wow-api.onrender.com/wows/random?movie=The%20Avengers', status_code=404)
    with pytest.raises(HTTPError):
        get_account('The Avengers')

def test_get_account_success(requests_mock, example_json_data):
    requests_mock.get('https://owen-wilson-wow-api.onrender.com/wows/random?movie=Meet%20The%20Parents',
                      json=example_json_data)
    assert get_account('Meet The Parents') == \
           example_json_data
