"""
Copyright Ionut Soran 2021. ALL RIGHTS RESERVED.
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
Cell class for processing and manipulation of the coordinates of the points in 2D space.
"""
import logging

logger = logging.getLogger(__name__)

# TODO Create docstring for the CellPoint class for


class CellPoint:

    def __init__(self, points, n=0):
        if len(points) > 0:
            self.points = points
        else:
            self.points = [0] * n

    def set_mutliplier(self, one=None, values=None):
        self.func_caller(lambda x, y: x * y, one, values)
        return self

    def set_offset(self, one=None, values=None):
        self.func_caller(lambda x, y: x + y, one, values)

        return self

    def func_caller(self, func, one=None, values=None):
        if one:
            for idx, point in enumerate(self.points):
                self.points[idx] = func(point, one)
        else:
            self.points = [func(point, value) for point, value in zip(self.points, values)]

    def to_tuple(self):
        return tuple(self.points)
