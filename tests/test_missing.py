import json
import os
import unittest

import locode


class TestMissing(unittest.TestCase):

    _BASE_PATH = os.path.dirname(locode.__file__)

    def test_missing_countries(self):
        with open(os.path.join(self._BASE_PATH, 'countries.json')) as f:
            data = json.load(f
                    )
        list_dir = [x for x in os.listdir(self._BASE_PATH)
                if not any(y in x for y in ('__init__.py', 'countries.json'))]
        self.assertListEqual(sorted(data.values()), sorted(list_dir))

    def test_missing_states(self):
        for country_folder in sorted(os.listdir(self._BASE_PATH)):
            if len(country_folder) != 2:
                continue

            country_folder = os.path.join(self._BASE_PATH, country_folder)
            with open(os.path.join(country_folder, 'states.json')) as f:
                data = json.load(f)

            list_dir = [x.split('.')[0] for x in os.listdir(country_folder)
                    if not any(y in x for y in ('__init__.py', 'states.json'))]
            print sorted(data.values()), sorted(list_dir)
            self.assertListEqual(sorted(data.values()), sorted(list_dir),
                    msg=country_folder)


if __name__ == '__main__':
    unittest.main()
