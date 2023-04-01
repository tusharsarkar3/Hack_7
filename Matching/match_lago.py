from .models import Questions, Global_stats
import math

def num_similarities_binary(user_answers, matches):
    counter = 0
    if user_answers.datechar == matches.datechar:
        counter +=1
    if user_answers.animal == matches.animal:
        counter +=1
    if user_answers.daynight == matches.daynight:
        counter +=1
    if user_answers.minmax == matches.minmax:
        counter +=1

def num_similarities_multi(user_answers, matches):
    #movie
    user_answers.movie
    #books
    #music


def matching_algorithm(request):
    user_answers = Questions.objects.get(user=request.user)

    filter_matches = Questions.objects.filter(state=user_answers.state, city=user_answers.city,
                                              age__gte=user_answers.partner_age_low, age__lte=user_answers.partner_age_high,
                                              gender = user_answers.gender, religion = user_answers.partner_religion,
                                              mothertongue = user_answers.partner_mothertongue,
                                              relationshiptype = user_answers.relationshiptype, edu = user_answers.partner_edu,
                                              profession = user_answers.partner_profession
                                              )
    final_matches = []
    for matches in filter_matches:
        number_of_similarities_binary_fields = num_similarities_binary(user_answers, matches)
        if number_of_similarities_binary_fields >= Global_stats.binary_question_similarity_mean:
            print("Consider them")
            final_matches.append(matches)
        number_of_similarities_binary_fields = num_similarities_multi(user_answers.movie, matches.movie)




