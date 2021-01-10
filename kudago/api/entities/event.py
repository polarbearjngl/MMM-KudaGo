import enum
import os
from datetime import datetime
from pathlib import Path
import qrcode

from kudago.api.entities.base_entity import KudagoBase


class Event(KudagoBase):
    """Event for which companies provide information."""

    def __init__(self, client, since, until, **kwargs):
        """Init object.

        Args:
            client: Client for accessing to KudaGo Api.
            since: Timestamp for start of event searching interval.
            until: Timestamp for end of event searching interval.

        Kwargs:
            id: Identifier
            title: Name of event.
            dates: Dates of event.
            place: Place of event.
            location: City of event (see content of class Location).
            price: Price for event.
            categories: Category for classifying event (see content of class EventType).
            is_free: Information about free access to event.
        """
        self.client = client
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.tags = kwargs.get('tags')
        self.is_free = kwargs.get('is_free')
        self.price = 'Бесплатно' if self.is_free and not kwargs.get('price') else kwargs.get('price')
        self.location = kwargs.get('location').get('slug')
        self.categories = ','.join(kwargs.get('categories'))
        self.date = self.convert_dates(kwargs.get('dates'), since=since, until=until)
        self.place = client.places.get_place(place_info=kwargs.get('place'))
        self.site_url = kwargs.get('site_url')
        self.qr_img_path = None

        self._id_attrs = (self.id, )
        self.client.events_info.append(self)
        self.client.events_info_ids.append(self.id)
        self.create_qr_image()

    def convert_dates(self, dates, since, until):
        """Converts date for event from timestamp in given format.

        Args:
            dates: Dates of event.
            since: Timestamp for start of event searching interval.
            until: Timestamp for end of event searching interval.

        Returns:
            Converted date.
        """
        ftimestamp = datetime.fromtimestamp
        event_date = [(ftimestamp(date['start']).strftime(self.client.DATE_FORMAT)) for date in dates
                      if since < date['start'] <= until]
        return event_date[0] if event_date else ftimestamp(since).strftime(self.client.DATE_FORMAT_SHORT)

    def create_qr_image(self):
        if self.client.create_qr_img:
            directory = str(Path(__file__).parent.parent.absolute()) + os.sep + "QR_img" + os.sep
            qr = qrcode.QRCode(box_size=2, border=3)
            qr.add_data(self.site_url)
            qr.make()
            img = qr.make_image(fill_color="black", back_color="white")
            Path(directory).mkdir(parents=True, exist_ok=True)
            img.save(directory + str(self.id))
            self.qr_img_path = directory + str(self.id)

    def __str__(self):
        return '\n'.join([self.title, self.date, self.place, self.price])


class EventType(enum.Enum):
    """There are various categories for classifying events and places."""

    concert = 'concert'                              # Концерты
    theater = 'theater'                              # Спектакли
    party = 'party'                                  # Ночная жизнь
    exhibition = 'exhibition'                        # Выставки
    festival = 'festival'                            # Фестивали
    show = 'show'                                    # Шоу (Развлечения)
    games = 'games'                                  # Игры (Развлечения)
    night = 'night'                                  # Ночь
    evening = 'evening'                              # Творческие вечера
    quest = 'quest'                                  # Квесты
    stand_up = 'stand-up'                            # Стендап (Развлечения)
    ball = 'ball'                                    # Балы (Развлечения)
    business_events = 'business-events'              # События для бизнеса
    circus = 'circus'                                # Цирковые представления (Развлечения)
    comedy_club = 'comedy-club'                      # Comedy club / Камеди клаб (Развлечения)
    dance_trainings = 'dance-trainings'              # Занятия танцами (Раздел Отдых
    education = 'education'                          # Обучение
    entertainment = 'entertainment'                  # Развлечения
    fashion = 'fashion'                              # Мода и стиль
    flashmob = 'flashmob'                            # Флешмобы (Развлечения)
    holiday = 'holiday'                              # Праздники
    kids = 'kids'                                    # Детям
    kvn = 'kvn'                                      # КВН (Развлечения)
    magic = 'magic'                                  # Фокусники, иллюзионисты (Развлечения)
    masquerade = 'masquerade'                        # Маскарады (Развлечения)
    meeting = 'meeting'                              # Встречи
    open = 'open'                                    # Дни открытых дверей
    other = 'other'                                  # Разное
    permanent_exhibitions = 'permanent-exhibitions'  # Постоянные выставки
    photo = 'photo'                                  # Фотография
    presentation = 'presentation'                    # Презентации
    recreation = 'recreation'                        # Отдых
    romance = 'romance'                              # Романтика (Развлечения)
    sale = 'sale'                                    # Распродажа (Магазины)
    social_activity = 'social-activity'              # Благотворительность
    speed_dating = 'speed-dating'                    # Быстрые свидания (Развлечения)
    sport = 'sport'                                  # Активный отдых
    tour = 'tour'                                    # Экскурсии
    yarmarki = 'yarmarki-razvlecheniya-yarmarki'     # Ярмарки (Развлечения, Ярмарки)
    yoga = 'yoga'                                    # Йога
