import sys
import pytest
# set path
sys.path.append('../')
from app.main import merge_data

@pytest.fixture
def example_json_movie1():
    return [{"movie":"Cars","year":2006,"release_date":"2006-06-09","director":"John Lasseter","character":"Lightning McQueen","movie_duration":"01:56:36","timestamp":"01:23:13","full_line":"Wow, you were right!","current_wow_in_movie":4,"total_wows_in_movie":5,"poster":"https://images.ctfassets.net/bs8ntwkklfua/6dsHUil72TJLYqbwYMEjH4/387a2d9994a2f1fb069d970a0f30ba32/Cars_Poster.jpg","video":{"1080p":"https://videos.ctfassets.net/bs8ntwkklfua/5WH68GXLSVdosuz0ouwFDF/0b55b456669a8bf8a13e6aecd46cae89/Cars_Wow_4_1080p.mp4","720p":"https://videos.ctfassets.net/bs8ntwkklfua/7KSwlI2izHJDNtiGAH32SU/7d7698ac27be72753ddc1e2291399b46/Cars_Wow_4_720p.mp4","480p":"https://videos.ctfassets.net/bs8ntwkklfua/6OExsgI6VJHXcjNZtlqBkx/3152bd6700486416ec0b818829de9374/Cars_Wow_4_480p.mp4","360p":"https://videos.ctfassets.net/bs8ntwkklfua/2ibZvAYOWwmoqQtANL3d8o/9c09f29a7f42ecd996ac991b52b2cc65/Cars_Wow_4_360p.mp4"},"audio":"https://assets.ctfassets.net/bs8ntwkklfua/iJ5LIuyc3pmvEAaiSVSLS/85e36dc0324b28549ea56a6882a03062/Cars_Wow_4.mp3"}]


@pytest.fixture
def example_json_movie2():
    return [{"movie":"The Internship","year":2013,"release_date":"2013-05-29","director":"Shawn Levy","character":"Nick Campbell","movie_duration":"02:05:02","timestamp":"00:40:45","full_line":"Wow!","current_wow_in_movie":2,"total_wows_in_movie":5,"poster":"https://images.ctfassets.net/bs8ntwkklfua/6XhmTpc1PoiTf0q1nDYMyv/594947f72b4dba7f3c24938a680dd603/The_Internship_Poster.jpg","video":{"1080p":"https://videos.ctfassets.net/bs8ntwkklfua/2HrgjW55Ubyibrj5jWCONN/8cc67817fcf43821fa808f45f47b771d/The_Internship_Wow_2_1080p.mp4","720p":"https://videos.ctfassets.net/bs8ntwkklfua/1quea0uaxZG0XhG2OZHyiN/bc567d11211c484c57df81ebc2738da5/The_Internship_Wow_2_720p.mp4","480p":"https://videos.ctfassets.net/bs8ntwkklfua/7cVSPYGUbn5jm7Lab0lafw/b5071272d7146d70ab1dbf08f4a1319b/The_Internship_Wow_2_480p.mp4","360p":"https://videos.ctfassets.net/bs8ntwkklfua/6QCTva7iEh8WRGFRbOL62X/f7cbf460bc7f6841818390b0f5fdcf45/The_Internship_Wow_2_360p.mp4"},"audio":"https://assets.ctfassets.net/bs8ntwkklfua/2T6B1CgkHRARp0UT9ZTbct/c0019c6d2664f5d2f8baf7b1f95beb6d/The_Internship_Wow_2.mp3"}]


@pytest.fixture
def example_load_data():
    return [['Movie Name', 'Release Year', 'Rating', 'id'],
            ['Cars', '2006', '7.2', '11'],
            ['The Internship', '2013', '6.3', '22']]

@pytest.fixture
def example_write_data():
    return [['Movie Name', 'Release Year', 'Rating', 'id', 'Total Wows', 'Full Line'],
            ['Cars', '2006', '7.2', '11', '5', "Wow, you were right!"],
            ['The Internship', '2013', '6.3', '22', '5', 'Wow!']]


def test_merge_data(mocker, example_load_data, example_write_data, example_json_movie1, example_json_movie2):
    mocker.patch("app.main.get_account", side_effect=
    [example_json_movie1, example_json_movie2])
    assert merge_data(example_load_data) == example_write_data
