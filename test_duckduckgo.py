import pytest
import requests

def test_duckduckgo_presidents_qeury():
    url = 'https://api.duckduckgo.com'
    response = requests.get(url + "?q=presidents+of+the+united+states&format=json")
    my_json = response.json()
    reltopics = my_json['RelatedTopics']
    presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Buren',
                  'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan',
                  'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland',
                  'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover',
                  'Truman', 'Eisenhower', 'Kennedy', 'Nixon', 'Ford', 'Carter', 'Reagan',
                  'Bush', 'Clinton', 'Obama', 'Trump', 'Biden']
    text = ""
    for i in reltopics:
        text += i['Text']
    i = 1
    for p in presidents:
        assert p in text
        print()
        print(p + " = passed")
        i = i + 1