from agent import Agent
import random


class Robot(Agent):

    def __init__(self, position: tuple[int, int], facing):
        super().__init__(position, facing)
        self.battery = 100
        self.just_Turned = False


    def decide(self, percept: dict[tuple[int, int], ...]):
        free_spaces = []
        for k, v in percept.items():
            if v == " ":
                free_spaces.append(k)

        if free_spaces:
            return "move", free_spaces

    def act(self, environment):
        cell = self.sense_around(environment)

        decision, target = self.decide(cell)
        if decision == "move":
            self.move(environment, target)
        pass


    def move(self, environment, to):
        self.battery -= 1
        if self.just_Turned:
            front_obj, front_loc = self.sense_front(environment)
            if front_obj == " ":
                environment.move_to(self.position, front_loc)
                self.position = front_loc
                self.just_Turned = False
        else:
            new_direction = random.choice(to)
            cx, cy = self.position
            tx, ty = new_direction

            if tx == cx and ty == cy - 1:
                new_facing = '^'
            elif tx == cx and ty == cy + 1:
                new_facing = 'v'
            elif tx == cx - 1 and ty == cy:
                new_facing = '<'
            elif tx == cx + 1 and ty == cy:
                new_facing = '>'
            else:
                return

            if self.facing != new_facing:
                self.facing = new_facing
            self.just_Turned = True

    def charge(self):
        if self.battery + 5 <= 100:
            self.battery += 5
        else:
            self.battery = 100

    def __str__(self):
        return self.facing

