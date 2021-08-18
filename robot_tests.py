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

    def test_initial_location_of_robot_world_size_20(self):
        """
        This test defines a world and instantiate a robot, then checks the robot's location. Same as previous test,
        except world size is 20x20.

        """
        world_size = 20.0  # size of world (square)
        measurement_range = 5.0  # range at which we can sense landmarks
        motion_noise = 0.2  # noise in robot motion
        measurement_noise = 0.2  # noise in the measurements

        # instantiate a robot, r
        r = robot(world_size, measurement_range, motion_noise, measurement_noise)

        # check the location of r
        self.assertEquals(10.0, r.x)
        self.assertEquals(10.0, r.y)

    def test_initial_location_of_robot_is_center_of_world(self):
        """
        Defines a list of world sizes and verifies tjat the robot's initial location is at the center.
        """
        world_sizes = [20.0, 25.0, 30.0, 37.3, 42.002, 51.9, 104,34, 214,53]

        for size in world_sizes:
            # instantiate a robot, r
            r = robot(world_size=size)

            # check the location of r
            self.assertEquals(size/2, r.x)
            self.assertEquals(size/2, r.y)


if __name__ == '__main__':
    unittest.main()
