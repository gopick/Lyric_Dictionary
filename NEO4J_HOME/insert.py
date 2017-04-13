#insert data
import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost',27017)

db = conn.test

song_db = db.song_lyrics

# -*- coding: utf-8 -*-

count = 0
words = {}
with open('words.txt') as f:
	for line in f:
		if(line[0] != '#'):
				words[str(count)] = line[:-1]
		count += 1

import csv

temp_file = open('temp.txt', 'a')

det = open("data.txt",'r')
songs = det.readlines()
song_detail={}
song_counter = 0
with open("songs.csv", "rb") as f:
	reader = csv.reader(f, delimiter=",")
	for line in reader:
		t = songs[song_counter].split(',')
		song_detail["song_name"] = t[0]
		song_detail["album_name"] =t[1]
		song_detail["artist_name"] = t[2]
		song_detail["genre"] = t[3][:-1]
		song_detail["words"] = []
		for item in line[2:]:
			temp = item.split(':')
			if temp[0] in words:
				temp_dict = {}
				temp_dict[words[temp[0]]] = temp[1]
				song_detail["words"].append(temp_dict)
		song_db.insert(str(song_detail))
		temp_file.write(str(song_detail))
		temp_file.write('\n')
		song_counter +=1

det.close()
temp_file.close()