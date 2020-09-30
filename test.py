
import pytest

from API import API

api = API()

def test_total_analysis():
    urls = ["https://www.sueddeutsche.de/wirtschaft/bahn-milliarden-ausbau-1.5029830"]
    assert isinstance(api.news_analysis(urls), dict)
