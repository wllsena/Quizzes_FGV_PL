import pandas as pd
import importlib
import os
import sys
sys.path.append('..')

num_quiz = max([int(file[5]) for file in os.listdir("../quizzes") if file[:4] == "quiz"])
file = "quiz_{}".format(num_quiz)
solved = importlib.import_module("solved." + file)

def tests(funcs_str, tests, grades, keys=False, notall=1/2):
    for name in pd.read_csv("../broker/classroom.csv").Name:
        final_report = open("../broker/reports/final_report_{}.txt".format(file), "w+")
        report_file  = open("../broker/repositories/{}/report_{}_{}.txt".format(name, file, name), "w+")

        try:
            attempt = importlib.import_module("broker.repositories.{}.{}".format(name, file))
            funcs        = [getattr(attempt, func) for func in funcs_str]
            funcs_solved = [getattr(solved, func)  for func in funcs_str]

            reports = ""
            question = 0
            amount = [0, 0]

            if not keys:
                keys = [lambda a, b: a == b for i in range(len(funcs))]

            for i in range(len(funcs)):
                question += 1
                report = ""
                sub_question = 0
                number = len(tests[i])
                hits = 0

                for t in tests[i]:
                    sub_question += 1
                    report += "      sub-questão {}: ".format(sub_question)
                    output = funcs_solved[i](t)
                    try:
                        given_output = funcs[i](t)
                        if keys[i](output, given_output):
                            report += "Correto! :) - {}({}) == {}\n".format(funcs_str[i], t, output)
                            hits += 1
                        else:
                            report += "Errado   :( - {}({}) == {} não {}\n".format(funcs_str[i], t, output, given_output)
                    except:
                        report += "Errado.. :( - {}({}) deu erro\n".format(funcs_str[i], t)

                if hits == number:
                    value = grades[i]
                else:
                    value = grades[i]*notall*hits/number
                amount[0] += value
                amount[1] += grades[i]

                reports += "   Questão {} - {:0.1f}/{} pontos\n".format(
                    question, value, grades[i]) + report + "\n\n"

            reports = "Relatório - {}: Nota: {:0.4f}/{}:\n\n".format(name, amount[0], amount[1]) + reports
            report_file.write(reports)
            final_report.write(reports)
            report_file.close()
            
            os.system("git -C ../broker/repositories/{} add report_{}_{}.txt".format(name, file, name))
            os.system('git -C ../broker/repositories/{} commit report_{}_{}.txt -m "Relatório quiz"'.format(name, file, name))
            os.system("git -C ../broker/repositories/{} push".format(name))
        except:
            print("Erro {}".format(name))

        final_report.close()

