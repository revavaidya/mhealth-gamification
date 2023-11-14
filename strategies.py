from collections import Counter

data_set = " badges, points, leaderboards, avatars, challenges, levels " \
 "leaderboards, challenges, levels, connection (relatedness), achievement, feedback, prompting, tracking" \
"Social influences, Challenges, collaboration ,Competition, High Scores, Badges, Narrative, Streaks, Points, Levels, Unlockable content Lifelines" \
"feedback,\
goal-setting, point, scores, badges, levels, \
challenges, competitions; relatedness support, social feedback, recognition, \
comparison  leaderboards, teams, communication functions;  autonomy \
avatars, environments, user choice in goals, activities, \
narratives" \
"Points, collaboration, levels, rewards, feedback"


# split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
Counters_found = Counter(split_it)
#print(Counters)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counters_found.most_common(7)
print(most_occur)