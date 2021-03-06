'''
Kodutoo 7
03.10.2014
Andres Liiver
'''

import simulator
from robot import *
import random

def main():
    random.seed()
    world_width = 10
    world_height = 10
    #obstacles = [(4, 4), (4,5), (4,6), (5,6), (6,6), (6,5), (6,4)]
    #world = simulator.World(world_width, world_height, sleep_time = 1, obstacles=obstacles, treasure=(5, 5))
    world = simulator.World(world_width, world_height, sleep_time = 1)
    robots = []
    i = 0

    #robots.append(Robot(world, random.randint(0, world_width-1), random.randint(0, world_height-1), random.randint(0, 7)))
    #robots.append(Robot(world, 1, 8, 5))

    while i < (world_width // 3):
        try:
            robots.append(Robot(world, random.randint(0, world_width-1), random.randint(0, world_height-1), random.randint(0, 7)))
            i += 1
        except simulator.RegistrationException:
            pass

    while True:
        try:
            world.print_state()
            for robot in robots:
                robot.reason(world)

            world.tick()
        except simulator.RobotWallCrashException:
            print("A robot crashed into a wall! Simulation over!")
            return
        except simulator.RobotCollisionException:
            print("A robot crashed into another robot! Simulation over!")
            return
        except simulator.RobotObjectCrashException:
            print("A robot crashed into an object!")
            return
        except simulator.RobotFoundTreasureException:
            print("A robot found the treasure! You win!")
            return
    
if __name__ == "__main__":
    main()