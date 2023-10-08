from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 mins a day!",
    "march": "Learn Django for 20 mins a day!",
    "april": "Eat vegetables every day!",
    "may": "Drink a gallon of water daily!",
    "june": "Eat no meat for the entire month!",
    "july": "Walk for at least 20 mins a day!",
    "august": "Learn Django for 20 mins a day!",
    "september": "Eat vegetables every day!",
    "october": "Drink a gallon of water daily!",
    "november": "Eat no meat for the entire month!",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text":challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
    