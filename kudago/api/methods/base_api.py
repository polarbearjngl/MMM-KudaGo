import requests
from json import JSONDecodeError
from requests import HTTPError


class BaseApi(object):
    """Base API class."""

    API_URL = 'https://kudago.com/public-api'
    VER_1_4 = '/v1.4'
    LANG = 'ru'

    @staticmethod
    def _request(method, url, is_decode_to_json=True, params=None, headers=None, data=None, **kwrags):
        resp = requests.request(method=method,
                                url=url,
                                params=params,
                                headers=headers,
                                data=data,
                                **kwrags)
        try:
            resp.raise_for_status()
            if not is_decode_to_json:

                return resp

            content = resp.json()
        except (HTTPError, JSONDecodeError) as error:
            return error

        return content
