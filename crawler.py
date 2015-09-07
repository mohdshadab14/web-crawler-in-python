import urllib2

seed_page='https://www.bbc.com'

def get_source(url):
	try:
		page=urllib2.urlopen(url)
		page_src=page.read()
		return page_src

	except:
		return ""


def get_link(page):
	start_link=page.find('<a href=')
	
	if start_link==-1:
		return None,0
	else:
		start_quote=page.find('"',start_link)
		end_quote=page.find('"',start_quote+1)
		end=page.find('.com',start_quote,end_quote)
		if end!=-1:
#			print 'hello'
			url=page[start_quote+1:end+4]
			#print url
			return url,end_quote
		else:
			return None,end_quote


def union(p,q):
	for e in q:
		if e not in p:
			p.append(e)

	


def get_all_links(page):
	links=[]
	while True:
		url,end_pos=get_link(page)
		if url:
			links.append(url)
			page=page[end_pos:]
		elif not url and end_pos!=0:
			page=page[end_pos:]
		else:
			break
	return links


def web_crawl(seed_page):
	tocrawl=[seed_page]
	crawled=[]
	notlink=[]
	while tocrawl:
		page=tocrawl.pop()
		if page not in crawled and page not in notlink:
			if page.find('.com')==-1:
				notlink.append(page)
			else:
				links=get_all_links(get_source(page))
				union(tocrawl,links)
				crawled.append(page)
				print page


#	print len(crawled)
#	for e in crawled:
#		print e
	
web_crawl(seed_page)

