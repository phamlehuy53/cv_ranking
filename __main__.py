# from utils.person_info import Person
from cv_ranking.core import model
import argparse
import pandas as pd
from cv_ranking.utils.json2csv import json2dict
# %%
def main(args):
    json_path = args.fpath
    json_dir = args.dir
    output_file = args.output
    verbose = args.verbose
    json_paths = []
    if json_path:
        json_paths.append(json_path)
    else:
        for root_dir, sub_dir, files in os.walk(json_dir):
            if files:
                paths = list(map( lambda x: os.path.join(root_dir, x), files ))
                json_paths += paths
    print(f"Processing {len(json_paths)} files!")

    cv_dicts = []
    for json_path in json_paths:
        json_dict = json2dict(json_path=json_path)
        if not json_dict:
            print(f"Reading {json_path} failed. Check again!")
            continue
        cv_dicts.append(json_dict)

    dat = model.rank(cv_dicts)
    df = pd.DataFrame(dat)
    if verbose:
        print(dat)
    else:
        df.to_csv(output_file, index=False)
    print(f"Completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-d", "--dir", help="Path to direcotry contain CVs", default=None, type=str)
    group1.add_argument("-f", "--fpath", help="Path to CV file", default=None, type=str)
    
    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument('-o', "--output", help="Path to output csv", default=None, type=str)
    group2.add_argument('-v', "--verbose", help="Print to stdout", default=False, type=str)
    
    args = parser.parse_args()

    main(args)
