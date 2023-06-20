"""Problem: Given a list of client emails, create a function that takes in the list as an argument and returns a new list with only the domain of each email. This was inspired by an actual problem I did at work recently.

clients = ['brucewayne@gotham.com',
'homer_simpson@springfieldnuclear.com',
'hank_hill@arlenpropane.com',
'petergriffin@pawtucketbrewery.com']"""



import re

def get_domains(clients):
    separated= [re.split("@",each_email)[1] for each_email in clients]
    print(separated)


clients = ['brucewayne@gotham.com',
'homer_simpson@springfieldnuclear.com',
'hank_hill@arlenpropane.com',
'petergriffin@pawtucketbrewery.com']

get_domains(clients)