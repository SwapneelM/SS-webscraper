for div in soup.find_all('div'):    
    if div['class'][0] == 'postcard-left':
        for x in div.contents:
            print "\n\n", x
            if x['class']:
                if x['class'][0] == 'postcard-text':
                    for p in x.contents:
                        print "\n", p.contents

                    if p.a.string:
                        if 'Hindi' in p.a.string:
                            print p.a['href']


for div in soup.find_all('div'):
    if div['class'][0]=='postcard-text':
        for p in div.find_all('p'):
            if "Team" in p.text:
                if "DRI" in p.text:
                    start_index = p.text.find(':')
                    dri = p.text[(start_index+1):].split(',')
                    print dri
                else:
                    end_index = p.text.find(' and ')
                    start_index = p.text.find(':')
                    team = p.text[(start_index+1):end_index].split(',')
                    print team