import pandas as pd

'''
O arquivo "names2012.txt" no formato csv possui os seguintes dados:

As colunas estao no formato : name,sex,births

Sophia,F,22158
Emma,F,20791
Isabella,F,18931
Olivia,F,17147
...



Na funcao near, dado o parametro inteiro num:

-- Crie um DataFrame a partir desse arquivo
Ex

name     sex  births 
Sophia    F   22158  
Emma      F   20791  
Isabella  F   18931  

-- Crie a coluna 'mean by sex' com os valoes da média relativos à aquele 'sex'
Ex:

name     sex  births mean by sex
Sophia    F   22158  89.970382
Emma      F   20791  89.970382
Isabella  F   18931  89.970382

-- Crie a coluna 'mean distance' com os valores da distancia entre o número de 'births' e o numero mean by 'sex'
Ex:

name     sex  births mean by   sex mean distance
Sophia    F   22158  89.970382 22068.029618 
Emma      F   20791  89.970382 20701.029618
Isabella  F   18931  89.970382 18841.029618

-- Crie a coluna 'n distance' com os valores da distancia entre 'sex mean distance' e o parametro 'num'
Ex: (para num = 10360)

name     sex  births mean by   sex mean distance n distance
Sophia    F   22158  89.970382 22068.029618      11708.029618
Emma      F   20791  89.970382 20701.029618      10341.029618
Isabella  F   18931  89.970382 18841.029618      8481.029618

--
Retorne a tupla (min_male, min_female), onde 'min_male' é a pessoa de sex 'M' de menor 'n distance', 
o mesmo para min_famele com o 'F'

Ex:
near(10360) = ('John', 'Elizabeth')

'''

def near(num):
    return ('', '')