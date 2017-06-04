import re, os, sys
from bs4 import BeautifulSoup


data = """

"""
soup = BeautifulSoup(data, 'html.parser')

# required final dataset
data_scraped = []

talk_count = 0

# find all the divisions overall

for div in soup.find_all('div'):	
	# reset all talk data	
	print "\nNew Talk\n"
	talk_data = {}
	lang_count = 0
	pdf_link_count = 0
	# verify parent div class for project
	if div['class'][0] == 'postcard-left':
		# extract the image link from each division
		for img in div.find_all('img'):
			talk_data['image'] = img['src']

	if div['class'][0] == 'postcard-text':
		print "\nFound Talk\n"
		if div.h3:
			start_index = div.h3.text.find(':')
			if start_index==(-1):
				title = ''
			else:
				title = div.h3.text[start_index:]
			talk_data['name'] = title
		# find the sub-divisions with data within each research talk
		talk_data['pdf'] = div.h3.a['href']
		
		for p in div.find_all('p'):

			if "Published" in p.text:
				start_index = p.text.find('on')
				end_index = p.text.find('-')
				if (start_index==(-1) or end_index==(-1)):
					published_on = '' 
				else:
					published_on = p.text[(start_index+2):(end_index-1)]
				talk_data['description'] = p.text
				for a in p.find_all('a'):
					if pdf_link_count == 0:
						talk_data['pdf_links'] = []
					pdf_links = {}
					pdf_links['name'] = a.text.replace('link', '')
					pdf_links['url'] = a['href']
					talk_data['pdf_links'].append(pdf_links)
					pdf_link_count += 1

			elif "info" in p.text or "Info" in p.text:
				start_index = p.text.find(':')
				if start_index == (-1):
					description = ''
				else:
					description = p.text
				talk_data['description'] = description

			elif "Audio" in p.text:
				start_index = p.text.find(':')
				if start_index==(-1):
					audio = ''
				else:
					audio = p.text[start_index:].split(',')
				talk_data['audio'] = audio

			elif "Team" in p.text:
				if "DRI" in p.text:
					start_index = p.text.find(':')
					if start_index==(-1):
						dri = []
					else:	
						dri = p.text[(start_index+1):].split(',')
					talk_data['dri'] = dri
				else:
					end_index = p.text.find(' and ')
					start_index = p.text.find(':')
					if (start_index==(-1) or end_index==(-1)):
						team = []
					else:
						team = p.text[(start_index+1):end_index].split(',')
					talk_data['scripting'] = team
			
			elif p.iframe:
				talk_data['video'] = p.iframe['src']

			else:
				languages = ['Hindi', 'Nepali', 'Tamil', 'Marathi', 'Spanish', 'Catalan', 'English', 'Malayalam', 'Chinese', 'Japanese']
				if lang_count == 0:
					talk_data['video_links'] = []
				for lang in languages:
					if lang in p.text:
						language = {}
						language['name'] = lang
						language_url = p.a['href']
						talk_data['video_links'].append(language)
						lang_count += 1
		# increment the talk count by one each time you complete the iteration
		print "\nTalk Data Extracted for talk ", talk_count
		print "\n", div
		talk_count += 1
		data_scraped.append(talk_data)

print data_scraped
