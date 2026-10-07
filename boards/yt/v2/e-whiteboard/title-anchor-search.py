"""YouTube search scrape used 2026-10-07 to anchor the doc 10 titles (views as of that day).
    python3 title-anchor-search.py "how to talk to camera"
"""
import sys,re,json,urllib.request,urllib.parse
q=sys.argv[1]
req=urllib.request.Request("https://www.youtube.com/results?search_query="+urllib.parse.quote(q),headers={"User-Agent":"Mozilla/5.0","Accept-Language":"en-US"})
s=urllib.request.urlopen(req).read().decode()
m=re.search(r'var ytInitialData = (\{.*?\});</script>',s)
d=json.loads(m.group(1))
out=[]
def walk(o):
    if isinstance(o,dict):
        if 'videoRenderer' in o:
            v=o['videoRenderer']
            t=''.join(r['text'] for r in v['title']['runs'])
            ch=v.get('ownerText',{}).get('runs',[{}])[0].get('text')
            vc=v.get('viewCountText',{}).get('simpleText','')
            out.append((v['videoId'],t,ch,vc))
        for x in o.values(): walk(x)
    elif isinstance(o,list):
        for x in o: walk(x)
walk(d)
for r in out[:15]: print(' | '.join(map(str,r)))
