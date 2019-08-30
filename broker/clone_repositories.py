import os
import pandas as pd

cr = pd.read_csv("classroom.csv")

for i in cr.index:
    os.system("mkdir repositories/{} & git clone {} repositories/{}/".format(cr.Name[i], cr.URL[i], cr.Name[i]))
