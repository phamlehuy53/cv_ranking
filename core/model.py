
from cv_ranking.utils.score_cv import *
from cv_ranking.utils.ranking import *
from typing import Dict, List
import argparse
from numpy import iterable
import pandas as pd
import os

NUMBER_OF_CRITERIA = 12


FEATURE_SCORING = {
    'info': {
        'features': ['CanEmail', 'CanTelNum', 'CanFullName'],
        'fn': pointing_person_info
    },
    'introduction': {
        'features': ['CanDob', 'SexCode', 'CanAddress', 'CanNationality', 'Interest', 'Strength', 'FutureGoals'],
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
        'features': ['LearningDiploma'],
        'fn': pointing_learning_diploma

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
        'fn': rank_diploma
    },
    'cv_image': {
        'features': ['CanImgCand'],
        'fn': pointing_cv_image
    },
    'language': {
        'features': ['LanguageCertificate'],
        'fn': pointing_language_certificate

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
# %%

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
        features = FEATURE_SCORING[k]['features']
        score_fn = FEATURE_SCORING[k]['fn']
        if not score_fn:
            continue
        dat = [ cv[ftr] for ftr in features]
        c = score_fn(*dat)
        star += c
        res[k] = c
    res['sum'] = star
    return res

def rank(cv_dicts: List[Dict]) -> List:
    """
    Evaluate CV's score

    Caculate each field's score then get sum

    Parameters
    ----------
    cv_dicts : Dict
        Each key-value is a field   
    Returns
    -------
    List:
        [{field: score}]
    """
    assert type(cv_dicts) == list
    dat = []
    for cv_dict in cv_dicts:
        cv_scores = score(cv_dict)
        dat.append(cv_scores)
    return dat
