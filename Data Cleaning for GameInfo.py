import pandas as pd
import json

# Load data
file = 'S:/NUS/EBAC5006 Project/Data/PlayStoreGame/PlayStoreGameAppInfoReview.json'
data =  pd.read_json(file)


# Change data.id into numbers
i = 0
for keys in data:
    data[i] = data.pop(keys)
    i = i + 1
    
data.keys()

# See how the information distributed 

data[1]['appInfo'] # 固定47条信息
data[1]['appInfo'].keys()

'''
Output: 
    
dict_keys(['title', 'description', 'descriptionHTML', 'summary', 'summaryHTML', 
'installs', 'minInstalls', 'score', 'ratings', 'reviews', 'histogram', 'price', 'free', 
'currency', 'sale', 'originalPrice', 'saleText', 'offersIAP', 'inAppProductPrice', 'size',
 'androidVersion', 'androidVersionText', 'developer', 'developerId', 'developerEmail', 
 'developerWebsite', 'developerAddress', 'privacyPolicy', 'developerInternalID',
 'genre', 'genreId', 'icon', 'headerImage', 'screenshots', 'video', 'videoImage',
 'contentRating', 'contentRatingDescription', 'adSupported', 'containsAds', 'released',
 'updated', 'version', 'recentChanges', 'recentChangesHTML', 'appId', 'url'])

'''

totalinfo = ['title', 'description', 'descriptionHTML', 'summary', 'summaryHTML', 
'installs', 'minInstalls', 'score', 'ratings', 'reviews', 'histogram', 'price', 'free', 
'currency', 'sale', 'originalPrice', 'saleText', 'offersIAP', 'inAppProductPrice', 'size',
 'androidVersion', 'androidVersionText', 'developer', 'developerId', 'developerEmail', 
 'developerWebsite', 'developerAddress', 'privacyPolicy', 'developerInternalID',
 'genre', 'genreId', 'icon', 'headerImage', 'screenshots', 'video', 'videoImage',
 'contentRating', 'contentRatingDescription', 'adSupported', 'containsAds', 'released',
 'updated', 'version', 'recentChanges', 'recentChangesHTML', 'appId', 'url']

for ele in totalinfo:
    print('<{}>'.format(ele), '\n', data[1]['appInfo'][ele])


# Prepare a dataframe only with GameId
GameId = [ *range(1,171,1) ]
GameInfo_df = pd.DataFrame(GameId)
GameInfo_df.columns = ['GameID']

# load 47 columns of information into the dataframe
i = 0
j = 0
while j < 47:
    i = 0
    info = []
    while i <= 169:
        #print(i,j)
        info.append(data[i]['appInfo'][totalinfo[j]])
        i = i + 1
    GameInfo_df[totalinfo[j]] = info
    #print(len(info))    
    j = j + 1
    
GameInfo_df = GameInfo_df.set_index('GameID')
# GameInfo_df.to_csv('GameInfo.csv')

'''
后续可能需要：
1. 个别游戏名是乱码，需要决定一下是直接删，还是手动去搜这个游戏，把名称改了（毕竟只有170个游戏）
2. installs给的数量都是很笼统的，都是500，000+， 1，000，000+这样的； 可以直接看mininstall
3. histogram列意义不明
4. 网址类的data应该就直接删了把
5. released date改成date类型
6. update意义不明，是指总共多少人进行过版本更新吗？
7. genre里面可能包含多个元素，可能后续需要分开
'''






