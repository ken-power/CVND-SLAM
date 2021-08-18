import unittest

from robot_class import robot


class RobotTestCases(unittest.TestCase):

    def test_create_new_robot(self):
        r = robot()

        self.assertIsNotNone(r)

    def test_initial_location_of_robot(self):
        """
        This test defines a world and instantiate a robot, then checks the robot's location.

        Define a small 10x10 square world, a measurement range that is half that of the world and small
        values for motion and measurement noise. These values will typically be about 10 times larger, but for now
        we just want to demonstrate this behavior on a small scale.
        """
        world_size = 10.0  # size of world (square)
        measurement_range = 5.0  # range at which we can sense landmarks
        motion_noise = 0.2  # noise in robot motion
        measurement_noise = 0.2  # noise in the measurements

        # instantiate a robot, r
        r = robot(world_size, measurement_range, motion_noise, measurement_noise)

        # check the location of r
        self.assertEquals(5.0, r.x)
        self.assertEquals(5.0, r.y)


if __name__ == '__main__':
    unittest.main()
