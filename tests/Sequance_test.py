import unittest
from l_sys.Sequence import Sequence


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.curve_coch = Sequence(l_sys="curve_coch")
        self.triang_serp = Sequence(l_sys="triangle_serpinskii")

    def test_CurveCoch(self):
        result = self.curve_coch.make_seq(iterations=2)[0]
        self.assertEqual(result, "f+f-f-f+f+f+f-f-f+f-f+f-f-f+f-f+f-f-f+f+f+f-f-f+f")

    def test_TrianglSerpin(self)
        result = self.triang_serp.make_seq(iterations=3)[0]
        self.assertEqual(result, "f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f-gggg+f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f+gggg-f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f-gggggggg-gggggggg")


if __name__ == '__main__':
    unittest.main()
