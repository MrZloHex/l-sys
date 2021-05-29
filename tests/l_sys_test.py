import unittest
from l_sys.l_sys import LSys


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.curve_coch = LSys(l_sys="curve_coch", iterations=2)
        self.triang_serp = LSys(l_sys="triangle_serpinskii", iterations=3)
        self.curve_serp = LSys(l_sys="curve_serpinskii", iterations=3)
        self.curve_drakon = LSys(l_sys="curve_drakon", iterations=4)
        self.pifs_tree = LSys(l_sys="pifagors_tree", iterations=3)

    def test_CurveCoch(self):
        result = self.curve_coch.make_seq()
        self.assertEqual(result, "f+f-f-f+f+f+f-f-f+f-f+f-f-f+f-f+f-f-f+f+f+f-f-f+f")  # noqa E501

    def test_TrianglSerpin(self):
        result = self.triang_serp.make_seq()
        self.assertEqual(result, "f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f-gggg+f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f+gggg-f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f-gggggggg-gggggggg")  # noqa E501

    def test_CurveSerpin(self):
        result = self.curve_serp.make_seq()
        self.assertEqual(result, "b-a-b+a+b+a+b-a-b-a+b+a-b-a-b-a+b+a-b-a-b+a+b+a+b-a-b")  # noqa E501

    def test_CurveDrakon(self):
        result = self.curve_drakon.make_seq()
        self.assertEqual(result, "fx+yf++-fx-yf++-fx+yf+--fx-yf++-fx+yf++-fx-yf+--fx+yf+--fx-yf+")  # noqa E501

    def test_PifsTree(self):
        result = self.pifs_tree.make_seq()
        self.assertEqual(result, "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0")


if __name__ == '__main__':
    unittest.main()
