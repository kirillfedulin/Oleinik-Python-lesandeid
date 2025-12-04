#5.1
#esimene ülesanne
from importlib.metadata import diagnose
import math



def float_kontroll(sisend:str)->float:
     while True:
        try:
            arv = float(sisend)
            return arv
        except ValueError:
            sisend=input("Plaun sisseta arv!")


def int_kontroll(sisend:str)->int:
     while True:
        try:
            arv = int(sisend)
            return arv
        except ValueError:
            sisend=input("Plaun sisseta arv!")



def arithmetic(a:float,b:float,tehe:str)->any:
    """Lihtne kalkulator:
    + - liitmine
    - - lahuramine
    * - korrutamine
    / - jagamine
    Muul juhul tagastab "Tundmatu tehe"
    :param float a: esimene arv
    :param float: b teine arv
    :param srt tehe: tehe, mis tuleb teha
    :return/rtype: tehte tulemus float või str
    """

    if tehe in ["+", "-", "*", "/"]:
        if tehe=="/" and b == 0:
            vastus = "Nulliga jagamine pole lubatud"
        else:
            vastus = eval(f"{a}{tehe}{b}")
    else:
        vastus="Tundmatu tehe"
    return vastus



def is_year_leap(year: int) -> bool:
   if (year % 4 == 0 and year % 100 != 0):
       return True
   else:
        return False


def square(külg: float) -> any:
    perimitor = 4 *külg
    pindala = külg * külg
    diagonal = külg * math.sqrt(2)
    return perimitor, pindala, diagonal 