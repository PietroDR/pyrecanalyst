#! /usr/bin/env python
# coding: utf-8

import unittest
from Model.VictorySettings import VictorySettings


class TestVictorySettings(unittest.TestCase):
    def test_get_victory_string(self):
        settings = VictorySettings(None)
        self.assertEqual(settings.get_victory_string(), "Standard")
