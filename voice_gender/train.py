import os
import pickle
import warnings
import numpy as np
from sklearn.mixture import GaussianMixture as GMM
from voice_gender.features import extract_features

warnings.filterwarnings("ignore")


class ModelsTrainer:

    def __init__(self, females_files_path, males_files_path):
        self.females_training_path = females_files_path
        self.males_training_path = males_files_path

    def train(self):
        # collect voice features
        male_voice_features, female_voice_features = self.collect_features()
        # generate gaussian mixture models
        # TODO configurable
        females_gmm = GMM(n_components=16, covariance_type='diag', n_init=3)
        males_gmm = GMM(n_components=16, covariance_type='diag', n_init=3)
        # fit features to models
        females_gmm.fit(female_voice_features)
        males_gmm.fit(male_voice_features)
        return males_gmm, females_gmm

    def collect_features(self):
        """
    	Collect voice features from various speakers of the same gender.

    	Args:
    	    files (list) : List of voice file paths.

    	Returns:
    	    (array) : Extracted features matrix.
    	"""
        females = [os.path.join(self.females_training_path, f) for f in
                   os.listdir(self.females_training_path)]
        males = [os.path.join(self.males_training_path, f) for f in
                 os.listdir(self.males_training_path)]

        male_features = np.asarray(())
        # extract features for each speaker
        for file in males:
            print(file)
            # extract MFCC & delta MFCC features from audio
            vector = extract_features(file)
            # stack the features
            if male_features.size == 0:
                male_features = vector
            else:
                male_features = np.vstack((male_features, vector))

        female_features = np.asarray(())
        # extract features for each speaker
        for file in females:
            print(file)
            # extract MFCC & delta MFCC features from audio
            vector = extract_features(file)
            # stack the features
            if female_features.size == 0:
                female_features = vector
            else:
                female_features = np.vstack((female_features, vector))

        return male_features, female_features

    def save(self, gmm, filename):
        """ Save Gaussian mixture model using pickle.

            Args:
                gmm        : Gaussian mixture model.
                name (str) : File name.
        """
        if not filename.endswith(".gmm"):
            filename += ".gmm"
        with open(filename, 'wb') as gmm_file:
            pickle.dump(gmm, gmm_file)


if __name__ == "__main__":
    models_trainer = ModelsTrainer("/home/user/SLR45/females",
                                   "/home/user/SLR45/males")
    m, f = models_trainer.train()
    models_trainer.save(m, "males")
    models_trainer.save(f, "females")
