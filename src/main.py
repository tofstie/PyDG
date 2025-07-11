import sys
import os
# Sets path of file to ./PyDG
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parameters.parameters import Parameters

# Main Function
def main(parameter_path: str):
    test = Parameters()
    test.read_parameters(parameter_path)

# Check arguments and run main function
if __name__ == "__main__":
    if len(sys.argv) > 2:
        raise ValueError("Too many arguments, the program only accepts one parameter file")
    if len(sys.argv) == 1:
        raise ValueError("A location to find parameter files is required, please input an argument")
    main(sys.argv[1])