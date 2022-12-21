import math, random
from Body import Body
from Antigen import Antigen
from Detector import Detector
from ImmuneSystem import ImmuneSystem

def iterate(t, maxT, numAntigens, numPopulation, Pd, population):
    while (t < maxT):
        deltaT = ( (-1/numAntigens) * math.log(random.random()) )
        t += deltaT

        for body in population:
            damage = Pd * len(body.antigens)
            body.takeDamage(damage)
            # print(f"{body.label}: {body.health}")
            if (body.checkDeath()):
                print(f"{body.label} died at T: {t}")
                population.remove(body)

    for body in population:
        print(f"{body.label} survived!")

def init():
    health = 100        # create a body with 100 health
    t = 0
    maxT = 10
    numAntigens = 100
    numPopulation = 10
    Pd = 0.001          # probability that an antigen does damage

    population = []

    print(f"Number in population: {numPopulation}, Health: {health}, Number Antigens: {numAntigens}")

    for i in range(numPopulation):
        b = Body(f"body {i}", health)
        population.append(b)
        for i in range(numAntigens):
            a = Antigen(f"antigen {i}")
            a.infect(b)

    iterate(t, maxT, numAntigens, numPopulation, Pd, population)

init()
