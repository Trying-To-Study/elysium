# Code created by TryingToStudy
import random as r

# personal project, app for champ, lane, and build (general) select


def rand(x):
    """To get a random champ of the list"""
    r.shuffle(x)
    champ = r.choice(x)
    return champ


def position():
    """To get a random position to play the champ at"""
    positions = ["Baron Lane", "ADC", "Support", "Jungle", "Mid-lane"]
    r.shuffle(positions)
    pos = r.choice(positions)
    return pos


def build():
    """To get the type of build for this match"""
    types = ["AD", "AP", "Tank"]
    r.shuffle(types)
    t = r.choice(types)
    return t


def result():
    """prints out the champ and details"""
    f = open("Champions.csv", "r")

    data = f.read().split('\n')
    data = data[1:-1]
    f.close()
    output = [rand(data), position(), build()]

    return output


def write():
    """Writes into a file to display in OBS"""
    f = open("Champs.txt", "w")
    variable = result()
    x = f'Currently: {variable[0]} at {variable[1]} building {variable[2]} '
    f.write(x)
    f.close()


# hehe code go brrrr

write()





