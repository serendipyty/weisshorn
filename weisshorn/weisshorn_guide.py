from weisshorn.driver.time import TimeStepping
from weisshorn.parameters.parameter import Parameter

DTYPE = 'float8'

print(f"The package name is {__package__}")
print(f"The module name is {__name__}")

def run():
    # test_sum()
    print("Everything passed")

    # Read and validate input file
    parameters = Parameter('input_v1.toml')

    # Initialize driver
    driver = TimeStepping(parameters)

    # GO!
    driver.go()