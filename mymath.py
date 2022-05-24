import random
import string
import math
import cmath

def Plus(x, y):
    return x + y


def Minus(x, y):
    return x - y


def Div(x, y):
    return x / y


def Mul(x, y):
    return x * y


def OOD(x, y):
    return x % y


def STEP(x, y):
    return x ** y


def WMN(x):
    return len(x)


def SUMN(x):
    y = x
    cnt = 0
    while y != 0:
        cnt += y % 10
        y /= 10
        y = int(y)
    return cnt

def LOG(x):
    return math.log(x)

def KOR(x):
    return math.sqrt(x)

def RAND(x, y):
    return random.randint(x, y)

def FNP(x, y):
    return y * (x/100)

def FPN(x, y):
    return x / (y/100)