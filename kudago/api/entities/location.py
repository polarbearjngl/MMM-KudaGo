import enum


class Location(enum.Enum):
    """List of cities for which KudaGo collects interesting events and activities."""

    spb = 'spb'                  # St. Petersburg
    msk = 'msk'                  # Moscow
    nsk = 'nsk'                  # Novosibirsk
    ekb = 'ekb'                  # Yekaterinburg
    nnv = 'nnv'                  # Nizhny Novgorod
    kzn = 'kzn'                  # Kazan
    smr = 'smr'                  # Samara
    krd = 'krd'                  # Krasnodar
    sochi = 'sochi'              # Sochi
    ufa = 'ufa'                  # Ufa
    krasnoyarsk = 'krasnoyarsk'  # Krasnoyarsk
    kev = 'kev'                  # Kiev
