import numpy as np
from sklearn.metrics import mean_squared_error
import sys
sys.path.append("..")
import grading


def submit_mse(compute_mse, email, token):
    ASSIGNMENT_KEY = "SBaWP48eEeeGSBKyliRlgg"
    PART_KEY = "u2t7D"

    # First, do rigorous local testing to help the learner
    for n in [1, 5, 10, 10**3]:
        elems = [np.arange(n), np.arange(n, 0, -1), np.zeros(n),
                 np.ones(n), np.random.random(n), np.random.randint(100, size=n)]
        for el in elems:
            for el_2 in elems:
                true_mse = np.array(mean_squared_error(el, el_2))
                my_mse = compute_mse(el, el_2)
                if not np.allclose(true_mse, my_mse):
                    print('mse(%s,%s)' % (el, el_2))
                    print("should be: %f, but your function returned %f" % (true_mse, my_mse))
                    raise ValueError('Wrong result')
    # Second, submit some reference values. There is nothing preventing the learner from
    # manually submitting numbers computed not via tensorflow, so there is little point
    # in comprehensive server-side testing
    test_pairs = (
        (np.array([
            0.85415937, 0.768366, 0.9763879, 0.11861405, 0.21219242]),
         np.array([0.27163543, 0.14893905, 0.84616464,
                   0.86294942, 0.65509213])),
        (np.array([1, 2, 3]), np.array([3, 2, 2])),
        (np.array([1]), np.array([1])))
    answers = []
    for pair in test_pairs:
        answers.append(compute_mse(pair[0], pair[1]))
    grader = grading.Grader(ASSIGNMENT_KEY)
    grader.set_answer(PART_KEY, answers)
    grader.submit(email, token)
