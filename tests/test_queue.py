from unittest import TestCase

from lib.queue import queue
from lib.utils import randColor


class TestQueue(TestCase):

    def test_push(self):
        q_max = 10
        q = queue([1 for i in range(q_max)], q_max)

        for _ in range(q_max * 2):
            q.push(2)

        self.assertListEqual(list(q), [2 for _ in range(q_max)])

    def test_pop_empty_queue(self):
        q = queue([], 10)
        self.assertEqual(q.pop(), None)
        self.assertListEqual(list(q), [])

    def test_pop_returns_item(self):
        item = randColor()
        q = queue([item], 13)
        returned = q.pop()
        self.assertEqual(item, returned)

    def test_pop_empty(self):
        q = queue([], 35)
        returned = q.pop()
        self.assertListEqual(list(q), [])
        self.assertEqual(returned, None)

    def test_pop_single(self):
        items = [1]
        q = queue(items, 53)
        returned = q.pop()
        self.assertListEqual(list(q), [])
        self.assertEqual(returned, 1)

    def test_clear_empty(self):
        q = queue([], 32)
        q.clear()
        self.assertListEqual(list(q), [])

    def test_clear_many(self):
        q = queue([i for i in range(100)], 100)
        q.clear()
        self.assertListEqual(list(q), [])

    def test_insert_0(self):
        q = queue([9999], None)
        q.insert(0, 1)
        expected = [1, 9999]
        self.assertListEqual(list(q), expected)

    def test_insert_1(self):
        q = queue([9999], None)
        q.insert(1, 1234)
        expected = [9999, 1234]
        self.assertListEqual(list(q), expected)

    def test_insert_index_exceeds_maximum(self):
        max_len = 1
        q = queue([9999], max_len)
        q.insert(9, 1234)
        expected = [9999]
        self.assertListEqual(list(q), expected)

