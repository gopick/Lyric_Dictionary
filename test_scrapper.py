import urllib2
#Ideally this should give the info, but it doesn't work
#So, I copied the source code(only the required links) 
#and put it in u.html in the working directory
#response = urllib2.urlopen('http://www.azlyrics.com/u.html')
#html = response.read()

from bs4 import BeautifulSoup
#soup = BeautifulSoup(html, 'html.parser')
with open("u.html") as html_data:
	soup = BeautifulSoup(html_data, 'html.parser')

#Get all the artists whose name starts with u
f = open('ulinks.txt', 'w+')
for link in soup.find_all('a'):
    f.write(link.get('href'))
    f.write('\n')
f.close()

f = open('ulinks.txt','r')
links = []
links = f.read().splitlines()

#now parse each artist using urllib2 
#Somehow this is returning nice html for parsing

#MAKE A GLOBAL FILE FOR SINGLE OBJECT
#f = open('ulyrics.txt','w+')
#use this to keep all the lyrics of artists in U
for link in links:
	response = urllib2.urlopen('http://www.azlyrics.com/' + link)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	song_links=soup.find_all('a',{"id":""},class_="")
	link = link.split("/")[1].split(".")[0]
	f = open(link+'.txt','w+')
	#parse each song of the particular artist
	for song_link in song_links:
		temp_link = song_link.get('href')
		if temp_link[0:2] == '..':
			song_url = 'http://www.azlyrics.com' + temp_link[2:]
			lyric_response = urllib2.urlopen(song_url)
			lyric_html = lyric_response.read()
			lyric_soup = BeautifulSoup(lyric_html, 'html.parser')
			lyrics=lyric_soup.find_all('div',{"id":""},class_="")
			f.write(lyrics[0].get_text())
			f.write('\n')
			f.write('=======================')
	f.close()
