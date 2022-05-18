# 1st we should define a function that filters the valid line up for the teams 
# 2nd categorize by the position they play as well as the team 
# 3rd maybe create a class for the teams and another one for positions 

from pip._vendor import requests as r 
league = r.get('https://foxes90-prempundit.herokuapp.com/players')
if league.status_code == 200:
    league = league.json()
league['Players']

# class team: 
#     #nested dictionary, sort them by team
#     def clubs
#     #each club is a nested dictionary

#     def eligibility():
#         if player injured or suspended = True
#             pop Out
#         else insert in line up 
#      
# 