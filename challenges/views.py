from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

months_challenge = {
    "jan":"Eat no meat",
    "feb":"walk 20 minutes",
    "march":"learn new skill",
    "april":"Eat no meat",
    "may":"walk 20 minutes",
    "june":"learn new skill",
    "july":"Eat no meat",
    "august":"walk 20 minutes",
    "september":"learn new skill",
    "october":None,
    "november":None,
    "december":None
}



def index(request):
    months = list(months_challenge.keys())
    return render(request,"challenges/index.html",{
        "months":months
    })
def monthly_challenges_by_number(request,month):
    months = list(months_challenge.keys())

    if month > len (months):
        return HttpResponseNotFound("Invalid Month")
    else :
        pass
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request,month):
    try:
        challenge_text = months_challenge[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text , # new
            "month":month.capitalize()           # new
        })
    except:
        raise Http404()



