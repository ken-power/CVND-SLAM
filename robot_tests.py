import unittest

from robot_class import robot


class RobotTestCases(unittest.TestCase):

    def test_create_new_robot(self):
        r = robot()

        self.assertIsNotNone(r)


if __name__ == '__main__':
    unittest.main()
