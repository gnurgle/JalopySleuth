import copy
import requests
import sqlite3 as sql
from bs4 import BeautifulSoup

#Run for year range
def RunForYears(st,ed):

	#Define passed variables
	start_year = st
	end_year = ed

	for year in range(start_year,end_year):
		getMakeByYear(year)
	
#Get make by year passed
def getMakeByYear(year):

	#define base URL
	baseUrl = "https://autodetective.com/directory/"
	yearUrl = baseUrl + str(year)

	#fetch page
	page = requests.get(yearUrl)

	#decode with Beautiful Soup
	soup = BeautifulSoup(page.content, 'html.parser')

	#fetch span class 'name' for Make names
	results = soup.find_all('span', class_='name')

	#Print list of names
	for result in results:
		make = (str(result)[24:-7])
		#For passing url replace " " with -
		make = make.replace(" ", "-")
		#Call function to pull Models for Make
		getModelByMakeAndYear(make,year,yearUrl)

#Get Model by Make and Year
def getModelByMakeAndYear(mke,yer,yearU):

	#Define passed variables
	make = mke
	year = yer
	yearUrl = yearU

	#Make new url for scrapping
	makeUrl = yearU + "/" + make

	#fetch page
	page = requests.get(makeUrl)

	#decode with Beautiful Soup
	soup = BeautifulSoup(page.content, 'html.parser')

	#fetch h3 class 'title' for all Models
	results = soup.find_all('h3', class_='title')

	#Print list of Models
	for result in results:
		model = (str(result)[19+len(make):-5])
		print(model)
		#For passing url replace "/" with ""
		tempModel = copy.copy(model)
		tempModel = tempModel.replace("/", "")
		#For passing replace " &amp; " with " "
		tempModel = tempModel.replace(" &amp; ", " ")
		#For passing replace " " with -
		tempModel = tempModel.replace(" ", "-")
		#For passing replace " " with -
		model = model.replace(" ", "-")
		#Set Trim Url
		trimUrl = makeUrl + "/" + tempModel
		#Call Function to pull Trims and misc info for
		getTrimByModelMakeYear(model,make,trimUrl)

#Get model specific info including trims
def getTrimByModelMakeYear(mdel,mke,trimU):

	#Define passed variables
	model = mdel
	make = mke
	trimUrl = trimU

	#fetch page
	page = requests.get(trimUrl)

	#decode with Beautiful Soup
	soup = BeautifulSoup(page.content, 'html.parser')

	#Find number of trims
	#fetch div class 'vital-stats block' for # Trims
	results = soup.find('div', class_='vital-stats block')
	#Find span class 'text' for # Trims 
	spanText = results.find_all('span', class_='text')
	#Find amount of trim in <i>
	amount = spanText[3].find_all('i')
	#Strip html tags and convert to int
	num_trim = (int(str(amount)[4:-5]))

	if num_trim > 1:
		#fetch h3 class 'title' for all Trims
		results = soup.find_all('h3', class_='title')

		#Print list of Trims
		for result in results:
			trim = (str(result)[25+len(make)+len(model):-5])
			print (trim)
			#For error of double spaces in certain cases
			trim = trim.replace("  "," ")
			#For passing replace " &amp; " with " "
			trim = trim.replace(" &amp; ", " ")
			#For passing replace " " with -
			trim = trim.replace(" ", "-")
			#For passing url replace "/" with ""
			trim = trim.replace("/", "")
			#Set info URL
			infoUrl = trimUrl + "/trim/" + trim

			#Call Function to pull Info for specific vehicle (finally)
			getInfo(infoUrl)
	else:
		getInfo(trimUrl)


#Get trim specific info to save to DB
def getInfo(infoU):

	#Define passed variables
	infoUrl = infoU

	#fetch page
	page = requests.get(infoUrl)

	#decode with Beautiful Soup
	soup = BeautifulSoup(page.content, 'html.parser')

	#fetch div class 'table fixed block' for all info
	results = soup.find('div', class_='table fixed block')

	#fetch values for info and temp save to array
	#lambda function matched just td, not td_title
	infos = results.find_all(lambda tag: tag.name == 'div' and tag.get('class') ==['td'])

	outp = []

	#print list and strip extra details
	for value in infos:
		outp.append(str(value)[16:-6])
	#Save to DB
	conn = sql.connect('car_base.db')
	cur = conn.cursor()
	cur.execute("INSERT OR IGNORE INTO Base VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
	(outp))

	conn.commit()
	conn.close()


if __name__ == '__main__':
	#1981-current
	RunForYears(1981,2021)
