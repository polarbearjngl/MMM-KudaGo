import json
import os
import shutil
from pathlib import Path

from kudago.api.entities.event import EventType
from kudago.api.methods.events import Events
from kudago.api.methods.places import Places


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class KudagoClient(metaclass=Singleton):
    """Client for accessing to KudaGo Api."""

    DATE_FORMAT = '%d.%m.%y %H:%M'
    DATE_FORMAT_SHORT = '%d.%m.%y'

    def __init__(self, location, categories, tags, create_qr_img=0):
        """Init object.

        Args:
            location: City for collecting events (see content of class Location)
            categories: Categories for classifying events (see content of class EventType).
            tags: Tags for events, separated by comma, for much more relevant search.
        """
        self.places = Places(client=self)
        self.tags = tags.split(',') if tags else []
        self.categories = []
        self.places_info = []
        self.events_info = []
        self.events_info_ids = []
        self.create_qr_img = create_qr_img
        categories = categories if isinstance(categories, list) else categories.split(',')
        for cat_name in categories:
            category = getattr(EventType, cat_name, None)
            if category is not None:
                self.categories.append(category.name)
                setattr(self, cat_name, Events(category=category.value, location=location, client=self))

    def collect_events(self, target_days):
        """Call collecting events for every category of KudagoClient, that was initialized.

        Args:
            target_days: Number of days, for creating interval (since today until target days).

        Returns:
            Collected events.
        """
        if self.create_qr_img:
            directory = str(Path(__file__).parent.parent.absolute()) + os.sep + "QR_img" + os.sep
            if os.path.exists(directory):
                shutil.rmtree(directory)
        for category in self.categories:
            events_obj = getattr(self, category, None)
            if events_obj is not None:
                events_obj.get_events(target_days=target_days)

        return self.events_info

    def write_events_to_file(self, filename):
        """Write collected events info in file with given name and extension.

        Args:
            filename: Name of result file.
        """
        directory = str(Path(__file__).parent.parent.absolute()) + os.sep
        open(directory + filename, 'w', encoding='utf-8').close()
        if self.events_info:
            events = sorted(self.events_info, key=lambda c: c.date)
            with open(directory + filename, 'w', encoding='utf-8') as f:
                json.dump([c.to_dict() for c in events], f, ensure_ascii=False, indent=4)
