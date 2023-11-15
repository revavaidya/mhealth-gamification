from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json
import os
apps_list = ["Impulse - Brain Training",
"Planet Fitness Workouts",
"Flo Period Pregnancy Tracker",
"MyFitness Pal Calorie Counter",
"Yuka Food Cosmetic Scanner"
]

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
    app_idx.review(how_many=100)

    df = pd.DataFrame(np.array(app_idx.reviews),columns=['review'])
    df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
    df2['App_Name'] = x
    df2.head()
    store_csv = x + ".csv"
    csv_file_path = os.path.join(new_subdirectory_path, store_csv)
    df2.to_csv(csv_file_path, index=False)
    print("Added", x, "to" , store_csv)
    #created = True


    #   strava = AppStore(country="us", app_name="Impulse - Brain Training")
    # strava.review(how_many=1500)

    # df = pd.DataFrame(np.array(strava.reviews),columns=['review'])
    # df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
    # df2.head()

    # df2.to_csv('reviews_myimpusle.csv')


# -*- coding: utf-8 -*-
# from bs4 import BeautifulSoup
# import requestsheaders = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
# url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone &_sacat=0&LH_TitleDesc=0&Model=Apple%20iPhone%208&_sop=12&LH_PrefLoc=0&rt=nc&Storage%20Capacity=64%20GB&_dcat=9355'response=requests.get(url,headers=headers)
# soup=BeautifulSoup(response.content,'lxml')