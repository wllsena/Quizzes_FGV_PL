import pandas as pd
import os
import sys


num_quiz = max([int(file[5]) for file in os.listdir("../quizzes") if file[:4] == "quiz"])
file = "quiz_{}".format(num_quiz)

names = pd.read_csv("classroom.csv").Name

for name in names:
    os.system("git -C repositories/{} pull".format(name))
    os.system("cp ../quizzes/{}.py repositories/{}".format(file, name))
    os.system("git -C repositories/{} add {}.py".format(name, file))
    os.system('git -C repositories/{} commit {}.py -m "Quiz"'.format(name, file))
    os.system("git -C repositories/{} push".format(name))
