from charging_station import ChargingStation
from robot import Robot
from dirt import Dirt


def is_robot(object):
    if isinstance(object, Robot):
        return True
    return False


def is_charging_station(object):
    if isinstance(object, ChargingStation):
        return True
    return False


def is_dirt(object):
    if isinstance(object, Dirt):
        return True
    return False