# Using DJI tello's in swarm configuration
# You can only do this with DJI Tello EDU versions and you need to connect all drones to your local WIFI AP
# # based on SDK  https://djitellopy.readthedocs.io/en/latest/swarm/

# author Maarten Dequanter
# date 21/09/2022

from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.0.86",
    "192.168.0.85"
])

swarm.connect()
swarm.takeoff()

# run in parallel on all tellos
swarm.move_up(30)

# run by one tello after the other
swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))

# making each tello do something unique in parallel
swarm.parallel(lambda i, tello: tello.move_left(i * 20 + 20))
swarm.parallel(lambda i, tello: tello.move_right(i * 20 + 20))

swarm.land()
swarm.end()