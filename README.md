# Landmark Detection and Robot Tracking using SLAM

I completed this project as part of Udacity's [Computer Vision Nanodegree](https://www.udacity.com/course/computer-vision-nanodegree--nd891) program.

The goal of this project is to implement SLAM (Simultaneous Localization and Mapping) for a 2 dimensional world.

We combine knowledge of robot sensor measurements and movement to create a map of an environment from only sensor and motion data gathered by a robot, over time. SLAM provides a way to track the location of a robot in the world in real-time and identify the locations of landmarks such as buildings, trees, rocks, and other world features.

Below is an example of a 2D robot world with landmarks (purple x's) and the robot (a red 'o') located and found using *only* sensor and motion data collected by that robot. 

![](images/robot_world.png)

# Project Files
The project consists of three Python notebooks and one python file.

* **Notebook 1**: [Robot Moving and Sensing](1.%20Robot%20Moving%20and%20Sensing.ipynb)
* **Notebook 2**: [Omega and Xi, Constraints](2.%20Omega%20and%20Xi,%20Constraints.ipynb)
* **Notebook 3**: [Landmark Detection and Tracking](3.%20Landmark%20Detection%20and%20Tracking.ipynb)
* **Python file**: [robot_class.py](robot_class.py)

The first two notebooks are for exploration of the code, and include a review of SLAM architectures.
Notebook 3 and the `robot_class.py` file contain the project code that implements landmark detection and tracking using SLAM.

