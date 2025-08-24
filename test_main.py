import unittest
from main import greet

class TestGreeting(unittest.TestCase):
    def test_basic_greeting(self):
        """Перевірка базового привітання"""
        self.assertEqual(greet("Іван"), "Привіт, Іван!")
        
    def test_empty_name(self):
        """Перевірка порожнього імені"""
        self.assertEqual(greet(""), "Привіт, !")
        
    def test_special_characters(self):
        """Перевірка спеціальних символів у імені"""
        self.assertEqual(greet("Марія-Анна"), "Привіт, Марія-Анна!")

if __name__ == '__main__':
    unittest.main()
