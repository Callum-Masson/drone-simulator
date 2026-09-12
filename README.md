# Drone Control System Simulator 

Simulating a drone with 6-DOF to research implementing drone control systems.

## Overview

The simulation models a simple quadrotor as 2 crossed lines with rotors at each end in 3 dimensions.
The drone is controlled by adapting the thrust produced by each rotor with the aim of travelling from point A to point B.

## Method

The control system (in pid.py) uses a proportional and derivative control method for 5 different variables.
A Kp variable and Kd variable was made for each the horizontal errors, vertical error, and rotational errors. A desired rotation of the drone was calculated depending on the position error in x and y and the velocity error in x and y which is updated at every time step. The rotation is then achieved by applying a different thrust to each rotor depending on the rotational Kp and Kd. The base thrust applied to the rotors was calculated using vertical postion error and velocity error controlling the height.

## Limitations
- No air resistance accounted for
- No noise variables
- Kp and Kd values found from trial and error, some work better in certain situations than others

## Assumptions
- Mass: 1kg
- IYY and IXX: 0.01kg m^2
- IZZ: 0.02kg m^2
- Length of arms: 0.25m
- Max rotor thrust per rotor: 15N

## Results
Drone reaches most destinations succesfully. Drone sometimes doesn't take the fastest path and can sometimes take a long time to settle within the area of the mark. Sometimes has large overshoot. Demos can be seen in the visualisations folder.

## Next Steps
- Introducing some noise variables, e.g. wind
- Air resistance
- Create a better model for control

## Usage
"python -m Visualisation.plot"