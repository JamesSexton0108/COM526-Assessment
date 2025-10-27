from agent import Agent
import utils

class ChargingStation(Agent):

    def __init__(self, position, facing):
        super().__init__(position, facing)

    def decide(self, environment):
        front_obj, front_loc = self.sense_front(environment)
        if utils.is_robot(front_obj):
            return "charge", front_obj, front_loc
        return "wait", None, None




    def act(self, environment):
        decision, item, cell = self.decide(environment)

        if decision == "charge":
            item.charge()
        else:
            pass

    def __str__(self):
        return self.facing
