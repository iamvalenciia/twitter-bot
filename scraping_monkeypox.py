

import requests
from bs4 import BeautifulSoup
import pandas as pd

"""This is a "Scraping Bot" that gets data from a "spreadsheet" 
that belongs to Global Health (a Data Science Initiative). 

My program shows the number of confirmed, suspected, and discarded cases 
of monkeypox in real-time. In addition, it shows the confirmed cases of each country"""



COUNTRIES = ['Wales','Northern Ireland','Italy','Scotland','Bolivia','United Arab Emirates','Iran','England','Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
URL = 'https://docs.google.com/spreadsheets/d/1CEBhao3rMe-qtCbAgJTn5ZKQMRFWeAeaiXFpBY3gbHE/htmlview#'


def main():

	#To get html data from the url
	html_data = html_information(URL)
	
	#to save all the [id] from each patient
	all_ids = get_cases_id(html_data)

	#to get the [status] of each patient
	all_status = get_cases_status (html_data)

	#to get the [country] of each patient
	all_countries = get_country_patient (html_data, COUNTRIES)

	# Building a {dictionary} with the [3 lists]
	# In this project I Don't use the dictionary but was very greatful
	# build this function I recomend you to see and compare with the website
	
	the_dictionary = building_dictionary (all_ids, all_status, all_countries)
	# for _ in the_dictionary:
	# 	print(_)
	
	#to get the [countries] with their [confirmed cases number] 
	cases_countries = confirmed_cases_each_country(html_data)
	
	
	#to calculate the [confirmed, suspected, discarded] cases
	number_status = calculate_the_status (all_status)

	# to build a Dataframe pandas from the data of cases_countries
	descending_Cases = dataframe_cases(cases_countries)
	# for _ in range(0,10):
	# 	print(descending_Cases.iloc[_]['Country'],'-', descending_Cases.iloc[_]['Cases'])
	
	print('----------------------------')
	print('monkeypox Cases in the World')
	print('----------------------------')

	try:  
		print(f'Confirmed cases: {number_status[0]}')
		print(f'Suspected cases: {number_status[1]}')
		print(f'discarded cases: {number_status[2]}')

	except IndexError as index_err:
		print(index_err)

	print('----------------------------------------')
	print('Countries With Confirmed monkeypox Cases')
	print('----------------------------------------')

	print(descending_Cases)

	print('-----------------------------------------------------------')
	print('This program is automated to update at the moment we run it')
	print('-----------------------------------------------------------')
			


def html_information(url):
	"""To get the html information from the website.

    Parameters
    	url: the url from the website
    Return: all html tags from the website"""

	try:
		response = requests.get(url)
		response.raise_for_status()

	except requests.exceptions.HTTPError as errh:
		print ("Http Error:",errh)
	except requests.exceptions.ConnectionError as errc:
		print("Error Connecting:",errc)
	except requests.exceptions.Timeout as errt:
		print ("Timeout Error:",errt)
	except requests.exceptions.RequestException as err:
		print ("OOps: Something Else",err)
	
	text = response.text
	html_data = BeautifulSoup(text, 'html.parser')
	
	return html_data



def get_cases_id(html_data):
	"""analyze the html data to find the id's from each monkeypox cases
	using the selector [class="s2"], and then return it in a list.

    Parameters
    	html_data: all html tags from the website
    Return: complete list with the id of all monkeypox cases in the world"""

	#to get all the tags from the selector [class="s2"]
	all_class_s2 = html_data.find_all("td",  class_="s2")

	#to save the id of each patient
	id_list = []
	
	for class_s2 in all_class_s2:
		#this loop is to analyze each element into the each value
		for elements in class_s2:
			
			#to get the elements that only have numbers 
			if elements.isdigit():
				#to save the id as a integer
				id = int(f"{elements}")
				#to save the value into the id_list
				id_list.append(id)

	#skip value if duplicate in (id_list)
	clean_list = list(set(id_list))
	
	return clean_list



def get_cases_status(html_data):
	"""analyze the html data to find the status(confirmed, suspected
	 and discarded) from each monkeypox cases using the selector 
	 [class="s0"], and then return it in a list.

    Parameters
    	html_data: all html tags from the website
    Return: complete list with the status of all monkeypox cases in the world"""

	#to get all the tags with the name class of "s0"
	all_status = html_data.find_all("td",  class_="s0")

	#to save the status of each patient
	status_patient = []

	for class_s0 in all_status:
		#to separate the tag html and get the text
		clean_text = class_s0.text

		#to get the text that have a status of each patient
		if clean_text == 'confirmed' or clean_text == 'suspected' or clean_text == 'discarded':
			status_patient.append(clean_text)

	return status_patient



def calculate_the_status(all_status):
	"""compute the list [all_status] to return the amount of
	confirmed, suspected and discarded cases.
	 
    Parameters
    	all_status: A list
    Return: A list with 3 values [confirmed_cases, suspected_cases, discarded_cases] """
	
	confirmed_cases = 0
	suspected_cases = 0
	discarded_cases = 0
	
	# [confirmed_cases, suspected_cases, discarded_cases]
	all_number_Cases = []

	for _ in all_status:
		if _ == 'confirmed':
			confirmed_cases += 1
		elif _ == 'suspected':
			suspected_cases += 1
		elif _ == 'discarded':
			discarded_cases += 1

	all_number_Cases.append(confirmed_cases)
	all_number_Cases.append(suspected_cases)
	all_number_Cases.append(discarded_cases)

	return all_number_Cases



def confirmed_cases_each_country(html_data):
	"""analyze the html data to find the countries with
	their confirmed cases using the selector 
	 ["div", id="1289291271"], and then return it in a list.
	 
    Parameters
    	html_data: all html tags from the website
    Return: A dictironary"""

	#to get all the tags with the slector id"
	global_tags = html_data.find_all("div", id="1289291271")
	
	#to save the coutries with their amount of cofirmed cases
	list_return = []
	
	for each_tag in global_tags:
		# the next line of code let us to localizate and navigate inside of each <tr> tag 
		tr_tags = each_tag.find_all("tr")

		for each_row in tr_tags:

			#to scan the tags of the first two "td" tags
			td_tags = each_row.find_all("td")[:2]
			
			
			value_country = ''
			value_cases = 0

			for country_and_amount in td_tags:
				clean_text = country_and_amount.text
				
				#	There are some countries with 0 confirmed cases wich means a empty place
				#	this countries have some suspected or discarted cases, and thats the reason
				#	the countries are here. 
		
				# We use the next if statement to replace the empty place with thier value "0"
				if clean_text == '':
					clean_text = '0'
				
				# This is to separate and save it in their respective variables 
				if clean_text.isdigit():
					value_cases = int(clean_text)
				else:
					value_country = clean_text

			value = value_country , value_cases
			list_return.append(value)

	#this is to delete the first two items from the list wich was the Headlines
	del list_return[0:2]
	getout_grand_total = list_return.pop()

	return list_return



def dataframe_cases(cases_countries):
	"""To build a Dataframe with two colums from two lists and sort
	by the amount of confirmed cases of each country.
	 
    Parameters
    	cases_countries: A list
    Return: DataFrame with module Pandas"""

	#to build a dataframe with 2 columns
	df = pd.DataFrame(cases_countries, columns=['Country','Cases',])

	# to sort the list by the amount of confirmed cases
	sort_Cases = df.sort_values(["Cases"], ascending=False)

	return sort_Cases




# ---------------------------------------------------------------/
# This two functions is only to build a dictionary with the data /
# ---------------------------------------------------------------/

def get_country_patient(html_data, countries_world):
	"""analyze the html data to find the country from each 
	monkeypox cases using the selector [class="s0"], and then
	return it in a list.
	 
    Parameters
    	html_data: all html tags from the website
    Return: complete list with the countries of all monkeypox cases in the world"""

	#to get all the tags with the name class of "s0"
	global_tags = html_data.find_all("div", id="0")

	#to save the country of each patient
	patient_countries = []

	for each_tag in global_tags:
		tr_tags = each_tag.find_all("tr")

		for each_row in tr_tags:
			# this line of code is to scan the 5 tags at the beginning
			td_tags = each_row.find_all("td")[:5]

			for each_td in td_tags:

				clean_text = each_td.text
				# This "if statement" is to verify that the text is a country 
				if clean_text in countries_world:
					patient_countries.append(clean_text)

	return patient_countries



def building_dictionary(ids, status, countries):
	"""Use [3 lists] to return a dictionary with
	all the information that we got from the website.
	 
    Parameters
		ids: A list
		status: A list
		countries: A list
    Return: A dictironary"""

	general_list = []

	for x, y, z in zip(ids, status, countries):
		dictionary_id = {}
		dictionary_id['ID'] = x
		dictionary_id['Status'] = y
		dictionary_id['Country'] = z

		general_list.append(dictionary_id)
	return general_list



if __name__=="__main__":
    main()







