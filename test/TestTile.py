#! /usr/bin/env python
# coding: utf-8

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from Model.Tile import Tile


class TestTile(unittest.TestCase):
    def test_tile_creation(self):
        tile = Tile(5, -5, 1, 0)
        self.assertEqual(tile.x, 5)
        self.assertEqual(tile.y, -5)
        self.assertEqual(tile.terrain, 1)
        self.assertEqual(tile.elevation, 0)
