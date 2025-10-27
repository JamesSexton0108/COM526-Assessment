from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, position: tuple[int, int], facing:str):
        self.position = position
        self.facing = facing
        self.direction_offsets = {
            "u": (0, -1), "^": (0, -1),
            "r": (1, 0),  ">": (1, 0),
            "d": (0, 1),  "v": (0, 1),
            "l": (-1, 0), "<": (-1, 0)
        }

    def sense_around(self, environment):
        neighbours = []
        for direction in ["u", "^", "r", ">", "d", "v", "l", "<"]:
            row_offset, col_offset = self.direction_offsets[direction]
            neighbours.append((self.position[0] + row_offset, self.position[1] + col_offset))

        return environment.get_cells(neighbours)

    def sense_front(self, environment):

        dx, dy = self.direction_offsets[self.facing]
        fx = self.position[0] + dx
        fy = self.position[1] + dy
        return environment.world[fy][fx],(fx,fy)

    @abstractmethod
    def decide(self, percept: dict[tuple[int,int],...]):
        pass

    @abstractmethod
    def act(self, environment):
        pass
