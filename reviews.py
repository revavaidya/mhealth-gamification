from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json
strava = AppStore(country="us", app_name="strava")
strava.review(how_many=1500)

df = pd.DataFrame(np.array(strava.reviews),columns=['review'])
df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
df2.head()

df2.to_csv('reviews_strava.csv')


# -*- coding: utf-8 -*-
# from bs4 import BeautifulSoup
# import requestsheaders = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
# url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=iphone &_sacat=0&LH_TitleDesc=0&Model=Apple%20iPhone%208&_sop=12&LH_PrefLoc=0&rt=nc&Storage%20Capacity=64%20GB&_dcat=9355'response=requests.get(url,headers=headers)
# soup=BeautifulSoup(response.content,'lxml')