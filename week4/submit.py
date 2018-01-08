import sys
sys.path.append("..")
import grading


# code_size = 71
# img_shape = (38, 38, 3) or (32, 32, 3)
def submit_autoencoder(submission, score, email, token):
    grader = grading.Grader("9TShnp1JEeeGGAoCUnhvuA")
    encoder, decoder = submission
    grader.set_answer("FtBSK", encoder.output_shape[1])
    grader.set_answer("83Glu", decoder.output_shape[1:])
    grader.set_answer("fnM1K", score)
    grader.submit(email, token)
