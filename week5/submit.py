import sys
import numpy as np
sys.path.append("..")
import grading


# code_size = 71
# img_shape = (38, 38, 3)
def submit_char_rnn(submission, email, token):
    grader = grading.Grader("cULEpp2NEeemQBKZKgu93A")
    history, samples = submission
    assert len(samples) == 25
    grader.set_answer("pttMO", int(np.mean(history[:10]) > np.mean(history[-10:])))
    grader.set_answer("uly0D", len(set(samples)))
    grader.submit(email, token)
