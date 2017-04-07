# -*- coding: utf-8 -*-
import requests
import json
import csv
import urllib2
import time


det = open('details.txt','a')
with open('ids1.txt') as f:
    for line in f:
    	r = json.load(urllib2.urlopen('http://api.musixmatch.com/ws/1.1/track.get?apikey=8705f37294dc36feeaed2cf7c53ba663&track_id='+line))
        # print r['message']['body']
        if not r['message']['body']: 
        	det.write('No info,No info,No info,No info\n')
        else:
        	det.write(r['message']['body']['track']['track_name'].encode('utf-8'))
        	det.write(',')
        	det.write(r['message']['body']['track']['album_name'].encode('utf-8'))
        	det.write(',')
        	det.write(r['message']['body']['track']['artist_name'].encode('utf-8'))
        	det.write(',')
        	if len(r['message']['body']['track']['primary_genres']['music_genre_list']) != 0 :
        		det.write(r['message']['body']['track']['primary_genres']['music_genre_list'][0]['music_genre']['music_genre_name'].encode('utf-8'))
        	else :
        		det.write('No info')
        	det.write('\n')

det.close()