# Locode

## Overview

This module contains a series of json files with ISO_3166-1, ISO_3166-2 and 
city codes from http://www.unece.org/cefact/locode/service/location.html

## bdist_egg

`python setup.py bdist_egg` supports `--country=<country_code>` for creation 
of light weight eggs.

## Usage

```python
>>> import locode
>>> locode.get_country_code('United States')
u'US'
>>> locode.get_country_code('Angola')
u'AO'
>>> locode.get_country_code('Uruguay')
u'UY'
>>> locode.get_state_code('Montevideo', 'Uruguay')
u'MO'
>>> locode.get_state_code('Arizona', 'US')
u'AZ'
>>> locode.get_state_code('Saint John', 'AG')
u'04'
>>> locode.get_city_code('New York', 'NY', 'US')
u'NYC'
>>> locode.get_city_code('Punta Carretas', 'Montevideo', 'Uruguay')
u'PCA'
>>> locode.get_city_code('Ondjiva', 'Cunene', 'AO')
u'NGV'
```

```python
>>> locode.get_city_code('-', '-', '-')
u'XX'
>>> locode.get_state_code('-', '-')
u'XX'
>>> locode.get_country_code('-')
u'XX'
```
