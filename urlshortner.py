import pyshorteners
link=input("enter the link to be shortened: ")
shortener=pyshorteners.Shortener()
x=shortener.tinyurl.short(link)
print("shorten link: "+x)