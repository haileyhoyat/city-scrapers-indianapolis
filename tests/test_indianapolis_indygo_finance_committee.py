from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import BOARD
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.indianapolis_indygo_finance_committee import (
    IndianapolisIndygoFinanceCommitteeSpider,
)

test_response = file_response(
    join(dirname(__file__), "files", "indianapolis_indygo_finance_committee.html"),
    url="https://www.indygo.net/about-indygo/board-of-directors/",
)
spider = IndianapolisIndygoFinanceCommitteeSpider()

freezer = freeze_time("2023-07-22")
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()


"""
Uncomment below

def test_tests():
    print("Please write some tests for this spider or at least disable this one.")
    assert False
"""


def test_title():
    assert parsed_items[0]["title"] == "IndyGo Finance Committee"


def test_description():
    assert parsed_items[0]["description"] == ""


def test_start():
    assert parsed_items[0]["start"] == datetime(2023, 1, 19, 8, 0)


# def test_end():
#     assert parsed_items[0]["end"] == datetime(2019, 1, 1, 0, 0)


def test_time_notes():
    assert (
        parsed_items[0]["time_notes"]
        == "Board meetings are set for 8:30AM unless otherwise noted in meeting description. Please double check the website before the meeting date."  # noqa
    )


def test_id():
    assert (
        parsed_items[0]["id"]
        == "indianapolis_indygo_finance_committee/202301191700/x/indygo_finance_committee"  # noqa
    )


def test_status():
    assert parsed_items[0]["status"] == "passed"


def test_location():
    assert parsed_items[0]["location"] == {
        "name": "Administrative Office - Board Room",
        "address": "1501 W. Washington St. Indianapolis, IN 46222",
    }


def test_source():
    assert (
        parsed_items[0]["source"]
        == "https://www.indygo.net/about-indygo/board-of-directors/"
    )


def test_links():
    assert parsed_items[0]["links"] == [
        {
            "href": "https://www.indygo.net/about-indygo/board-of-directors/",
            "title": "Meeting Page",
        }
    ]


def test_classification():
    assert parsed_items[0]["classification"] == BOARD


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
