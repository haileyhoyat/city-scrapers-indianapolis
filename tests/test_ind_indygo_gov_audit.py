from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import BOARD  # noqa
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.ind_indygo_gov_audit import IndIndygoGovAuditSpider

test_response = file_response(
    join(dirname(__file__), "files", "ind_indygo_gov_audit.html"),
    url="https://www.indygo.net/about-indygo/board-of-directors/",
)
spider = IndIndygoGovAuditSpider()

freezer = freeze_time("2023-08-10")
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
    assert parsed_items[0]["title"] == "IndyGo Governance and Audit Committee"


def test_description():
    assert parsed_items[0]["description"] == ""


def test_start():
    assert parsed_items[0]["start"] == datetime(2024, 1, 18, 13, 0)


# def test_end():
#     assert parsed_items[0]["end"] == datetime(2019, 1, 1, 0, 0)


def test_time_notes():
    assert parsed_items[0]["time_notes"] == ""  # noqa  # noqa


def test_id():
    assert (
        parsed_items[0]["id"]
        == "ind_indygo_gov_audit/202401181300/x/indygo_governance_and_audit_committee"  # noqa
    )


def test_status():
    assert parsed_items[0]["status"] == "tentative"


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
        },
        {
            "href": "https://public.onboardmeetings.com/Group/HrdLpC4rmFdYrgplGJZm82TtkS14OCvw7QLcFFPpPrIA/TQhh8dVF3IFGmqPt9KPGgkEFwuhy9cHXFm5%2FFdjTKHsA",  # noqa
            "title": "Past Governance Audit Committee packets",
        },
    ]


def test_classification():
    assert parsed_items[0]["classification"] == None  # noqa


@pytest.mark.parametrize("item", parsed_items)
def test_all_day(item):
    assert item["all_day"] is False
