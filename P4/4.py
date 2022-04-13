# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:52:46 2022

@author: Carlos
"""

from kanren import run, var, Relation, facts
a = var()
b = var()

padre = Relation()
facts(padre, ("David", "Carlos"),
              ("David", "Luz"),
              ("Omar", "Christian"),
              ("Omar", "Fabiana"),
              ("Gonzalo",  "Noemi"),
              ("Miki",  "Gabriela"),
              ("Fidel",  "Nilton"),
              ("Miguel","Gonzalo"),
              ("Miguel","Miki"),
              ("Pascual","David"),
              ("Pascual","Fidel"),
              )

madre = Relation()
facts(madre, ("Susana", "Carlos"),
              ("Susana", "Luz"),
              ("Gretel", "Christian"),
              ("Gretel", "Fabiana"),
              ("Herminia",  "Noemi"),
              ("Sandra",  "Gabriela"),
              ("Vicky",  "Nilton"),
              ("Magdalena","Gonzalo"),
              ("Magdalena","Miki"),
              ("Aurora","David"),
              ("Aurora","Fidel"),
              )

hermano = Relation()
facts(hermano,("Carlos",  "Luz"),
              ("Fabiana",  "Christian"),
              ("David",  "Fidel"),
              ("Susana",  "Miki"),
              ("Susana",  "Gretel"),
              ("Susana",  "Gonzalo"),
              ("Edmundo",  "Pancho"),
              )

abuelo = Relation()
facts(abuelo, ("Pascual", "Carlos"),
              ("Pascual", "Luz"),
              ("Miguel", "Carlos"),
              ("Miguel", "Luz"),
              ("Miguel", "Christian"),
              ("Miguel", "Fabiana"),
              ("Miguel",  "Noemi"),
              ("Miguel",  "Gabriela"),
              ("Pascual",  "Nilton"),
              )

tio= Relation()
facts(tio,    ("Susana", "Christian"),
              ("Susana", "Fabiana"),
              ("Susana", "Nilton"),
              ("Susana", "Noemi"),
              ("Susana", "Gabriela"),
              ("David", "Christian"),
              ("David", "Fabiana"),
              ("David", "Nilton"),
              ("David", "Noemi"),
              ("David", "Gabriela"),
              ("Gretel", "Carlos"),
              ("Gretel", "Luz"),
              ("Herminia",  "Luz"),
              ("Herminia",  "Carlos"),
              ("Sandra",  "Carlos"),
              ("Sandra",  "Luz"),
              ("Vicky",  "Carlos"),
              ("Vicky",  "Luz"),
              )
primo = Relation()
facts(primo,  ("Carlos", "Christian"),
              ("Carlos", "Fabiana"),
              ("Carlos", "Nilton"),
              ("Carlos", "Noemi"),
              ("Carlos", "Gabriela"),
              ("Luz", "Christian"),
              ("Luz", "Fabiana"),
              ("Luz", "Nilton"),
              ("Luz", "Noemi"),
              ("Luz", "Gabriela"),
              ("Christian", "Gabriela"),
              ("Fabiana", "Gabriela"),
              )



print(run(3, a, primo(a, "Noemi")))
print(run(4, b, primo("Carlos", b)))
print(run(1, a, padre(a,"Carlos")))
print(run(1, a, padre(a,"Christian")))
print(run(2, a, madre("Susana",a)))
print(run(1, a, madre(a,"Christian")))
print(run(4, a, abuelo("Miguel",a)))
print(run(1, a, abuelo(a,"Nilton")))
print(run(5, a, tio("David",a)))
print(run(3, a, tio(a,"Luz")))



