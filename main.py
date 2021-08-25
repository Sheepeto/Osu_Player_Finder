from selenium import webdriver
import random
import json

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
broken = False

def get_web_page(number):
    driver.get(f'https://osu.ppy.sh/users/{number}')

def generate_number():

    try:
        with open('./Users.txt') as f:
            Users = json.load(f)
    except FileNotFoundError:
        print("Could not load amounts.json")
        Users = {"Users": []}

    random_number = random.randint(2,15210892)

    if random_number in Users:
        generate_number()

    else:
        Users['Users'].append(random_number)
        with open(f'./Users.txt', 'w+') as f:
            json.dump(Users, f)
        print(len(Users['Users']))
        get_web_page(random_number)


generate_number()


