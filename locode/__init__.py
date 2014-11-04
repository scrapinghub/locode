import json
import re
import os


_BASE_PATH = os.path.dirname(__file__)
NOT_FOUND = u'XX'


def _get_code(data, text):
    value = data.get(text)
    if value:
        return value
    for char in ('/', ',', ' '):
        key = filter(lambda x: x.startswith(text + char), data.keys())
        if len(key) == 1:
            return data[key[0]]
    return NOT_FOUND


def get_language_code(text):
    if not text:
        return NOT_FOUND
    data = {'English': 'EN'}
    return _get_code(data, text)


_re_country_code = re.compile(r'^[A-Z]{2}$')
def get_country_code(text):
    if not text:
        return NOT_FOUND
    if _re_country_code.match(text):
        return text
    with open(os.path.join(_BASE_PATH, 'countries.json')) as f:
        data = json.load(f)
    return _get_code(data, text)


_re_state_code = re.compile(r'^[A-Z]{2}$')
def get_state_code(text, country):
    if not text:
        return NOT_FOUND
    if _re_state_code.match(text):
        return text
    country_code = get_country_code(country)
    if country_code == NOT_FOUND:
        return NOT_FOUND
    with open(os.path.join(_BASE_PATH, country_code, 'states.json')) as f:
        data = json.load(f)
    return _get_code(data, text)


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
    with open(os.path.join(_BASE_PATH, country_code, state_code + '.json')) as f:
        data = json.load(f)
    return _get_code(data, text)
