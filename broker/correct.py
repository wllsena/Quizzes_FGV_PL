import pandas as pd
from importlib import import_module as im
import signal
import copy
import os
import sys
sys.path.append('..')

num_quiz = max([int(file[5]) for file in os.listdir("../quizzes") if file[:4] == "quiz"])
file     = "quiz_{}".format(num_quiz)
names    = pd.read_csv("../broker/classroom.csv").Name
length   = len(names)

class test_timeout:
    def __init__(self, seconds, error_message=None):
        if error_message is None:
              error_message = 'test timed out after {}s.'.format(seconds)
        self.seconds       = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TestTimeout(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)

class Test:
    mutable = True

    def __init__(self, func_name, value, tests, key = lambda a, b: a == b, notall = 1/2, time = 10):
        self.func    = func_name
        self.value   = value
        self.tests   = tests
        self.key     = key
        self.notall  = notall
        self.time    = time
        self.amount  = len(tests)
        self.solved  = self.run(im("solved.{}".format(file)))
        self.mutable = False

    def __setattr__(self, name, value):
        if self.mutable:
            object.__setattr__(self, name, value)

    def run(self, module):
        tests   = copy.deepcopy(self.tests)
        outputs = [None]*self.amount

        for i in range(self.amount):
            t = tests[i]
            try:
                with test_timeout(self.time):
                    output = getattr(module, self.func)(t)
            except:
                output = "ERRO"
            outputs[i] = output

        if not self.mutable:
            hits  = sum([self.key(self.solved[i], outputs[i]) for i in range(self.amount)])
            grade = self.value if hits == self.amount else self.value*self.notall*hits/self.amount
            return grade, outputs
        return outputs

class report:
    answers = [None]*length
    grades  = [None]*length
    reports = [None]*length

    def __init__(self, tests):
        self.tests = tests

    def get_grade(self):
        tests = copy.deepcopy(self.tests)

        for i in range(length):
            name = names[i]
            try:
                module = im("broker.repositories.{}.{}".format(name, file))
                answer = []
                grade  = []
                for test in self.tests:
                    output = test.run(module)
                    answer.append(output[1])
                    grade.append(output[0])
            except:
                answer = [["unable to import" for i in t.tests] for t in self.tests]
                grade  = [0]*len(tests)

            self.answers[i] = answer
            self.grades[i]  = grade

    def get_report(self):
        for i in range(length):
            grade       = self.grades[i]
            answer      = self.answers[i]
            final_grade = [0, 0]
            report      = ""
            for k in range(len(self.tests)):
                test     = self.tests[k]
                output   = answer[k]
                expected = test.solved
                final_grade[0] += grade[k]
                final_grade[1] += test.value
                report += "   Questao: {}, Nota: {}/{}\n".format(k+1, grade[k], test.value)
                for j in range(test.amount):
                    report += "      {}({}) = {}\n".format(test.func, test.tests[j], expected[j])
                    report += "         valor dado: {}\n\n".format(output[j])

            self.reports[i] = "Quiz: {}, Aluno: {}, Notal final: {}/{}\n".format(
                num_quiz, names[i], final_grade[0], final_grade[1]) + report

    def write_reports(self):
        total_report = open("../broker/reports/total_report_{}.txt".format(file), "w+")
        minimum_report = open("../broker/reports/minimum_report_{}.txt".format(file), "w+")
        for i in range(length):
            report = open("../broker/repositories/{}/report_{}.txt".format(names[i], file), "w+")
            report.write(self.reports[i])
            total_report.write(self.reports[i])
            minimum_report.write(self.reports[i].partition("\n")[0] + "\n")
            report.close()
        total_report.close()
        minimum_report.close()

    def push_reports(self):
        for name in names:
            os.system("git -C ../broker/repositories/{} add report_{}.txt".format(name, file))
            os.system('git -C ../broker/repositories/{} commit report_{}.txt -m "Relatório quiz"'.format(name, file))
            os.system("git -C ../broker/repositories/{} push".format(name))
