# from utils.person_info import Person
from utils.score_cv import *
# from utils.ranking import *
from typing import Dict
from utils.json2csv import json2dict
import argparse
import pandas as pd

NUMBER_OF_CRITERIA = 12

FEATURE_SCORING = {
    'info': {
        'feature': ['CanEmail', 'CanTelNum', 'CanFullName'],
        'fn': pointing_person_info
    },
    'introduction': {
        'feature': ['CanDob', 'SexCode', 'CanAddress', 'CanNationality', 'Interest', 'Strength', 'FutureGoals'],
        'fn': pointing_personal_summary
    },
    'experience': {
        'features': ['ExperienceYears'],
        'fn': pointing_experience_year
    },
    'soft_skill': {
        'features': ['SoftSkill'],
        'fn': pointing_soft_skill
    },
    'skill': {
        'features': ['Skill'],
        'fn': pointing_skill
    },
    'graduated': {
        'features': ['LearningDiploma', 'Specialize'],
        'fn': pointing_diploma
    },
    'is_updated': {
        'features': ['IsUpdate'],
        'fn': pointing_update_cv
    },
    'learning_awards': {
        'features': ['LearningAwards'],
        'fn': None
    },
    'working_awards': {
        'features': ['WorkingAwards'],
        'fn': None
    },
    'diploma': {
        'features': ['Diploma'],
        'fn': pointing_diploma
    },
    'cv_image': {
        'features': ['CanImgCand'],
        'fn': pointing_cv_image
    },
    'language': {
        'features': ['LanguageCertificate'],
        'fn': pointing_language_certificate()
    },
    'interest': {
        'features': ['Interest'],
        'fn': None
    },
    'reference_person': {
        'features': ['ReferencePerson', 'ReferencePersonPosition'],
        'fn': pointing_reference_person
    },

}


def score(cv: Dict) -> Dict:
    """
    Score dict-type CV

    [TODO:description]

    Parameters
    ----------
    cv : Dict
        [TODO:description]

    Returns
    -------
    Dict:
        {criteria: point}
    """
    star = 0
    res = {}
    for k in FEATURE_SCORING.keys():
        features = FEATURE_SCORING[k]['feature']
        score_fn = FEATURE_SCORING[k]['fn']
        dat = [ cv[ftr] for ftr in features]
        c = score_fn(*dat)
        star += c
        res[k] = c
    res['sum'] = star
    return res

def main(args):
    json_path = args['fpath']
    json_dir = args['dir']
    output_file = args['output']
    verbose = args['verbose']
    json_paths = []
    if json_path:
        json_paths.append(json_path)
    else:
        for root_dir, sub_dir, files in os.walk(json_dir):
            if files:
                paths = list(map( lambda x: os.path.join(root_dir, x), files ))
                json_paths += paths
    print(f"Processing {len(json_paths)} files!")

    dat = []
    for json_path in json_paths:
        json_dict = json2dict(json_path=json_path)
        if not json_dict:
            print(f"Reading {json_path} failed. Check again!")
            continue
        dat.append(json_dict)

    df = pd.DataFrame(dat)
    if verbose:
        print(dat)
    else:
        df.to_csv(output_file)

    print(f"Completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-d", "--dir", help="Path to direcotry contain CVs", action="store_true", default=None)
    group1.add_argument("-f", "--fpath", help="Path to CV file", action="store_true", default=None)
    
    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument('-o', "--output", help="Path to output csv", default=None, action="store_true")
    group2.add_argument('-v', "--verbose", help="Print to stdout", default=False, action="store_true")
    
    args = parser.parse_args()

    main(args)
