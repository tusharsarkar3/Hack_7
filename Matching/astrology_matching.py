from kerykeion import KrInstance, Report
from kerykeion.relationship_score import RelationshipScore
from .models import Questions

# Args: Name, year, month, day, hour, minuts, city, nation(optional)
def give_relationship_score(request,matches):
    user = Questions.objects.get(user=request.user)
    dob = user.dob.strip().split("-")
    tob = user.tob.strip().split(":")
    user_characteristics = KrInstance(request.user.first_name + " " + request.user.last_name,
                                      dob[2], dob[1], dob[0], tob[0], tob[1], user.pob)
    for match in matches:
        match_q = Questions.objects.get(user=match.user)
        dob_2 = match_q.dob.strip().split("-")
        tob_2 = match_q.tob.strip().split(":")
        match_characteristics = KrInstance(match.user.first_name + " " + match.user.last_name,
                                          dob_2[2], dob_2[1], dob_2[0], tob_2[0], dob_2[1], match_q.pob)

        score = RelationshipScore(user_characteristics,match_characteristics)
        match.match_score_western = score

