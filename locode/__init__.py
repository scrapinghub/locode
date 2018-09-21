import json
import re
import os


_BASE_PATH = os.path.dirname(__file__)
NOT_FOUND = u'XX'

def _get_dict(filename, lower=False):
    try:
        with open(filename) as f:
            data = json.load(f)
            if lower:
                data = dict((key.lower(), val) for key, val in data.items())
            return data
    except IOError:
        return None

def _get_code(filename, text):
    data = _get_dict(filename, True)
    text = text.lower()
    if data is None:
        return NOT_FOUND
    value = data.get(text)
    if value:
        return value
    for char in ('/', ',', ' '):
        key = list(filter(lambda x: x.startswith(text + char), data.keys()))
        if len(key) == 1:
            return data[key[0]]
    return NOT_FOUND


def get_language_code(text):
    if not text:
        return NOT_FOUND
    data = {'English': 'EN'}
    return data.get(text, NOT_FOUND)


_re_country_code = re.compile(r'^[A-Z]{2}$')
def get_country_code(text):
    if not text:
        return NOT_FOUND
    if _re_country_code.match(text):
        return text
    return _get_code(os.path.join(_BASE_PATH, 'countries.json'), text)


_re_state_code = re.compile(r'^[A-Z0-9]{2}$')
def get_state_code(text, country):
    if not text:
        return NOT_FOUND
    if _re_state_code.match(text):
        return text
    country_code = get_country_code(country)
    if country_code == NOT_FOUND:
        return NOT_FOUND
    return _get_code(os.path.join(_BASE_PATH, country_code, 'states.json'), text)


_re_city_code = re.compile(r'^[A-Z]{3}$')
def get_city_code(text, state, country):
    if not text:
        return NOT_FOUND
    if _re_city_code.match(text):
        return text
    country_code = get_country_code(country)
    state_code = get_state_code(state, country_code)
    if any(NOT_FOUND == x for x in (country_code, state_code)):
        return NOT_FOUND
    return _get_code(os.path.join(_BASE_PATH, country_code, state_code + '.json'), text)


def get_countries():
    return _get_dict(os.path.join(_BASE_PATH, 'countries.json'))


_CODE_COUNTRY_MAP = {}
def get_country_by_code(code):
    if not _CODE_COUNTRY_MAP:
        for country, cd in get_countries().items():
            _CODE_COUNTRY_MAP[cd] = country
    return _CODE_COUNTRY_MAP[code]

def get_states(country):
    country_code = get_country_code(country)
    return _get_dict(os.path.join(_BASE_PATH, country_code, 'states.json'))


def get_cities(state, country):
    if not _re_country_code.match(country):
        country = get_country_code(country)
    if not _re_state_code.match(state):
        state = get_state_code(state, country)
    return _get_dict(os.path.join(_BASE_PATH, country, state + '.json'))
