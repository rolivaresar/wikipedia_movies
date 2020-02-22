from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from random import seed
from random import randint
import pandas as pd
import re 
import shutil
import os
from  builtins import any as b_any
from os import listdir
from os.path import isfile, join



def get_movie(titulo):
    
    ''' Given a movie title goes to its wikipedia page
        and get the information from the table in the right '''
    
    timmer = randint(10,20)
    print('Inicia timer de...{} segundos'.format(timmer))
    time.sleep(timmer)
    
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    driver = webdriver.Chrome()
    driver.get(url)
    
    time.sleep(10)
    
    u = driver.find_element_by_name('search')
    
    time.sleep(2)
    
    u.send_keys(titulo)
    
    time.sleep(5)

    suggestions = driver.find_elements_by_css_selector("div[class='suggestions-results']")

    movies = []
    for element in suggestions:
        movies.append(str(element.text))

    movies_list = movies[0].split("\n")

    for i in movies_list:
        if (i.find("film") != -1):
            break
            
    i = i.replace(" (soundtrack)","")
    driver.find_element_by_xpath('//*[@title="{}"]'.format(i)).click()

    time.sleep(10)
    
    table = driver.find_element_by_xpath(("//table[@class='infobox vevent']"))
    data = table.text
    
    return data


def write_movie(table,movie_name,path):
    
    ''' Given a movie and its information 
        writes a .txt file '''
    
    movie_name = clean_movie_name(movie_name)
    #Escribir txt
    file_path = path+movie_name
    file = open("{}.txt".format(file_path),"w") 
    file.write(data)
    file.close() 

def clean_movie_name(movie_name):
    
    ''' Given a movie title, removes special characters '''
    
    movie_name = movie_name.replace(" ","")
    movie_name = movie_name.replace("’","")
    movie_name = movie_name.replace("…","")
    movie_name = movie_name.replace(".","")
    return movie_name


def check_movie(movie_name,movie_list):
    movie_name = clean_movie_name(movie_name)
    movie_name = movie_name + ".txt"
    
    if (movie_name not in movie_list):
        return True
    else:
        return False

top2019 = ['The Dead Don’t Die',
          'Ad Astra',
          'Cindy la Regia',
          'Ford v Ferrari',
          'Once Upon a Time in…Hollywood',
          'Parasite',
          'Little Women',
          'The Irishman',
          'Marriage Story',
          'The Lighthouse',
          'Mission: Impossible – Fallout'
          'Ready Player One']

# the path were the files are going to be saved. 
# Example: /home/ubuntu/moviefiles/
mypath = ""

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for i in top2019:
	#First check if the movie is not in the folder
    if check_movie(movie_name=i,movie_list=onlyfiles):
    	#Download the data
        data = get_movie(ia)
        #Save data as txt
        write_movie(table=data,movie_name=i,path=mypath)
    else: 
        print("Movie: ",i," already in the database")