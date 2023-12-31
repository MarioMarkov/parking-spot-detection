import os
import shutil
from tqdm import tqdm


# Function to read the labels from the text file
def read_labels(label_file):
    labels = {}
    with open(label_file, "r") as file:
        for line in file:
            path, label = line.strip().split(" ")
            labels[path] = label
    return labels


# Function to split the images into separate folders based on the labels
def split_images(source_folder, label_file, destination_folder):
    labels = read_labels(label_file)
    label_files = list(labels.keys())

    for root, _, files in tqdm(os.walk(source_folder), total = 695898,desc="Finding images..."):
        for file in files:
            if file.lower().endswith(
                (".png", ".jpg", ".jpeg")
            ):  # Add more image extensions if necessary
                file_path = os.path.join(root, file)
                file_path = file_path.replace(source_folder, "")[1:]
                if file_path in label_files:
                    label = labels[file_path]
                    label_folder = os.path.join(destination_folder, label)
                    os.makedirs(label_folder, exist_ok=True)
                    shutil.copy2(os.path.join(root, file), label_folder)


# Usage example
source_folder = "data/PKLotSegmented"
label_file = "data/splits/PKLot/val.txt"
destination_folder = "pk_lot_data/val"

split_images(source_folder, label_file, destination_folder)
