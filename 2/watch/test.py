import sys
import urllib, os
with open("archive.txt", "r") as mylist:
 with open("temp.txt", "r") as temp:
  for line in mylist:
   vidid = line.strip()
#   print(vidid)
#   with open('temp.txt', 'w') as f:
   os.system("grep -h '" + vidid + "' emb.txt | head -1 > temp.txt") 
   for temp in open('temp.txt'):
    url = temp.strip()
    replace = url.split('/')[4]
    vidid = vidid.replace("[","")
    vidid = vidid.replace("]","")
   os.system("sed -i 's,1AMJ8mJ1BrheeQq," + replace + ",g' -- " + vidid + "/index.html")

#  with open('temp.txt', 'w') as f:
#   sys.stdout = f
