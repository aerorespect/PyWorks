import requests
import bs4 as bs
import matplotlib.pyplot as plt
import pandas as pd
import time

season = 1 
start_time = time.time()

seasonEnd = False      
# title = "BreakingBad"
title = input ('input title : ')    #input the title
# title = 'GoT'
print ('Title : ' + str(title))

link = input ('input IMDB Link : ')     #input IMDB Link (e.g : 'https://www.imdb.com/title/tt0944947/episodes?season=tt0944947' for Game of Thrones
# link = 'https://www.imdb.com/title/tt0944947/episodes?season=tt0944947'

potong, sep, after = link.partition("=")
urlRaw = str(potong) + '='


def ExtractIMDBSeries (soup):
    # function to scrape episode number, description and rating
    episodes_list = soup.find('div', attrs={'class': 'list detail eplist'}).findAll('strong')
    episode = 1
    totalEpisodes = []
    for each in episodes_list:
        episodes_item = []
        episodes_item.append(episode)
        episodes_item.append(season)    # extract episode number
        episodes_item.append(each.findPrevious('div', attrs={'class': 'airdate'}).text)
        episodes_item.append(each.text)    # extract episode title
        episodes_item.append(each.findNext('div', attrs={'class': 'item_description'}).text)     #extract episode description

        if each.findNext('span', attrs={'class': 'ipl-rating-star__rating'}):
            rating_value = each.findNext('span', attrs={'class': 'ipl-rating-star__rating'}).text   #extract episode IMDB rating
            episodes_item.append(float(rating_value))
        else:
            rating_value = 0
            episodes_item.append(float(rating_value))

        totalEpisodes.append(episodes_item)
        episode += 1

    return totalEpisodes    #list of episode number, airdate, title, description, and rating for one season



def checkUrl(url, season):
    #function to check how many season available for that series
    url = str(url) + str(season)
    sauce = requests.get(url)
    soup = bs.BeautifulSoup(sauce.text, 'html.parser')
    urlNext = str(url) + str(season + 1)
    sauceNext = requests.get(urlNext)
    soupNext = bs.BeautifulSoup(sauceNext.text, 'html.parser')

    if soup.find('h3', attrs={'id': 'episode_top'}) == soupNext.find('h3', attrs={'id': 'episode_top'}):
        #if this webpage is same as the previous webpage, it means there is no more new seasons
        seasonEnd = True
    else:
        seasonEnd = False

    return seasonEnd

writer = pd.ExcelWriter(str(title)+'_ratings.xlsx')

bigData = pd.DataFrame()


while seasonEnd == False :
    #iterate to extract data from all season
    seasonEnd = checkUrl(urlRaw, season)
    url = str(urlRaw) + str(season)
    sauce = requests.get(url)
    soup = bs.BeautifulSoup(sauce.text, 'html.parser')
    print('Season ' + str(season))
    bigData = bigData.append(ExtractIMDBSeries(soup),ignore_index = True)
    season += 1

bigData.columns = ['episode', 'season', 'airdate', 'title', 'description', 'rating']


bigData['TotalEpisode'] = bigData.index + 1

ax=plt.gca()


for j in bigData['season'].unique():
    if j == 1:
        bigData[bigData['season'] == j].plot(kind='line', x='TotalEpisode', y='rating', ax=ax, label='season ' + str(j))
    else:
        temp = bigData[bigData['season'] == j].copy()
        temp.loc[-1] = bigData[bigData['season'] == j-1].iloc[-1].copy()
        temp.index = temp.index+1
        temp = temp.sort_index()
        temp.plot(kind='line', x='TotalEpisode', y='rating', ax=ax, label='season ' + str(j))

plt.show()   
#save plot figure
plt.savefig (title + '_ratings.png')
writer.save()
print (bigData)
print (time.time()-start_time)
