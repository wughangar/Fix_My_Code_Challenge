#!/usr/bin/python3
"""
square
"""


class square():
    """
    initialize the class
    """
    def __init__(self, width=0, height=0, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """ permitter of my square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ str"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ main"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
