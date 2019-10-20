import pytest

from kudago.api.entities.event import EventType
from kudago.api.entities.location import Location
from kudago.api.kudago_client import KudagoClient


@pytest.fixture(scope='session')
def kudago_client():
    categories = ','.join([EventType.concert.name, EventType.business_events.name, EventType.stand_up.name, EventType.speed_dating.name])
    client = KudagoClient(location=Location.spb.value, categories=categories)
    yield client


@pytest.mark.parametrize(
    'existed_categories, categories_api_names',
    [pytest.param(['business_events', 'stand_up', 'speed_dating'],
                  ['business-events', 'stand-up', 'speed-dating'])])
def test_client_event_categories(kudago_client, existed_categories, categories_api_names):
    assert len(kudago_client.categories) == 4
    for not_e_cat in categories_api_names:
        assert getattr(kudago_client, not_e_cat, None) is None

    for e_cat in existed_categories:
        events_obj = getattr(kudago_client, e_cat, None)
        assert events_obj is not None
        assert events_obj.category in categories_api_names


def test_client_collect_target_days_greater_null(kudago_client):
    kudago_client.concert.get_events(target_days=1)
    assert len(kudago_client.events_info) > 0
    assert len(kudago_client.places_info) > 0
    assert len(kudago_client.events_info_ids) > 0


def test_client_collect_target_days_less_null(kudago_client):
    business_events = kudago_client.business_events.get_events(target_days=-1)
    assert len(business_events) == 0
    assert len(business_events) == 0
    assert len(business_events) == 0
