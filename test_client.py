import unittest
from client import create_presence, process_ans, c_adress_cheker, c_port_cheker
import time


class TestClient(unittest.TestCase):
    def test_create_presence(self):
        self.assertEqual(create_presence(),
                         {'action': 'presence', 'time': time.time(), 'user': {'account_name': 'Guest'}})

    def test_process_ans(self):
        message = {'response': 200}
        self.assertEqual(process_ans(message), '200 : OK')

    def test_bad_process_ans(self):
        message = {'response': 400, 'error': 'ошибка'}
        self.assertEqual(process_ans(message), '400 : ошибка')

    def test_c_adress_cheker(self):
        self.assertEqual(c_adress_cheker(), '127.0.0.1')

    def test_c_port_cheker(self):
        self.assertEqual(c_port_cheker(), 7777)


if __name__ == '__main__':
    unittest.main()
