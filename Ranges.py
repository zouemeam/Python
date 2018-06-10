from math import sqrt
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                       'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                       'The Night Listener': 3.0},
         'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                          'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                          'You, Me and Dupree': 3.5},
         'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                              'Superman Returns': 3.5, 'The Night Listener': 4.0},
         'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                          'The Night Listener': 4.5, 'Superman Returns': 4.0,
                          'You, Me and Dupree': 2.5},
         'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                          'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                          'You, Me and Dupree': 2.0},
         'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                           'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
         'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


#Euclidean distance algorithm

# def sim_distance(prefs, person1,person2):
# 	si={}
# 	for item in prefs[person1]:
# 		if item in prefs[person2]:
# 			si[item]=1
# 	if len(si) == 0:
# 		return 0
# 	sumofsquares=sum([(prefs[person1][movie]-prefs[person2][movie])**2 for movie in prefs[person1] if movie in prefs[person2]])
# 	return 1/(1+sumofsquares)

#Pearon Correlation Score

person1 = 'Lisa Rose'
person2 = 'Gene Seymour'
print(sim_distance(critics,person1,person2))

#