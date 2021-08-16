import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"FirstProject.settings")

import django
django.setup()

from FirstApp.models import student_info
from faker import Faker
from random import *

fake = Faker()

def phone_number():
    num = ""+str(randint(6,9))
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        f_id = fake.random_int(min =10,max=100)
        f_name = fake.name()
        f_Contact = phone_number()
        student_record = student_info.objects.get_or_create(ID=f_id,
                                                            Name= f_name,
                                                            Contact = f_Contact)[0]
    #     student_record.save()
    # return student_record
if __name__ =="__main__":
    print("start populting")
    populate(30)
    print("populating complete")
