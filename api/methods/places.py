from json import JSONDecodeError

from requests import HTTPError

from api.entities.place import Place
from api.methods.base_api import BaseApi


class Places(BaseApi):

    PLACES = '/places/%s'
    FIELDS = 'id,title'

    def __init__(self,
                 client):
        self.client = client
        self.url = self.API_URL + self.VER_1_4 + self.PLACES

    def get_place(self, place_info):
        """Получить информацию о месте проведения события.

        Args:
            place_info: идентификатор

        Returns:
            Название места проведения события.

        """
        if place_info is not None:
            place = [p for p in self.client.places_info if p.id == place_info.get('id')]
            if place:
                return place[0].title
            else:
                place = self._get_place(place_id=place_info.get('id'))
                if place is None:
                    return None
                self.client.places_info.append(place)
                return place.title
        else:
            return ''

    def _get_place(self,
                   place_id):
        """Отправка запроса на получение информации о месте проведения события.

        Args:
            place_id: идентификатор

        Returns:
            Информация о месте проведения события.

        """
        params = {
            'lang': self.LANG,
            'fields': self.FIELDS,
        }
        place = self._request(method='GET', url=self.url % place_id, params=params)
        if not isinstance(place, (HTTPError, JSONDecodeError)):
            return Place(**place)
        else:
            return None
