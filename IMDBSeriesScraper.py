import requests
import bs4 as bs
import matplotlib.pyplot as plt
import pandas as pd

season = 1

seasonEnd = False
# title = "BreakingBad"
title = input ('input title : ')

print ('Title : ' + str(title))

link = input ('input IMDB Link : ')

potong, sep, after = link.partition("=")
urlRaw = str(potong) + '='

# urlRaw = 'https://www.imdb.com/title/tt0944947/episodes?season='        #Friends : tt0108778 , GOT : tt0944947, BreakingBad : tt0903747, Dexter : tt0773262

# function to scrape episode number, description and rating
def ExtractIMDBSeries (soup):
    episodes_list = soup.find('div', attrs={'class': 'list detail eplist'}).findAll('strong')
    episode = 1
    totalEpisodes = []
    for each in episodes_list:
        episodes_item = [0, 1, 2, 3, 4]
        episodes_item[0] = episode      # extract episode number
        episodes_item[1] = each.findPrevious('div', attrs={'class': 'airdate'}).text
        episodes_item[2] = each.text    # extract episode title
        episodes_item[3] = each.findNext('div', attrs={'class': 'item_description'}).text     #extract episode description

        if each.findNext('span', attrs={'class': 'ipl-rating-star__rating'}):
            rating_value = each.findNext('span', attrs={'class': 'ipl-rating-star__rating'}).text   #extract episode IMDB rating
            episodes_item[4] = float(rating_value)
        else:
            rating_value = 0
            episodes_item[4] = float(rating_value)

        totalEpisodes += [episodes_item]
        episode += 1

    return totalEpisodes



def checkUrl(url, season):
    url = str(url) + str(season)
    sauce = requests.get(url)
    soup = bs.BeautifulSoup(sauce.text, 'html.parser')
    urlNext = str(url) + str(season + 1)
    sauceNext = requests.get(urlNext)
    soupNext = bs.BeautifulSoup(sauceNext.text, 'html.parser')

    if soup.find('h3', attrs={'id': 'episode_top'}) == soupNext.find('h3', attrs={'id': 'episode_top'}):
        seasonEnd = True
    else:
        seasonEnd = False

    return seasonEnd

writer = pd.ExcelWriter(str(title)+'_ratings.xlsx')
bigData = []

while seasonEnd == False :
    seasonEnd = checkUrl(urlRaw, season)
    url = str(urlRaw) + str(season)
    sauce = requests.get(url)
    soup = bs.BeautifulSoup(sauce.text, 'html.parser')
    print('Season ' + str(season))
    result = ExtractIMDBSeries(soup)
    print (result)
    dfwrite = pd.DataFrame(result, columns=['episode', 'airdate', 'title', 'description', 'rating']) #title', 'description',
    # dfwrite.to_excel(writer, sheet_name='Season ' + str(season))
    print (dfwrite)
    bigData += [dfwrite]
    season += 1

for a in range(len(bigData)):
    print (bigData[a])

ax=plt.gca()
printData = []

for i in range(len(bigData)):
    if i == 0 :
        print('aaa' + str(i))
        bigData[i]['totalEpisode'] = bigData[i]['episode']
        printData += [bigData[i]]
        print (bigData[i])
    else :
        print ('aaa' + str(i))
        bigData[i]['totalEpisode'] = bigData[i-1]['totalEpisode'].iloc[-1] + bigData[i]['episode']
        printData += [bigData[i]]
        print(bigData[i])


for j in range(len(printData)):
    if j == 0:
        printData[j] = printData[j].append(printData[j+1].iloc[0])
    else :
        if j == len(printData)-1:
            printData[j] = bigData[j]
        else :
            printData[j] = printData[j].append(bigData[j+1].iloc[0])

    printData[j].plot(kind='line', x='totalEpisode', y='rating', ax=ax, label='season ' + str(j + 1))

plt.savefig (title + '_ratings.png')
writer.save()
