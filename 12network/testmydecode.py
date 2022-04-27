
urllist=['https%3A%2F%2Fdrive.google.com%2Fuc%3Fexport%3Ddownload%26id%3D1WyFexiGemIYMmFu5I4_YEo1PitVYudqP']

def myunescape_decode(urllist):
    map=[('%3A',':'),('%2F','/'),('%3F','?'),('%3D','='),('%26','&'),('amp;','')]

    for i in range(len(urllist)):
        url=urllist[i]
        for item in map:
            (a,b)=item
            url=url.replace(a,b)
        urllist[i]=url



myunescape_decode(urllist)

print(urllist)
