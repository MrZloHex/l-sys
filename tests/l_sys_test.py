import unittest
from l_sys.l_sys import LSys


class TestLSys(unittest.TestCase):
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
        self.assertEqual(result, "g-f-g+f+g+f+g-f-g-f+g+f-g-f-g-f+g+f-g-f-g+f+g+f+g-f-g")  # noqa E501

    def test_CurveDragon(self):
        result = self.curve_dragon.make_seq()
        self.assertEqual(result, "fx+yf++-fx-yf++-fx+yf+--fx-yf++-fx+yf++-fx-yf+--fx+yf+--fx-yf+")  # noqa E501

    def test_BinTree(self):
        result = self.bin_tree.make_seq()
        self.assertEqual(result, "ffff[+ff[+f[+g]-g]-f[+g]-g]-ff[+f[+g]-g]-f[+g]-g")  # noqa

    def test_ErrorSys(self):
        self.assertRaises(ValueError, LSys, "qwe", 1)
        self.assertRaises(ValueError, LSys, "koch curve", 1)
        self.assertRaises(TypeError, LSys, 123, 1)
        self.assertRaises(TypeError, LSys, True, 1)

    def test_ErrorIter(self):
        self.assertRaises(ValueError, LSys, "Koch curve", -3)
        self.assertRaises(ValueError, LSys, "Koch curve", -678)
        self.assertRaises(TypeError, LSys, "Koch curve", True)
        self.assertRaises(TypeError, LSys, "Koch curve", "qwe")


if __name__ == '__main__':
    unittest.main()
