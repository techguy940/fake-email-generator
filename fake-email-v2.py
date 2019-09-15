from faker import Faker
import random

fake = Faker()

domains = ['@pridemail.co' , '@zingermail.co' , '@whoamail.co' , '@oofmail.co']

def main():
    number_of_emails = int(input("How many emails you want?: "))

    try:
        int(number_of_mails)
    except:
        raise ValueError('Enter an integer!')

    for i in range(number_of_emails):
        name = fake.name()
        name = name.replace(" ","")
        name = name.lower()

        num = random.randint(0,1000)
        num = str(num)

        domain = random.choice(domains)

        e_name = name
        e_name += num

        full_email = e_name+domain

        url = "https://mailsac.com/inbox/"

        print(url+e_name+domain)
        print(full_email)
        print('======================')


main()
