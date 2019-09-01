import os
import pandas as pd

cr = pd.read_csv("classroom.csv")

for i in cr.index:
    os.system("git -C repositories/{} add -A".format(cr.Name[i]))
    os.system('git -C repositories/{} commit -a -m "Organizando repositorio"'.format(cr.Name[i]))
    os.system("git -C repositories/{} push".format(cr.Name[i]))
