from json import JSONDecodeError
from requests import HTTPError
from api.entities.event import Event
from api.methods.base_api import BaseApi
from datetime import timezone, datetime, timedelta


class Events(BaseApi):
    """Object for collecting events by given category (see content of class EventType)."""

    EVENTS = '/events'
    PAGE_SIZE = 100
    FIELDS = 'id,title,dates,place,location,price,categories,is_free'

    def __init__(self,
                 client,
                 category,
                 location):
        """Init object.

        Args:
            client: Client for accessing to KudaGo Api.
            category: Category for classifying event of this obj (see content of class EventType).
            location: City for collecting events (see content of class Location).
        """
        self.client = client
        self.category = category
        self.location = location
        self.url = self.API_URL + self.VER_1_4 + self.EVENTS
        self.collected_events = []

    def get_events(self,
                   target_days,
                   page_size=None,
                   url=None):
        u"""Get a list of events relevant since today for a given number of days.

        Args:
            target_days: Number of days, for creating interval (since today until target days).
            page_size: Number of elements on one page of response.
            url: Request sending address.

        Returns:
            List of events.
        """
        if target_days < 0:
            return []

        target_days = int(target_days)
        since = datetime.now(tz=timezone.utc).timestamp()
        until = (datetime.now(tz=timezone.utc) + timedelta(days=target_days)).timestamp()
        params = {
            'lang': self.LANG,
            'page_size': self.PAGE_SIZE if page_size is None else page_size,
            'categories': self.category,
            'location': self.location,
            'fields': self.FIELDS,
            'actual_since': since,
            'actual_until': until
        }
        events = self._request(method='GET',
                               url=self.url if url is None else url,
                               params=params)
        self.collected_events.extend(events['results'])
        if events['next']:
            self.get_events(target_days=target_days,
                            page_size=page_size,
                            url=events['next'])
        if not isinstance(events, (HTTPError, JSONDecodeError)):
            return [Event(client=self.client, since=since, until=until, **info)
                    for info in self.collected_events
                    if info['id'] not in self.client.events_info_ids]
        else:
            return []
