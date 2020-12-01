import os, shutil, time
import models.utils as utils
import models.naive_bayes as gnb
import models.decision_tree as dt
import models.random_forest as rf
import models.support_vector_machine as svm
import models.neural_network as nn

if __name__ == "__main__":
    assert utils.assert_correct_directory(), f"Make sure you execute from the project root directory!"
    if os.path.isdir("results"):
        shutil.rmtree("results")
    os.makedirs("results")

    # Change argument to True to use oversampling
    start = time.time()
    gnb.naive_bayes()
    dt.decision_tree()
    rf.random_forest()
    svm.support_vector_machine()
    nn.neural_network()
    end = time.time()
    print(f'Done training the models in {round(end-start, 3)} seconds')