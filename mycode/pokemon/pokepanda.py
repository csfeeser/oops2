#!/usr/bin/python3


import pandas

def main():

    # create a dataframe from json
    df = pandas.read_csv("pokedex.txt")

    # writeout dataframe to CSV
    df.to_csv("pokedex.csv")

if __name__ == "__main__":
    main()
