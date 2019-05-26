import urllib.request
from os.path import expanduser
import os
import math
import tarfile


def downloadSLR45(path=expanduser("~/SLR45.tgz")):
    zip_url = "http://www.openslr.org/resources/45/ST-AEDS-20180100_1-OS.tgz"
    urllib.request.urlretrieve(zip_url, path)


def extract_dataset(compressed_dataset_file_name=expanduser("~/SLR45.tgz"),
                    dataset_directory=expanduser("~/SLR45")):
    tar = tarfile.open(compressed_dataset_file_name, "r:gz")
    tar.extractall(dataset_directory)
    tar.close()


def train_test_split(dataset_dict, f_or_m):
    training_data, testing_data = [], []

    for i in range(1, 5):
        length_data = len(dataset_dict[f_or_m + "000" + str(i)])
        length_separator = math.trunc(length_data * 2 / 3)

        training_data += dataset_dict[f_or_m + "000" + str(i)][
                         :length_separator]
        testing_data += dataset_dict[f_or_m + "000" + str(i)][
                        length_separator:]

    return training_data, testing_data


if __name__ == "__main__":
    dataset_directory = expanduser("~/SLR45")
    # select females files and males files
    file_names = [fname for fname in os.listdir(dataset_directory) if
                  ("f0" in fname or "m0" in fname)]
    dataset_dict = {"f0001": [], "f0002": [], "f0003": [], "f0004": [],
                    "f0005": [],
                    "m0001": [], "m0002": [], "m0003": [], "m0004": [],
                    "m0005": [], }

    # fill in dictionary
    for fname in file_names:
        dataset_dict[fname.split('_')[0]].append(fname)
    # divide and group file names
    training_set, testing_set = {}, {}
    training_set["females"], testing_set["females"] = train_test_split(
        dataset_dict, "f")
    training_set["males"], testing_set["males"] = train_test_split(
        dataset_dict, "m")


    def move_files(src, dst, group):
        for fname in group:
            os.rename(src + '/' + fname, dst + '/' + fname)


    move_files(dataset_directory, expanduser("~/SLR45/TrainingData/females"),
               training_set["females"])
    move_files(dataset_directory, expanduser("~/SLR45/TrainingData/males"),
               training_set["males"])
    move_files(dataset_directory, expanduser("~/SLR45/TestingData/females"),
               testing_set["females"])
    move_files(dataset_directory, expanduser("~/SLR45/TestingData/males"),
               testing_set["males"])
