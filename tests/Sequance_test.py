import unittest
from l_sys.Sequence import Sequence


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.seq = Sequence(l_sys="coch", iterations=2)

    def right_seq(self):
        result = self.seq.make_seq()[0]
        self.assertEqual(result, "f+f-f-f+f+f+f-f-f+f-f+f-f-f+f-f+f-f-f+f+f+f-f-f+f")


if __name__ == '__main__':
    unittest.main()
