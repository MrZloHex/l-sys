import unittest
from l_sys.l_sys import LSys


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.curve_koch = LSys(l_sys="Koch curve", iterations=2)
        self.triangle_serp = LSys(l_sys="Sierpinski triangle", iterations=3)
        self.curve_serp = LSys(l_sys="Sierpinski curve", iterations=3)
        self.curve_dragon = LSys(l_sys="Dragon curve", iterations=4)
        self.bin_tree = LSys(l_sys="Binary tree", iterations=3)

    def test_KochCurve(self):
        result = self.curve_koch.make_seq()
        self.assertEqual(result, "f+f-f-f+f+f+f-f-f+f-f+f-f-f+f-f+f-f-f+f+f+f-f-f+f")  # noqa E501

    def test_TriangleSerp(self):
        result = self.triangle_serp.make_seq()
        self.assertEqual(result, "f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f-gggg+f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f+gggg-f-g+f+g-f-gg+f-g+f+g-f+gg-f-g+f+g-f-gggggggg-gggggggg")  # noqa E501

    def test_CurveSerp(self):
        result = self.curve_serp.make_seq()
        self.assertEqual(result, "b-a-b+a+b+a+b-a-b-a+b+a-b-a-b-a+b+a-b-a-b+a+b+a+b-a-b")  # noqa E501

    def test_CurveDragon(self):
        result = self.curve_dragon.make_seq()
        self.assertEqual(result, "fx+yf++-fx-yf++-fx+yf+--fx-yf++-fx+yf++-fx-yf+--fx+yf+--fx-yf+")  # noqa E501

    def test_BinTree(self):
        result = self.bin_tree.make_seq()
        self.assertEqual(result, "1111[11[1[0]0]1[0]0]11[1[0]0]1[0]0")

    def test_ErrorSys(self):
        self.assertRaises(ValueError, LSys, "qwe", 1)
        self.assertRaises(TypeError, LSys, 123, 1)


if __name__ == '__main__':
    unittest.main()
