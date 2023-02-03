#!/usr/bin/python3

import Fixme

import pytest

def test__evens_1():
    Fixme.evens(10) == [0, 2, 4, 6, 8, 10]


def test__evens_2():
     Fixme.evens(11) == [0, 2, 4, 6, 8, 10]


def test__evens_3():
     Fixme.evens(0) == [0]


def test__evens_4():
     Fixme.evens(1) == [0]


def test__evens_5():
    Fixme.evens(-1) == []
    
