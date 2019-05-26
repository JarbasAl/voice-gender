import pickle
import warnings
import numpy as np
from voice_gender.features import extract_features
from os.path import join, dirname

warnings.filterwarnings("ignore")


class GenderIdentifier:
    females_model_path = join(dirname(__file__), "models", "females.gmm")
    males_model_path = join(dirname(__file__), "models", "males.gmm")
    # load models
    females_gmm = pickle.load(open(females_model_path, 'rb'))
    males_gmm = pickle.load(open(males_model_path, 'rb'))

    @staticmethod
    def predict(audio):
        if isinstance(audio, str):  # file path
            audio = extract_features(audio)
        # female hypothesis scoring
        is_female_scores = np.array(GenderIdentifier.females_gmm.score(audio))
        is_female_log_likelihood = is_female_scores.sum()
        # male hypothesis scoring
        is_male_scores = np.array(GenderIdentifier.males_gmm.score(audio))
        is_male_log_likelihood = is_male_scores.sum()

        if is_male_log_likelihood > is_female_log_likelihood:
            return "male"
        else:
            return "female"


if __name__ == "__main__":
    print(GenderIdentifier.predict("/females/f0001_us_f0001_00033.wav"))
