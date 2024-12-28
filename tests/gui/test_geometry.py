import unittest
from src.gui.geometry import GeometryBuilder, Vector
import random 
class TestGeometry(unittest.TestCase):
    def test_builder(self):
        screen = Vector(1000, 1000)

        geometry_string = GeometryBuilder(screen) \
            .shape(1000, 1000) \
            .build()
        self.assertEqual(geometry_string, "1000x1000+0+0")

        geometry_string = GeometryBuilder(screen) \
            .shape(1000,1000) \
            .position(100, 100) \
            .build()
        self.assertEqual(geometry_string, "1000x1000+100+100") 

        geometry_string = GeometryBuilder(screen) \
            .shape(500, 500) \
            .center() \
            .build()
        self.assertEqual(geometry_string, "500x500+250+250")
