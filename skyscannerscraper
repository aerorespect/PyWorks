from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import datetime as dt
import time
import random
import pandas as pd


maxlagtime = 13     #duration of sleep time between action
origin = 'london heathrow'
destination = 'jakarta'

duration = 17       #duration of days

departyear = 2019   #year depart
departmonth = 8     #month depart
departdate = 1      #date depart

returnyear = 2019   #year return
returnmonth = 8     #month return
maxreturndate = 25      #maximum return date

maxduration = maxreturndate - departdate

db = pd.DataFrame()


def choose_destination(origin,destination):
    originbar = browser.find_element_by_css_selector('#fsc-origin-search')
    time.sleep(random.uniform(0,maxlagtime))
    originbar.clear()
    time.sleep(random.uniform(0, maxlagtime))
    originbar.send_keys(origin)
    time.sleep(random.uniform(0,maxlagtime))
    destinationbar = browser.find_element_by_css_selector('#fsc-destination-search')
    time.sleep(random.uniform(0,maxlagtime))
    destinationbar.clear()
    destinationbar.send_keys(destination)
    time.sleep(random.uniform(0,maxlagtime))




def startdate(startyear, startmonth, startdate):
    dtnow = dt.datetime.now()
    if startyear > dtnow.year:
        month = (12 - dtnow.month + 1) + startmonth
    else :
        month = startmonth - dtnow.month + 1
    isostartdate = dt.datetime(startyear, startmonth, startdate).isocalendar()
    weekcalculate = dt.datetime(startyear, startmonth, 1).isocalendar()
    week = isostartdate[1] - weekcalculate[1] + 1
    weekday = dt.datetime(startyear, startmonth, startdate).isoweekday()

    browser.find_element_by_css_selector('#depart-fsc-datepicker-button > span:nth-child(1)').click()
    time.sleep(random.uniform(0, maxlagtime))
    browser.find_element_by_css_selector('#depart-calendar__bpk_calendar_nav_select').click()
    time.sleep(random.uniform(0, maxlagtime))
    browser.find_element_by_css_selector(
        '#depart-calendar__bpk_calendar_nav_select > option:nth-child(' + str(month) + ')').click()  # pick month
    time.sleep(random.uniform(0, maxlagtime))
    browser.find_element_by_css_selector(
        'tr.bpk-calendar-grid__week:nth-child(' + str(week) + ') > td:nth-child(' + str(
            weekday) + ') > button:nth-child(1) > span:nth-child(1)').click()  # pick date
    time.sleep(random.uniform(0, maxlagtime))


#enter startdate
def enddate(endyear, endmonth, enddate):
    dtnow = dt.datetime.now()
    if endyear > dtnow.year:
        month = (12 - dtnow.month + 1) + endmonth
    else:
        month = endmonth - dtnow.month + 1
    isoenddate = dt.datetime(endyear, endmonth, enddate).isocalendar()
    weekcalculate = dt.datetime(endyear, endmonth, 1).isocalendar()
    week = isoenddate[1] - weekcalculate[1] + 1
    weekday = dt.datetime(endyear, endmonth, enddate).isoweekday()

    browser.find_element_by_css_selector('#return-fsc-datepicker-button > span:nth-child(1)').click()
    time.sleep(random.uniform(0, maxlagtime))
    browser.find_element_by_css_selector('#return-calendar__bpk_calendar_nav_select').click()
    time.sleep(random.uniform(0, maxlagtime))
    browser.find_element_by_css_selector('#return-calendar__bpk_calendar_nav_select > option:nth-child('+str(month)+')').click()
    time.sleep(random.uniform(0, maxlagtime))
    browser.find_element_by_css_selector(
        'tr.bpk-calendar-grid__week:nth-child(' + str(week) + ') > td:nth-child(' + str(
            weekday) + ') > button:nth-child(1) > span:nth-child(1)').click()
    time.sleep(random.uniform(0, maxlagtime))


#enter passanger number
def passangernumber(paxadult,paxchild,*childage) :
    browser.find_element_by_css_selector(
        '.CabinClassTravellersSelector_CabinClassTravellersSelector__triggertext__3-XXD').click()
    time.sleep(random.uniform(0, maxlagtime))

    if paxadult == 1 :
        pass
    else :
        for i in range(paxadult-1):
            browser.find_element_by_css_selector(
                'div.CabinClassTravellersSelector_CabinClassTravellersSelector__nudger-wrapper__2hRiQ:nth-child(4) > div:nth-child(1) > button:nth-child(3) > span:nth-child(1) > svg:nth-child(1)').click()
            time.sleep(random.uniform(0, maxlagtime))

    for j in range(paxchild):
        browser.find_element_by_css_selector(
            'div.CabinClassTravellersSelector_CabinClassTravellersSelector__nudger-wrapper__2hRiQ:nth-child(6) > div:nth-child(1) > button:nth-child(3) > span:nth-child(1) > svg:nth-child(1)').click()
        time.sleep(random.uniform(0, maxlagtime))

    i = 0
    for list in childage:
        browser.find_element_by_css_selector('#children-age-dropdown-' + str(i)).click()
        time.sleep(random.uniform(0, maxlagtime))
        browser.find_element_by_css_selector(
            '#children-age-dropdown-' + str(i) + ' > option:nth-child(' + str(list + 2) + ')').click()
        time.sleep(random.uniform(0, maxlagtime))
        i += 1

    browser.find_element_by_css_selector('button.BpkLink_bpk-link__2e_PE').click()
    time.sleep(random.uniform(0, maxlagtime))


def scrapeflightdata():
    flightscraper = {}
    id = 1

    a = 7

    for i in range(a):
        flightdata = {
            'depart_date': '',
            'depart_departure': '',
            'depart_departure_airport': '',
            'depart_arrival': '',
            'depart_arrival_airport': '',
            'depart_layover': '',
            'depart_duration': '',
            # 'depart_airlines' : '',
            'return_date': '',
            'return_departure': '',
            'return_departure_airport': '',
            'return_arrival': '',
            'return_arrival_airport': '',
            'return_layover': '',
            'return_duration': '',
            # 'return_airlines' : '',
            'price-per-pax': '',
            'total-price': ''
        }

        try:
            flightdata['depart_date'] = dt.date(departyear, departmonth, departdate)

            depart_departure = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[2]/div[2]/div[1]/span[1]')
            flightdata['depart_departure'] = depart_departure.text

            depart_departure_airport = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[2]/div[2]/div[1]/span[2]/span'
            )
            flightdata['depart_departure_airport'] = depart_departure_airport.text

            depart_arrival = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[2]/div[2]/div[3]/span[1]')
            flightdata['depart_arrival'] = depart_arrival.text

            depart_arrival_airport = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[2]/div[2]/div[3]/span[2]/span'
            )
            flightdata['depart_arrival_airport'] = depart_arrival_airport.text

            depart_layover = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[2]/div[2]/div[2]/div'
            )
            flightdata['depart_layover'] = depart_layover.text

            depart_duration = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[2]/div[2]/div[2]/span'
            )
            flightdata['depart_duration'] = depart_duration.text

            flightdata['return_date'] = dt.date(returnyear, returnmonth, returndate)

            return_departure = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[3]/div[2]/div[1]/span[1]'
            )
            flightdata['return_departure'] = return_departure.text

            return_departure_airport = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[3]/div[2]/div[1]/span[2]/span'
            )
            flightdata['return_departure_airport'] = return_departure_airport.text

            return_arrival = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[3]/div[2]/div[3]/span[1]'
            )
            flightdata['return_arrival'] = return_arrival.text

            return_arrival_airport = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[3]/div[2]/div[3]/span[2]/span'
            )
            flightdata['return_arrival_airport'] = return_arrival_airport.text

            return_layover = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[3]/div[2]/div[2]/div'
            )
            flightdata['return_layover'] = return_layover.text

            return_duration = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[1]/div/div/div[3]/div[2]/div[2]/span'
            )
            flightdata['return_duration'] = return_duration.text

            price_per_pax = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[3]/div/div[2]/div/div/a'
            )
            flightdata['price-per-pax'] = price_per_pax.text

            total_price = browser.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/div[4]/section[3]/div/div[3]/div[4]/div/ul/li[' + str(
                    i + 1) + ']/div/div/article/div/div[3]/div/div[2]/div/a'
            )
            flightdata['total-price'] = total_price.text

            flightscraper[id] = flightdata
            id += 1

        except:
            continue

    #writer = pd.ExcelWriter('flightscraper.xlsx')

    df = pd.DataFrame(flightscraper).T

    columsnindex = ['depart_date',
                    'depart_departure',
                    'depart_departure_airport',
                    'depart_arrival',
                    'depart_arrival_airport',
                    'depart_layover',
                    'depart_duration',
                    'return_date',
                    'return_departure',
                    'return_departure_airport',
                    'return_arrival',
                    'return_arrival_airport',
                    'return_layover',
                    'return_duration',
                    'price-per-pax',
                    'total-price']
    df = df.reindex(columns=columsnindex)

    return df


while duration != maxduration:
    departdate = 1
    returndate = departdate + duration
    while returndate != maxreturndate:
        returndate = departdate + duration
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        time.sleep(random.uniform(0,maxlagtime))
        browser = webdriver.Firefox(profile)
        browser.get('https://www.skyscanner.net')
        try:
            choose_destination(origin, destination)
            startdate(departyear, departmonth, departdate)
            enddate(returnyear, returnmonth, returndate)
            passangernumber(2, 1, 1)

            findflight = browser.find_element_by_css_selector('.BpkButton_bpk-button__12Eue')
            findflight.click()

            time.sleep(random.uniform(17, 22))
            df = scrapeflightdata()
            db = db.append(df, ignore_index=True)
            print(df)
            print(db)

            browser.delete_all_cookies()
            browser.quit()
            time.sleep(random.uniform(2, maxlagtime + 2))

            departdate += 1

        except NoSuchElementException:
            browser.delete_all_cookies()
            browser.quit()
            time.sleep(random.uniform(2, maxlagtime + 2))
            writer = pd.ExcelWriter('flightscraper.xlsx')
            db.to_excel(writer, sheet_name='bisadong')
            print(db)
            writer.save()
            departdate += 1
            continue
    duration+=1



writer = pd.ExcelWriter('flightscraper.xlsx')
db.to_excel(writer, sheet_name='bisadong')
print (db)
writer.save()


