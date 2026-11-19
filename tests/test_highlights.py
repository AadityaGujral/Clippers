import unittest
from app.highlights import fixed_segments


class FixedSegmentTests(unittest.TestCase):
    def test_segments(self):
        self.assertEqual(fixed_segments(70, 30, 4), [(0, 30), (30, 60), (60, 70)])

    def test_empty_duration_rejected(self):
        with self.assertRaises(ValueError):
            fixed_segments(0)


if __name__ == "__main__":
    unittest.main()
