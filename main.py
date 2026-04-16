# StopLightSim.py
# Name: Jack Schulz
# Date: 4-16-26
# Assignment: Lab 11

import simpy

# Global variable to track light state
greenLight = True


def stopLight(env):
    """Simulates a traffic light that cycles between green, yellow, and red."""
    global greenLight

    while True:
        print("Green")
        greenLight = True
        yield env.timeout(30)

        print("Yellow")
        yield env.timeout(2)

        print("Red")
        greenLight = False
        yield env.timeout(20)


def car(env, car_id):
    """Simulates a car arriving and waiting for the light."""

    print("Car", car_id, "arrived at", env.now)

    while greenLight == False:
        print("Car", car_id, "waiting")
        yield env.timeout(1)

    yield env.timeout(1)
    print("Car", car_id, "departed at", env.now)


def carArrival(env):
    """Creates cars at regular intervals."""

    car_id = 0

    while True:
        yield env.timeout(5)
        car_id += 1
        env.process(car(env, car_id))


def main():
    env = simpy.Environment()

    # Start processes
    env.process(stopLight(env))
    env.process(carArrival(env))

    # Run simulation
    env.run(until=100)

    print("Simulation complete")


if __name__ == "__main__":
    main()