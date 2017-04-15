import csv
import pymongo
from pymongo import MongoClient

#!/usr/bin/python2
from py2neo import authenticate,Graph,Node,Relationship
authenticate("localhost:7474", "neo4j", "cs315")
graph = Graph("http://localhost:7474/db/data/")

#mongo
conn = MongoClient('localhost',27017)
db = conn.test
song_lyrics = db.song_lyrics.find()


#Open the file back and read the contents
f=open("final_words.txt", "r")
fl =f.readlines()
f= open("zenith.py","w+")
f=open("zenith.py","a+")

f.write('# -*- coding: utf-8 -*-'+'\n')
f.write('from py2neo import authenticate,Graph,Node,Relationship'+'\n')
f.write('authenticate("localhost:7474", "neo4j", "cs315")'+'\n')
f.write('graph = Graph("http://localhost:7474/db/data/")'+'\n')


for x in fl:
 f.write("Node_"+x.rstrip('\n').encode("ascii", "ignore")+" = Node('Word',Name='"+x.rstrip('\n')+"')"+'\n')
 f.write("graph.create(Node_"+x.rstrip('\n').encode("ascii", "ignore")+")\n")

# det = open("data.txt",'r')
# songs = det.readlines()
# song_detail={}
# song_counter = 0
# with open("data.txt", "rb") as fi:
# 	reader = csv.reader(fi, delimiter=",")
# 	for line in reader:
# 		t = songs[song_counter].split(',')
# 		song_detail["song_name"] = t[0]
# 		song_detail["album_name"] =t[1]
# 		song_detail["artist_name"] = t[2]
# 		song_detail["genre"] = t[3][:-1]
# 		f.write("Song_"+str(song_counter)+" = Node('Track',Name='"+song_detail["song_name"]+"',AlbumName='"+song_detail["album_name"]+"',ArtistName='"+song_detail["artist_name"]+"',Genre='"+song_detail["genre"]+"')"+'\n')
# 		f.write("graph.create(Song_"+str(song_counter)+")\n")
# 		song_counter +=1


song_count = 0
for song in song_lyrics:
	if song_count>500:
		break
	f.write("Song"+" = Node('Track',Name='"+song["song_name"]+"',AlbumName='"+song["album_name"]+"',ArtistName='"+song["artist_name"]+"',Genre='"+song["genre"]+"')"+'\n')
	f.write("graph.create(Song"+")\n")
	word_count = 0
	for word in song["words"]:
		f.write("Rel_"+str(word_count)+" = Relationship("+"Song"+ ", 'Key'," + "Node_"+str(word.items()[0][0])+")"+'\n')
		f.write("graph.create(Rel"+"_"+str(word_count)+")\n")
		word_count+=1
	song_count+=1

f.close()   