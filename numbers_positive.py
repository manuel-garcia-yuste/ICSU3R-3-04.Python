#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program say if the number is positive or negative


def main():
    # this function runs the program

    # input
    integer = int(input("Enter an integer="))

    # process
    if (integer == 0):
        print("0")
    elif (integer < 0):
        print("negative")
    else:
        print("positive")


if __name__ == "__main__":
    main()
