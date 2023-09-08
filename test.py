from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase2(TestCase):
    def test_1(self):
        self.assertEqual(solution('rkqodlw', 'world'),True)
    def test_2(self):
        self.assertEqual(solution('cedewaraaossoqqyt', 'codewars'), True)
    def test_3(self):
        self.assertEqual(solution('katas', 'steak'),False)
    def test_4(self):
        self.assertEqual(solution('oneword',''),True)
    def test_5(self):
        self.assertEqual(solution('','oneword'),False)