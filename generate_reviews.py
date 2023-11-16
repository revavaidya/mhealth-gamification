from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json
import os

apps_list = ["Impulse - Brain Training",
"Planet Fitness Workouts",
"Flo Period Pregnancy Tracker",
"MyFitness Pal Calorie Counter",
"Yuka Food Cosmetic Scanner",
"ShutEye Sleep Tracker Sound",
"Me Daily Routine Planner",
"Blood Pressure App Health Body",
"BetterMe Health Coaching",
"JustFit Lazy Workout Fit",
"Sweatcoin Walking Step Counter",
"InPulse Heart Rate Monitor",
"All Trails Hike Bike Run",
"myCigna",
"I am Daily Affirmations",
"BetterSleep Relax and Sleep",
"Paired Couples Relationship",
"Finch Self Care Pet",
"Motivation Daily quotes",
"Aetna Health ",
"Calm",
"Lose It Calorie Counter",
"Strava",
"Peloton",
"Nike Run Club",
"Balance Meditation Sleep",
"Mindbody Fitness Salon Spa",
"Breeze Mental Health",
"Calorie Counter My Net Diary",
"Fitbit Health Fitness",
"Peak"
]

import time
start = time.time()
folder_path = os.getcwd()
subdir_name = 'reviews'
new_subdirectory_path = os.path.join(folder_path, subdir_name)
if not os.path.exists(new_subdirectory_path):
    # Create the new subdirectory
        os.makedirs(new_subdirectory_path)
        print(f"Subdirectory '{subdir_name}' created successfully.")
created = False

for x in apps_list:
    app_idx = AppStore(country="us", app_name=x)
    app_idx.review(how_many=1500)

    df = pd.DataFrame(np.array(app_idx.reviews),columns=['review'])
    df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
    df2['App_Name'] = x
    df2.head()
    store_csv = x + ".csv"
    csv_file_path = os.path.join(new_subdirectory_path, store_csv)
    df2.to_csv(csv_file_path, index=False)
    print("Added", x, "to" , store_csv)

end = time.time()
print("Time to compute using flair on leaderboard was")


