from environment import Environment
from robot import Robot
from charging_station import ChargingStation

if __name__ == "__main__":
    e = Environment("floorplan.txt")
    robot1 = e.world[10][3]
    charging_station1 = e.world[11][3]


    while robot1.battery > 0:
        print(e)
        charging_station1.act(e)
        robot1.act(e)
        print(robot1.position)
        print(robot1.battery)

