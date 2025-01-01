import unittest


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_reading_time(self):
        return f"{self.pages * 1.5} minutes"

    def apply_discount(self, discount):
        if not isinstance(discount, float):
            raise ValueError('Discount must be float number')
        if 0 <= discount <= 1:
            discounted_price = self.price - (discount * self.price)
            return f"${discounted_price}"
        raise ValueError('Discount must be float number between 0 and 1')


class TestBookClass(unittest.TestCase):
    def test_init_method(self):
        with self.assertRaises(TypeError):
            Book()

    def test__str__method(self):
        r = Book(1, 2, 3, 4)


        self.assertEqual(print(r), "1 by 2")


    # def test_get_reading_time(self):
    #     pass
    #
    # def test_apply_discount_not_float(self):
    #     pass
    #
    # def test_apply_discount_more_than_1(self):
    #     pass
    #
    # def test_apply_discount_less_than_0(self):
    #     pass
    #
    # def test_apply_discount_good_case(self):
    #     pass