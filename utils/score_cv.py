import re
from fuzzywuzzy import fuzz
from utils.spell_checker import correct
from utils.person_info import Person
from utils.phone_extract import *

email_address_rank = [0, 5]
experience_year_range = [[0, 1], [1, 2], [2, 3], [3, 5], [5, 100]]
skill_range = [[0, 1], [1, 3], [3, 4], [4, 5], [5, 100]]
soft_skill_range = [[0, 1], [1, 3], [3, 4], [4, 5], [5, 100]]
diploma_range = [[0, 1], [1, 3], [3, 4], [4, 5], [5, 100]]
is_update_point = [0, 5]
address_now_point = [0, 5]
reference_person_point = [0, 5]
cv_image_point = [3, 5]
interest_point = [0, 3, 5]
spell_point = [3, 5]
phone_number_point = [3,5]


def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s


def pointing_experience_year(years):
    experience_year = int(years)
    for i in range(len(experience_year_range)):
        if experience_year in range(experience_year_range[i][0], experience_year_range[i][1]):
            return i + 1
    return 0


def pointing_skill(skill):
    skill = skill.split(";")
    number_of_skills = len(skill)
    for i in range(len(skill_range)):
        if number_of_skills in range(skill_range[i][0], skill_range[i][1]):
            return i + 1
    return 0


def pointing_soft_skill(soft_skill):
    soft_skill = soft_skill.split(";")
    number_of_soft_skills = len(soft_skill)
    for i in range(len(soft_skill_range)):
        if number_of_soft_skills in range(soft_skill_range[i][0], soft_skill_range[i][1]):
            return i + 1
    return 0


def pointing_diploma(diploma):
    diploma = diploma.split(";")
    number_of_diploma = len(diploma)
    for i in range(len(diploma_range)):
        if number_of_diploma in range(diploma_range[i][0], diploma_range[i][1]):
            return i + 1
    return 0


def pointing_update_cv(is_update):
    if is_update.lower() == 'yes' or is_update.lower().find("yes") != -1:
        return is_update_point[1]
    return is_update_point[0]


def pointing_tel_num(tel_num):
    valid_check, phone = valid_phonenum(tel_num)
    if valid_check:
        return phone_number_point[1]
    return phone_number_point[0]


def pointing_cv_image(cv_image):
    if cv_image != "" and cv_image.lower().find("none") != 0:
        return cv_image_point[1]
    return cv_image_point[0]


def pointing_email_address(email_address, fullname):
    if email_address.lower().find("none") == 0 or fullname.lower().find("none") == 0:
        return 0
    email_address_point = 0
    fullname = fullname.lower()
    fullname = no_accent_vietnamese(fullname)
    fullname_no_space = fullname.replace(" ", '')
    name_split = fullname.split(" ")
    email_name = email_address.split('@')[0]
    if fuzz.ratio(fullname_no_space, email_name) > 50:
        return email_address_rank[1]
    acronym_name_1 = ''
    acronym_name_2 = ''
    for i in range(len(name_split) - 1):
        acronym_name_1 = acronym_name_1 + name_split[i][0]
    acronym_name_2 = acronym_name_2 + name_split[len(name_split) - 2][0] + name_split[len(name_split) - 1][0]
    name_split.append(acronym_name_1)
    name_split.append(acronym_name_2)
    for checker in name_split:
        if email_name.find(checker) != -1:
            email_address_point = email_address_point + 1
    if email_address_point > 1:
        return email_address_rank[1]
    return email_address_rank[0]


def pointing_personal_summary(dob, sex, address, nation, interest, strength, future_goal):
    point = 0
    dob_pattern = "^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$"
    if len(re.findall(dob_pattern, dob)) > 0:
        point += 1
    if sex.lower().find('none') != 0:
        point += 1
    if address.lower().find('none') != 0:
        point += 1
    if nation.lower().find('none') != 0:
        point += 1
    if interest.lower().find('none') != 0:
        point += 2
    if strength.lower().find('none') != 0:
        point += 2
    if future_goal.lower().find('none') != 0:
        point += 2
    return int(point/10*5)


def pointing_reference_person(reference_person, reference_person_position):
    if reference_person != "" and reference_person.lower().find("none") != 0:
        return reference_person_point[1]
    return reference_person_point[0]


def pointing_person_info(email, tel_num, fullname):
    point = int((pointing_email_address(email, fullname) + pointing_tel_num(tel_num))/2)
    return point


def pointing_learning_diploma(learning_diploma, specialize):
    if learning_diploma != "" and learning_diploma.lower().find("none") != 0:
        return 5
    return 0


def pointing_language_certificate(language_certificate):
    language_certificate = language_certificate.split(";")
    if len(language_certificate) > 5:
        return 5
    return len(language_certificate)

