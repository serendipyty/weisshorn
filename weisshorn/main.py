from driver.time import TimeStepping
from parameter.parameter import Parameters

DTYPE = 'float8'

if __name__ == "__main__":
    # test_sum()
    print("Everything passed")

    parameters = Parameters()

    # Initialize driver
    driver = TimeStepping(parameters)

    # GO!
    driver.go()