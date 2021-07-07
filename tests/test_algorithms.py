import math
from unittest import TestCase

import algorithms.algorithms as alg


class Test(TestCase):
    @staticmethod
    def asert_number_of_permutation(n_elements):
        counter = 0
        for _ in alg.permute(n_elements):
            counter += 1
        return counter == math.factorial(n_elements)

    def test_permute(self):
        self.assertTrue(all(self.asert_number_of_permutation(n)
                            for n in range(1, 8)))

    @staticmethod
    def asert_number_of_subset(n_elements):
        counter = 0
        for _ in alg.all_subsets(n_elements):
            counter += 1
        return counter == 2 ** n_elements

    def test_all_subsets(self):
        self.assertTrue(self.asert_number_of_subset(n) for n in range(1, 10))

    @staticmethod
    def assert_number_for_mesh_creator(number, *arrays):
        counter = 0
        for _ in alg.mesh_creator(*arrays):
            counter += 1
        return number == counter

    def test_mesh_creator(self):
        self.assertTrue(all((
            self.assert_number_for_mesh_creator(6, [1, 2], [3, 5, 6]),
            self.assert_number_for_mesh_creator(12, [1, 2], [3, 5, 6], [8, 9]),
            self.assert_number_for_mesh_creator(2, [1], [3], [3], [4, 6]))))
