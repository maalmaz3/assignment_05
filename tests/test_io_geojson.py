import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import io_geojson

class TestIoGeoJson(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.gj = io_geojson.read_geojson('data/us_cities.geojson')
	def test_read_geojson(self):
		self.assertIsInstance(self.gj, dict)