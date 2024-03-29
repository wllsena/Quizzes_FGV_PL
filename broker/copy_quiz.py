import pandas as pd
import os
import sys

file = sys.argv[1]

names = pd.read_csv("classroom.csv").Name

for name in names:
    os.system("git -C repositories/{} pull".format(name))
    os.system("cp ../quizzes/{}.py repositories/{}".format(file, name))
    os.system("git -C repositories/{} add {}.py".format(name, file))
    os.system('git -C repositories/{} commit {}.py -m "Quiz"'.format(name, file))
    os.system("git -C repositories/{} push".format(name))
