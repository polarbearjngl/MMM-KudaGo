import enum


class Location(enum.Enum):
    """List of cities for which KudaGo collects interesting events and activities."""

    spb = 'spb'                  # Санкт - Петербург
    msk = 'msk'                  # Москва
    nsk = 'nsk'                  # Новосибирск
    ekb = 'ekb'                  # Екатеринбург
    nnv = 'nnv'                  # Нижний Новгород
    kzn = 'kzn'                  # Казань
    smr = 'smr'                  # Самара
    krd = 'krd'                  # Краснодар
    sochi = 'sochi'              # Сочи
    ufa = 'ufa'                  # Уфа
    krasnoyarsk = 'krasnoyarsk'  # Красноярск
    kev = 'kev'                  # Киев
