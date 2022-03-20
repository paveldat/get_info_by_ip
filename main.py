import requests
from pyfiglet import Figlet

import socket

def get_info_by_ip(ip='127.0.0.1'):
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
		
		data = {
			'[IP]' : response.get('query'),
			'[Country]' : response.get('country'),
			'[City]' : response.get('city'),
			'[Organization]' : response.get('org'),
			'[Region name]' : response.get('regionName'),
			'[Lat]' : response.get('lat'),
			'[Lon]' : response.get('lon')
		}

		for k, v in data.items():
			print(f'{k} : {v}')

	except requests.exceptions.ConnectionError:
		return 'Check your connection'

def get_ip_by_hostname(hostname='google.com'):
	try:
		print(f'Hostname: {hostname}')
		get_info_by_ip(ip=socket.gethostbyname(hostname))

	except socket.gaierror as error:
		return f'Invalid Hostname. Error: {error}'


def main():
	preview = Figlet(font='slant')
	print(preview.renderText('Made by Pavel Dat'))
	resp = input('Enter IP or URL: ')
	
	if len(resp) == 0:
		print("The input is empty. Try again")
		main()
	elif resp.count('.') == 3:
		get_info_by_ip(ip=resp)
	else:
		get_ip_by_hostname(hostname=resp)

if __name__ == '__main__':
	main()