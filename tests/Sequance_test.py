import unittest
from l_sys.Sequence import Sequence


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.curve_coch = Sequence(l_sys="curve_coch")
        self.triang_serp = Sequence(l_sys="triangle_serpinskii")
        self.curve_serp = Sequence(l_sys="curve_serpinskii")
        self.curve_drakon = Sequence(l_sys="curve_drakon")
        self.pifs_tree = Sequence(l_sys="pifagors_tree")

    def test_CurveCoch(self):
        result = self.curve_coch.make_seq(iterations=2)
        self.assertEqual(result, "f+f-f-f+f+f+f-f-f+f-f+f-f-f+f-f+f-f-f+f+f+f-f-f+f")

    def test_TrianglSerpin(self):
        result = self.triang_serp.make_seq(iterations=3)
        self.assertEqual(result, "f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f-gggg+f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f+gggg-f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f-gggggggg-gggggggg")

    def test_CurveSerpin(self):
        result = self.curve_serp.make_seq(iterations=3)
        self.assertEqual(result, "b-a-b+a+b+a+b-a-b-a+b+a-b-a-b-a+b+a-b-a-b+a+b+a+b-a-b")

    def test_CurveDrakon(self):
        result = self.curve_drakon.make_seq(iterations=4)
        self.assertEqual(result, "fx+yf++-fx-yf++-fx+yf+--fx-yf++-fx+yf++-fx-yf+--fx+yf+--fx-yf+")

    def test_PifsTree(self):
        result = self.pifs_tree.make_seq(iterations=3)
        self.assertEqual(result, "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0")


if __name__ == '__main__':
    unittest.main()
