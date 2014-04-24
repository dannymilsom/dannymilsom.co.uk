import json
import datetime
import json
from twython import Twython

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from about.forms import ContactForm


def contact(request):
    """
    Returns a contact form and data taken from the twitter API via twython.
    """

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
                clean_data = form.cleaned_data
                send_mail('New website email', clean_data['message'], 
                          clean_data['email'], ['dannymilsom@hotmail.co.uk'])

                if request.is_ajax():
                    json_respsone = {
                        'errors': False,
                        'message': "Thanks for getting in touch {}. "
                                   "I'll endevour to reply within 24 hours! "
                                   "Danny".format(clean_data['name'])
                    }

                    return HttpResponse(json.dumps(json_respsone), 
                                        content_type="application/json")
        else:
            json_response = {
                'errors':  form.errors,
            }
            return HttpResponse(json.dumps(json_response), 
                                content_type="application/json")

    data = {'form': form}

    # get latest twitter posts
    twitter = Twython('IWhiXqAMXlQizxNbmGYUHg', 
        '230gGuTQm2lCi8YcmZcf4SibseQJmmNE5Wn3ZBvAg', 
        '168158421-dZZYSYdsE43nKRgNGx5wzKhhHlb7FIA1XWJvlqNJ',
        'CimXe6LTOeWPaTCETsg6MpcpZ6FInIyxGns2xSKtQfJWE'
    )

    try:
        tweets = twitter.get_user_timeline(count=4)
    except:
        tweets = None

    if tweets:
        for tweet in tweets:
            tweet['text'] = Twython.html_for_tweet(tweet)

        avatar_url = tweets[0]['user']['profile_image_url']

        data['tweets'] = tweets
        data['avatar'] = avatar_url

    return render(request, 'contact.html', data)