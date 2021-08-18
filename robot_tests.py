import unittest

from robot_class import robot


class RobotInitializations(unittest.TestCase):

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
        self.assertEqual(5.0, r.x)
        self.assertEqual(5.0, r.y)

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
        self.assertEqual(10.0, r.x)
        self.assertEqual(10.0, r.y)

    def test_initial_location_of_robot_is_center_of_world(self):
        """
        Defines a list of world sizes and verifies tjat the robot's initial location is at the center.
        """
        world_sizes = [20.0, 25.0, 30.0, 37.3, 42.002, 51.9, 104, 34, 214, 53]

        for size in world_sizes:
            # instantiate a robot, r
            r = robot(world_size=size)

            # check the location of r
            self.assertEqual(size / 2, r.x)
            self.assertEqual(size / 2, r.y)


class RobotMovementTests(unittest.TestCase):

    def setUp(self) -> None:
        world_size = 10.0  # size of world (square)
        measurement_range = 5.0  # range at which we can sense landmarks
        motion_noise = 0.2  # noise in robot motion
        measurement_noise = 0.2  # noise in the measurements

        self.noise_threshold = 2.0  # measurement noise can be between -1.0 and 1.0

        # instantiate a robot, r
        self.r = robot(world_size, measurement_range, motion_noise, measurement_noise)

    def test_move_robot_x1_y2(self):
        # choose values of dx and dy (negative works, too)
        dx = 1
        dy = 2
        is_moved = self.r.move(dx, dy)

        # Remember, there will be a random noise component to the measurements, so we won't get these exact values
        expected_x = 6.0
        expected_y = 7.0

        # print out the exact location
        self.assertTrue(is_moved)
        self.assertAlmostEqual(expected_x, self.r.x, delta=self.noise_threshold)
        self.assertAlmostEqual(expected_y, self.r.y, delta=self.noise_threshold)

    def test_move_robot_x4_y_neg2(self):
        # choose values of dx and dy (negative works, too)
        dx = 4
        dy = -2
        is_moved = self.r.move(dx, dy)

        # Remember, there will be a random noise component to the measurements, so we won't get these exact values
        expected_x = 8.0
        expected_y = 3.0

        # print out the exact location
        self.assertTrue(is_moved)
        self.assertAlmostEqual(expected_x, self.r.x, delta=self.noise_threshold)
        self.assertAlmostEqual(expected_y, self.r.y, delta=self.noise_threshold)


class LandmarksTests(unittest.TestCase):
    """
    Tests for creating landmarks, which are measurable features in the map. You can think of landmarks as things like
    notable buildings, or something smaller such as a tree, rock, or other feature.

    The robot class has a function `make_landmarks` which randomly generates locations for the number of specified
    landmarks.  We have to pass these locations as a third argument to the `display_world` function and the list of landmark locations is accessed similar to how we find the robot position `r.landmarks`.

    Each landmark has an `[x, y]` locations.
    """

    def setUp(self) -> None:
        world_size = 10.0  # size of world (square)
        measurement_range = 5.0  # range at which we can sense landmarks
        motion_noise = 0.2  # noise in robot motion
        measurement_noise = 0.2  # noise in the measurements

        self.noise_threshold = 2.0  # measurement noise can be between -1.0 and 1.0

        # instantiate a robot, r
        self.r = robot(world_size, measurement_range, motion_noise, measurement_noise)

    def test_create_3_landmarks(self):
        # create any number of landmarks
        num_landmarks = 3
        self.r.make_landmarks(num_landmarks)

        self.assertEqual(num_landmarks, len(self.r.landmarks))

        # The landmarks are generated in random locations, so we can make sure they are at least within the world grid
        for landmark in self.r.landmarks:
            self.assertTrue(landmark[0] <= self.r.world_size)
            self.assertTrue(landmark[1] <= self.r.world_size)

    def test_create_5_landmarks(self):
        # create any number of landmarks
        num_landmarks = 5
        self.r.make_landmarks(num_landmarks)

        self.assertEqual(num_landmarks, len(self.r.landmarks))

        # The landmarks are generated in random locations, so we can make sure they are at least within the world grid
        for landmark in self.r.landmarks:
            self.assertTrue(landmark[0] <= self.r.world_size)
            self.assertTrue(landmark[1] <= self.r.world_size)


class RobotSenseTests(unittest.TestCase):
    """
    Once we have some landmarks to sense, we need to be able to tell our robot to try to sense how far
    they are away from those landmarks.

    The measurements have the format, `[i, dx, dy]` where `i` is the landmark index (0, 1, 2, ...) and `dx` and `dy`
    are the measured distance between the robot's location (x, y) and the landmark's location (x, y). This distance
    will not be perfect since our sense function has some associated `measurement noise`.

    In these tests, we have a given our robot a range of `measurement_range` so any landmarks that are within that
    range of our robot's location, should appear in a list of measurements. Not all landmarks are guaranteed to be
    in our visibility range, so this list will be variable in length.

    Note: the robot's location is often called the **pose** or `[Pxi, Pyi]` and the landmark locations are often
    written as `[Lxi, Lyi]`.
    """

    def setUp(self) -> None:
        world_size = 10.0  # size of world (square)
        measurement_range = 5.0  # range at which we can sense landmarks
        motion_noise = 0.2  # noise in robot motion
        measurement_noise = 0.2  # noise in the measurements

        self.noise_threshold = 2.0  # measurement noise can be between -1.0 and 1.0

        # instantiate a robot, r
        self.r = robot(world_size, measurement_range, motion_noise, measurement_noise)

        # create landmarks
        num_landmarks = 5
        self.r.make_landmarks(num_landmarks)

    def test_sense_landmarks(self):
        measurements = self.r.sense()

        self.assertEqual(5, len(self.r.landmarks), "There should be 5 landmarks at random locations")
        self.assertEqual(5, len(measurements), "There should be 5 measurements; one for each landmark")


if __name__ == '__main__':
    unittest.main()
