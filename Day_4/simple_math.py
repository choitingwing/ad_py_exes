"""
A collection of simple math operations
This is a dostring
"""

def simple_add(a,b):
    """ The sum of two numbers / arrays

    Parameters
    ----------
    a: real number
    b: real number
        a and b need the same dimension.
        They can be numpy array

    Returns
    -------
    real number
        result of the sum of a and b

    Examples
    --------
    >>> simple_add(3,2)
    5
    >>> simple_add(2,2)
    4

    """
    return a+b

def simple_sub(a,b):
    """ The different of two numbers

    Parameters
    ----------
    a: a real number
    b: a real number

    Returns
    -------
    a real number
        result of the different of a and b

    """
    return a-b

def simple_mult(a,b):
    """ The product of two numbers

    Parameters
    ----------
    a: a real number
    b: a real number

    Returns
    -------
    a real number
        result of the product of a and b
    """
    return a*b

def simple_div(a,b):
    """ Division of two numbers

    Parameters
    ----------
    a: real number
    b: real number

    Returns
    -------
    a real number
        result of the Division of a and b

    """
    return a/b

def poly_first(x, a0, a1):
    """ The 1st order polynormial

    Parameters
    ----------
    x:  a real number
        The variable in the polynomial.
    a0: a real number
        The first constant.
    a1: a real number
        The 2nd constant.

    Returns
    -------
    a real number
        result of the 1st order polynormial

    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """ The 2nd order polynormial

    Parameters
    ----------
    x:  a real number
        The variable in the polynomial.
    a0: a real number
        The first constant.
    a1: a real number
        The 2nd constant.
    a2: a real number
        The 3rd constant.

    Returns
    -------
    a real number
        result of the 2nd order polynormial

    """
    return poly_first(x, a0, a1) + a2*(x**2)


# Feel free to expand this list with more interesting mathematical operations...
# .....
