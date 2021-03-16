from utils.person_info import Person
from utils.score_cv import *
from utils.ranking import *
from typing import Dict
from utils.json2csv import json2dict
NUMBER_OF_CRITERIA = 12

FEATURE_SCORING = {
    'info': {
        'feature': ['CanEmail', 'CanTelNum', 'CanFullName'],
        'fn': None
    },
    'introduction': {
        'feature': ['CanDob', 'SexCode', 'CanAddress', 'CanNationality', 'Interest', 'Strength', 'FutureGoals'],
        'fn': None
    },
    'experience': {
        'features': ['ExperienceYears'],
        'fn': None
    },
    'soft_skill': {
        'features': ['SoftSkill'],
        'fn': None
    },
    'skill': {
        'features': ['Skill'],
        'fn': None
    },
    'graduated': {
        'features': ['LearningDiploma', 'Specialize'],
        'fn': None
    },
    'is_updated': {
        'features': ['IsUpdate'],
        'fn': None
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
        'fn': None
    },
    'cv_image': {
        'features': ['CanImgCand'],
        'fn': None
    },
    'language': {
        'features': ['LanguageCertificate'],
        'fn': None
    },
    'interest': {
        'features': ['Interest'],
        'fn': None
    },
    'reference_person': {
        'features': ['ReferencePerson', 'ReferencePersonPosition'],
        'fn': None
    },
}


def score(cv: Dict):
    star = 0
    for k in FEATURE_SCORING.keys():
        features = FEATURE_SCORING[k]['feature']
        score_fn = FEATURE_SCORING[k]['fn']
        dat = [ cv[ftr] for ftr in features]
        star += score_fn(*dat)


