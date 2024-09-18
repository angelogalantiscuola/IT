# argparse
import argparse


def square(x):
    return x**2


def cube(x):
    return x**3


def main():
    parser = argparse.ArgumentParser(description="Square or cube a number")
    parser.add_argument("number", type=int, help="The number to be squared or cubed")
    parser.add_argument("--square", action="store_true", help="Square the number")
    parser.add_argument("--cube", action="store_true", help="Cube the number")
    args = parser.parse_args()
    number = args.number
    if args.cube:
        print(f"The cube of {number} is {cube(number)}")
    if args.square:
        print(f"The square of {number} is {square(number)}")
    else:
        print(f"No action specified for {number}")


if __name__ == "__main__":
    main()
