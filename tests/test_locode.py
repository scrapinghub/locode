import json
import os
import unittest

import locode


class TestLocode(unittest.TestCase):

    _BASE_PATH = os.path.dirname(locode.__file__)
    def test_case_insensitive(self):
        self.assertEqual(locode.get_country_code('UNITED STATES'), 'US')
        self.assertEqual(locode.get_state_code('CALIFORNIA', 'UNITED STATES'), 'CA')

if __name__ == '__main__':
    unittest.main()
