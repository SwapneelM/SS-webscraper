for div in soup.find_all('div'):    
	if div['class'][0] == 'postcard-left':
		for x in div.contents:
			print "\n\n", x
			if x['class'][0] == 'postcard-text':
				for p in x.contents:
					print "\n", p.contents

					if p.a.string:
						if 'Hindi' in p.a.string:
							print p.a['href']