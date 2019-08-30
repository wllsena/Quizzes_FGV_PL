import os
import pandas as pd

cr = pd.read_csv("classroom.csv")

for i in cr.index:
    os.system("git -C repositories/{} pull".format(cr.Name[i]))
