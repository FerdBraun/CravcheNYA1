# -*- coding: utf-8 -*-
from src.Types import DataType

RatingType = dict[str, float]


class HighScore:
    def __init__(self, data) -> None:

        self.data = data
        self.count = 0

    def calc(self):
        for score in self.data.values():
            if score >= 90:
                self.count += 1
        return self.count
