# Drone Control System Simulator 

Simulating a drone in 2 dimensions to research implementing drone control systems.

## Overview

The simulation models a simple drone as a line with 2 rotors at either end.
The drone is controlled by adapting the thrust produced by each rotor with the aim of travelling from point A to point B.

## Method

The control system (in pid.py) uses a proportional and derivative control method for 3 different variables.
A Kp variable and Kd variable was made for each the horizontal error, vertical error, and rotational error. A desired rotation of the drone was calculated depending on the position error in x and the velocity error in x which is updated at every time step. The rotation is then achieved by applying a different thrust to each rotor depending on the rotational Kp and Kd. The base thrust applied to both rotors was calculated using vertical postion error and velocity error controlloing the height.

## Limitations
- No air resistance accounted for
- 2 dimensional model
- Kp and Kd values found from trial and error, some work better in certain situations than others

## Assumptions
- Mass: 1kg
- Moment of intertia: 0.01kg m^2
- Length of drone: 0.5m
- Max rotor thrust per rotor: 30N

## Results
Drone reaches most destinations succesfully. Drone doesn't take the fastest path and can sometimes take a long time to settle within the area of the mark. Sometimes has large overshoot. Demos can be seen in the visualisations folder.

## Next Steps
- 3 dimensions
- Introducing some noise variables, e.g. wind
- Come up with different model for control

## Usage
"python -m Visualisation.plot"