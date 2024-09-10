"""
------------------------------------------------------------------------
Lab 4, Functions Library
------------------------------------------------------------------------
Author: Ahmed Nafees
ID:     169053598
Email:  nafe3598@mylaurier.ca
__updated__ = "2023-10-02"
------------------------------------------------------------------------
"""
import math


def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """
    diam = radius*2
    return diam


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, area, vol = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        area - area of the square pyramid (float)
        vol - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    sb = base/2
    ph = height
    sh = math.sqrt(sb**2 + ph**2)
    area = base**2 + 4*(sb*sh)
    vol = (base**2)*(ph/3)
    return sh, area, vol


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.10
    QUARTERS_VALUE = 0.25
    LOONIES_VALUE = 1.00
    TOONIES_VALUE = 2.00

    nickel_change = nickels*NICKEL_VALUE
    dime_change = dimes*DIME_VALUE
    quarters_change = quarters*QUARTERS_VALUE
    loonies_change = loonies*LOONIES_VALUE
    toonies_change = toonies*TOONIES_VALUE
    total = nickel_change + dime_change + \
        quarters_change + loonies_change + toonies_change
    return total


def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """
    SECONDS_PER_YEAR = 31536000

    new_births = (SECONDS_PER_YEAR/births)*years
    new_deaths = (SECONDS_PER_YEAR/deaths)*years
    new_immigrants = (SECONDS_PER_YEAR/immigrants)*years
    new_size = size + new_births + new_immigrants - new_deaths
    return int(new_size)


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    SECONDS_IN_DAY = 86400
    SECONDS_IN_HOURS = 3600
    SECONDS_IN_MINUTES = 60

    days = seconds//SECONDS_IN_DAY
    hours = seconds//SECONDS_IN_HOURS
    minutes = seconds//SECONDS_IN_MINUTES
    return days, hours, minutes
