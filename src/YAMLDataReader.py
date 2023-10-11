# -*- coding: utf-8 -*-
from src.Types import DataType
from src.DataReader import DataReader
import yaml


class YAMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""

        self.students: DataType = {}

    def read(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            prime_service = yaml.safe_load(file)
            # for line in file:
            #   if not line.startswith(" "):
            #      self.key = line.strip()
            #     self.students[self.key] = []
            # else:
            #     subj, score = line.split(":", maxsplit=1)
            #     self.students[self.key].append(
            #         (subj.strip(), int(score.strip())))
        # return self.students
        return (prime_service)
