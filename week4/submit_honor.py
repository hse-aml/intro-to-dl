import sys
sys.path.append("..")
import grading


def submit_honor(submission, email, token):
    grader = grading.Grader("FCl7G51lEeeeZQ4xJ2nzLA")
    G, D = submission
    grader.set_answer("ryO01", D.output_shape[1])
    grader.set_answer("PmSxZ", G.output_shape[1:])
    grader.submit(email, token)
