#!/usr/bin/env python
# -*- coding: utf-8 -*-

{% set test_formula_name=cookiecutter.repo_name.replace('-','_') %}

"""
test_{{ test_formula_name }}
----------------------------------

Tests for `{{ test_formula_name }}` module.
"""

import unittest

from {{ test_formula_name }} import {{ test_formula_name }}


class Test{{ test_formula_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
