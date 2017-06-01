import re, os, sys
from bs4 import BeautifulSoup


data = """
<div class="postcard-left">
	<div class="postcard-image"><img src="assets/lagunita/images/paper/v4ai1.png" alt="" height="200" width="200"></div>
	<br><br>
	<div class="postcard-text">
		<h3><a href="https://www.cs.cmu.edu/~kkandasa/pubs/kandasamyIJCAI15activePostEst.pdf">Research Talk: Bayesian Active Learning for Posterior Estimation</a></h3>
		<p class="descriptor">Published on April 04, 2017 - <a href="https://www.cs.cmu.edu/~kkandasa/pubs/kandasamyIJCAI15activePostEst.pdf">Public link</a> - IJCAI 2016 (best paper)</p>
		<p><a target="_blank" href="https://www.youtube.com/watch?v=-dbzI20Yavs">Check out this talk in ALL Catalan</a></p>
		<p><a target="_blank" href="https://www.youtube.com/watch?v=CD1IFsPO_Jw">Check out this talk in ALL Hindi</a></p>
		<p><a target="_blank" href="https://www.youtube.com/watch?v=BG5JRs-hKfo">Check out this talk in ALL Spanish</a></p>
		<p><iframe width="500" height="300" src="https://www.youtube.com/embed/fxqBkVvkdB8" frameborder="0" allowfullscreen=""></iframe></p>
		<p>Directly Responsible Individuals (DRI) Team: Aseem Saxena, Sourav Singh</p>
		<p>Team: Aseem Saxena, Sourav Singh, Briana Berger, Ahmed Nasser, Tanveet Singh, and many others.</p>
		<p>Audio By: Briana Berger</p>
		<p>Super-DRIs: Afelio Padilla, Anshu Aviral</p>
	</div>
	</div>
"""
soup = BeautifulSoup(data, 'html.parser')

# required final dataset
data_scraped = []

talk_count = 0

# find all the divisions overall

for div in soup.find_all('div'):	
	# reset all talk data	
	talk_data = {}
	# verify parent div class for project
	if div['class'][0] == 'postcard-left':
		# extract the title


		# extract the title from each division
		#if div.div.img:
		#	talk_data['image'] = div.div.img['src']

		# find the sub-divisions with data within each research talk
		for x in div.children:
			if x['class'][0] == 'postcard-text':
				


# increment the talk count by one each time you complete the iteration
	print("Talk Data Extracted")
	talk_count += 1
	data_scraped.append(talk_data)
