#!/usr/bin/python3


import pandas

def main():

    # create a dataframe from json
    pokemon = df = pandas.read_csv("pokedex.csv")

    # writeout dataframe to CSV
    df.to_csv("pokedex.csv")

if __name__ == "__main__":
    main()
