import unittest
from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
       raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class Test_fit_transform(unittest.TestCase):
    def test_encode_equals(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_encode_not_equals(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 0, 1]),
            ('New York', [0, 0, 1, 0]),
            ('Moscow', [0, 0, 0, 1]),
            ('London', [0, 1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertNotEqual(transformed_cities, exp_transformed_cities)

    def test_encode_list(self):
        cities = ['Moscow']
        exp_transformed_cities = [('Moscow', [1])]
        transformed_cities = fit_transform(cities)
        self.assertListEqual(transformed_cities, exp_transformed_cities)

    def test_in_structure(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_structure_cities = ('Moscow', [0, 0, 1])
        transformed_cities = fit_transform(cities)
        self.assertIn(exp_structure_cities, transformed_cities)

    def test_empty(self):
        cities = []
        actual = fit_transform(cities)
        expected = []
        self.assertEqual(actual, expected)

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
