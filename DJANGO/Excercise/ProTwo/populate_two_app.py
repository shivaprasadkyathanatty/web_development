import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()
import random
from two_app.models import Topic,AccessRecord,Webpage,User
from faker import Faker
fakegen = Faker()
topics = ['search','social','market place','news','games']
def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date=fakegen.date()
        fake_name = fakegen.company()
        first_name=fakegen.first_name()
        last_name=fakegen.last_name()
        email=fakegen.email()
        user=User.objects.get_or_create(fname=first_name,lname=last_name,eml=email)[0]
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        accRec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__=='__main__':
    print ("Populating the Databases Please wait")
    populate(20)
    print ("Populating Completed")
