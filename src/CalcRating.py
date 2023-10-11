# -*- coding: utf-8 -*-
from src.Types import DataType

RatingType = dict[str, float]


class CalcRating:
    def __init__(self, data: DataType) -> None:

        self.data: DataType = data

        self.rating: RatingType = {}

    def calc(self) -> RatingType:

        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += float(subject[1])
            self.rating[key] /= len(self.data[key])
        return self.rating
    def YAMLcalc(self):
        for name in self.data.keys():
            self.rating[name] = 0.0
            for subjects in self.data[name].values():
                self.rating[name] += float(subjects)

            self.rating[name] /= len(self.data[name])

        return self.rating