# -*- coding: utf-8 -*-
from src.Types import DataType
from abc import ABC, abstractmethod


class DataReader(ABC):
    @abstractmethod
    def read(self, path: str) -> DataType:
        pass
