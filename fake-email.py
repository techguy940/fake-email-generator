from faker import Faker
import random


def main():
    ask = input('How many e-mails you want?: ')
    try:
        ask = int(ask)
    except:
        raise ValueError('Enter an integer')

    for i in range(ask):
        domains = ['@pridemail.co' , '@zingermail.co' , '@whoamail.co' , '@oofmail.co']

        fake = Faker()

        name = fake.name()
        name = name.replace(" ","")
        name = name.lower()

        num = random.randint(0,1000)
        num = str(num)

        mail_pre = name
        mail_pre += num

        url = "https://mailsac.com/inbox/"
        domain = random.choice(domains)

        mail_check_url = url+mail_pre+domain

        print(mail_check_url)


main()
