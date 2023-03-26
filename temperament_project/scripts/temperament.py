import scripts.TestQuestions
import random
import scripts.colleges_Info

QUESTION_LIST = scripts.TestQuestions.QUESTIONS


def check_answers(participant_answers,
                  extravert_introvert_yes=scripts.TestQuestions.EXTROVERSION_INTROVERSION_YES,
                  extravert_introvert_no=scripts.TestQuestions.EXTROVERSION_INTROVERSION_NO,
                  neuroticism=scripts.TestQuestions.NEUROTICISM_YES,
                  lie_scale_yes=scripts.TestQuestions.LIE_SCALE_YES,
                  lie_scale_no=scripts.TestQuestions.LIE_SCALE_NO):
    extraversion_score = 0
    neuroticism_score = 0
    lie_score = 0

    for question_number, answer in enumerate(participant_answers, start=1):
        if question_number in extravert_introvert_yes and answer == True:
            extraversion_score += 1

        elif question_number in extravert_introvert_no and answer == False:
            extraversion_score += 1

        elif question_number in neuroticism and answer == True:
            neuroticism_score += 1

        elif question_number in lie_scale_yes and answer == True:
            lie_score += 1

        elif question_number in lie_scale_no and answer == False:
            lie_score += 1

    return extraversion_score, neuroticism_score, lie_score


def temperament_calculate(extraversion_score, neuroticism_score, lie_score):
    participant_is_lying = False

    if lie_score > 4:
        participant_is_lying = True

    if 0 <= extraversion_score <= 12 and 12 <= neuroticism_score <= 24:
        return 'меланхолик', participant_is_lying

    elif 0 <= extraversion_score <= 12 and 0 <= neuroticism_score <= 12:
        return 'флегматик', participant_is_lying

    elif 12 <= extraversion_score <= 24 and 0 <= neuroticism_score <= 12:
        return 'сангвиник', participant_is_lying

    elif 12 <= extraversion_score <= 24 and 12 <= neuroticism_score <= 24:
        return 'холерик', participant_is_lying

    # Возвращает текст с теорией о темпераменте участника


def get_temperament_text(temperament, user_lying=False):
    if user_lying:
        return str(scripts.TestQuestions.TEMPERAMENT[temperament]) + scripts.TestQuestions.INSINCERITY_TEXT

    return str(scripts.TestQuestions.TEMPERAMENT[temperament])


def select_colleges_under_temperament(temperament, college_list):
    for college in college_list:
        print('-' * 50)
        print(college)
        for profession in college_list[college].items():
            if temperament in profession[-1]:
                print('Под ваш темперамент подходит профессия:', profession[0])
