from jira import JIRA
from os import system, name
import time

jira = JIRA(basic_auth=("email", "secret"), options={'server': 'jira.atlassian.net'})


def clear_cmd():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def epik_transform():
    global epicPrint
    epicPrint = str(input("""
    Wybierz epik, wpisując odpowiadający numerek z listy:
    XXXX
    """))
    match epicPrint:
        case '1':
            epicPrint = '10002'
        case '2':
            epicPrint = '10003'
        case '3':
            epicPrint = '10037'
        case '4':
            epicPrint = '10045'
        case '5':
            epicPrint = '10120'
        case '6':
            epicPrint = '11041'
        case '7':
            epicPrint = '11190'
        case '8':
            epicPrint = '11225'
        case '9':
            epicPrint = '11227'
        case '10':
            epicPrint = '11359'
        case _:
            epik_transform()


def create_issue():
    global summary
    global description
    new_issue_fields = {
        'project': {'key': 'BOKL'},
        'summary': summary,
        'description': description,
        'issuetype': {'id': '10003'},
        'parent': {'id': epicPrint}
    }
    new_issue = jira.create_issue(fields=new_issue_fields)
    jira.assign_issue(new_issue, assignee='email')
    print("Udało się! Zgłoszenie dodane :) Oto detale zgłoszenia:\n")
    print(f"Temat zgłoszenia: {summary}\nOpis: {description}\nNumer zgłoszenia: {new_issue.key}")
    time.sleep(10)


summary = str(input("Wpisz temat zgłoszenia\n"))
description = str(input("Wpisz opis zgłoszenia\n"))
epicPrint = ''
clear_cmd()
epik_transform()
create_issue()
