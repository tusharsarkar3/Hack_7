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
    return len(set(user_answers.strip().split(",")) & set(matches.strip().split(",")))



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
        try:
            number_of_similarities_binary_fields = num_similarities_binary(user_answers, matches)
            if number_of_similarities_binary_fields >= Global_stats.binary_question_similarity_mean:
                print("Consider them")
                final_matches.append(matches)
            number_of_similarities_movies = num_similarities_multi(user_answers.movie, matches.movie)
            if number_of_similarities_movies >= Global_stats.movies_number_of_similarity_mean:
                print("Consider them")
                final_matches.append(matches)

            number_of_similarities_books = num_similarities_multi(user_answers.books, matches.books)
            if number_of_similarities_books >= Global_stats.books_number_of_similarity_mean:
                print("Consider them")
                final_matches.append(matches)

            number_of_similarities_music = num_similarities_multi(user_answers.music, matches.music)
            if number_of_similarities_music >= Global_stats.music_number_of_similarity_mean:
                print("Consider them")
                final_matches.append(matches)

            freq = {}
            for item in matches:
                if (item in freq):
                    freq[item] += 1
                else:
                    freq[item] = 1

            match_made_in_heaven = []
            for key, value in  freq.items():
                if value ==4:
                    match_made_in_heaven.append(key)
            if len(match_made_in_heaven) == 0:
                return None
            return match_made_in_heaven
        except:
            return None




