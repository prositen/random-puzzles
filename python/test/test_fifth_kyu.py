import unittest

from python import fifth_kyu


class Test5Kyu(unittest.TestCase):
    def test_palindrome_chain_length(self):
        self.assertEquals(4, fifth_kyu.palindrome_chain_length(87))

    def test_valid_parentheses(self):
        self.assertEquals(fifth_kyu.valid_parentheses("  ("), False)
        self.assertEquals(fifth_kyu.valid_parentheses(")test"), False)
        self.assertEquals(fifth_kyu.valid_parentheses(""), True)
        self.assertEquals(fifth_kyu.valid_parentheses("hi())("), False)
        self.assertEquals(fifth_kyu.valid_parentheses("hi(hi)()"), True)

    def test_bowling_score(self):
        self.assertEqual(0, fifth_kyu.bowling_score([0] * 20))
        self.assertEqual(190, fifth_kyu.bowling_score([9, 1] * 10 + [9]))
        self.assertEqual(300, fifth_kyu.bowling_score([10] * 12))
        self.assertEqual(11, fifth_kyu.bowling_score([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0]))
        self.assertEqual(12, fifth_kyu.bowling_score([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0]))

    def test_caesar_cipher(self):
        c = fifth_kyu.CaesarCipher(5);

        self.assertEquals(c.encode('Codewars'), 'HTIJBFWX')
        self.assertEquals(c.decode('HTIJBFWX'), 'CODEWARS')
