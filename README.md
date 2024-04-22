# laserscan
This project simulates A Geometric Transformation Tool for Laser Scanner Distance Sensors
It contains A laserscan module (as .py file) that reads and writes laser scan data in polar (distance measurements and measurement angles) or cartesian (x, y) coordinates. It uses the csv module to read and write CSV files. It also transforms the laser data from polar to cartesian coordinates and vice a versa. it also does filtering on laser scan by setting lower/upper limits on measurement angles.





filter_angles_bet_upper_lower.py reads the “laserscan.csv” file which contains a laser data in cartesian coordinates. It filters out the measurements in (-π/2, -π/4) and (π/4, π/2) In order to remove the unreliable laser data because of the long standoffs.
