# -*- coding: utf-8 -*-
import argparse
import sys
from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader
from src.YAMLDataReader import YAMLDataReader
from src.HighScore import HighScore


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = 'data/data.txt'
    reader = TextDataReader()
    students = reader.read(path)
    # print("Students: ", students)
    rating = CalcRating(students).calc()
    # print("Rating: ", rating)
    YAML()


def YAML():
    path = 'data/data.yml'
    reader = YAMLDataReader()
    students = reader.read(path)
    print("Students: ", students)
    rating = CalcRating(students).YAMLcalc()
    print("Rating: ", rating)
    highScore = HighScore(rating).calc()
    print("Количество отличников: " + str(highScore))


if __name__ == "__main__":
    main()
