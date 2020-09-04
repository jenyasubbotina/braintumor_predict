import os
import pandas as pd
import argparse

def folder_structure_to_csv(path: str, name: str):

    all_folders = [["no_train","yes_train"],["no_test","yes_test"],
                   ["no_validation","yes_validation"]]
    for folders in all_folders :
        paths = []
        labels = []
        for folder in folders:
            for image in os.listdir(path+'/'+folder):
                paths.append(folder+'/'+image)
                labels.append(folder.split("_")[0])
            df = pd.DataFrame({'image_path': paths,'label': labels})
            split_name=name.split(".")
            save_path=split_name[0]+"_"+folder.split("_")[-1]+"."+split_name[-1]
            df.to_csv(save_path, index=None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create CSV from folder structure of a data-set')
    parser.add_argument('-p', '--path', type=str, required=True, help='Path to the data-set directory')
    parser.add_argument('-n', '--name', type=str, required=True, help='Name of the data-set')
    args = parser.parse_args()
    folder_structure_to_csv(args.path, args.name)
