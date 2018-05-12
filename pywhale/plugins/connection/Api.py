# Author: Logan Schwartz
# This file is part of pywhale.
# pywhale is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pywhale is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser
# General Public LICENSE along with krakenex. If not, see
# <http://www.gnu.org/licenses/gpl-3.0.txt>.

import os, sys

class Api (object):
	"""	Whaleclub.co cryptocurrency Exchange API Pyhon Client Connection Handler methods:"""
	
	def __init__(self, BTC_real_key='', BTC_demo_key='', DASH_real_key='', DASH_demo_key='', ETH_real_key='', LTC_real_key=''):
		"""Create an object with authentication information.
		API Token could be find from your API Settings panel which is available from the top right menu in your trading dashboard.

		Args:
		DASH_demo_key -- DASH API Token for demo mode
		DASH_real_key -- DASH API Token for real mode
		BTC_demo_key  -- BTC API Token for demo mode
		BTC_real_key  -- BTC API Token for real mode
		ETH_real_key  -- ETH API Token for real mode
		LTC_real_key  -- LTC API Token for real mode


		"""
		self.BTC_demo_key = BTC_demo_key
		self.BTC_real_key = BTC_real_key
		self.DASH_demo_key = DASH_demo_key
		self.DASH_real_key = DASH_real_key
		self.ETH_real_key = ETH_real_key
		self.LTC_real_key = LTC_real_key
		self.root_path = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-2])

		self.load_tokens()

	def load_tokens(self):
		"""Load API token from files
		BTC_demo_key.txt,BTC_real_key.txt,DASH_demo_key.txt,DASH_real_key.txt, ETH_real_key.txt, LTC_real_key.txt
		"""

		keys = []

		files = ["BTC_demo_key.txt",
		"BTC_real_key.txt",
		"DASH_demo_key.txt",
		"DASH_real_key.txt",
		"ETH_real_key.txt",
		"LTC_real_key.txt",
		]

		#open files and save token
		for file in files:
			filepath = '/'.join([self.root_path, 'api_keys', file])
			f = open(filepath,'r')
			for lines in file:
				key = f.readline().rstrip('\n')
				self.validate_key(file, key)
				keys.append(key)
				break	#only read 1st line

		#update token with token loaded
		self.BTC_demo_key,self.BTC_real_key,self.DASH_demo_key,self.DASH_real_key,self.ETH_real_key,self.LTC_real_key = keys
		welcome_message = '\n'+'#'*49+'\n'+'#'*6+'          Welcome to PyWhale         '+'#'*6+'\n'+'#'*6+'   Python wrapper for whaleclub.co   '+'#'*6+'\n'+'#'*49+'\n\n'
		message = """API token loaded, ready to trade!\ntype PyWhale.help() at anytime to see available functions"""
		print (welcome_message + message)

	def validate_key(self, file, key):
		"""Validate that the key exists and is complet"""

		#check if token exist and are complet, token length is 36 char long
		if len(key) == 36:
			return
		
		error_message = '''\nError, API token for {} is either missing or incomplet (length < 36 characters)\nCheck that you've correctly enter your API token in {}/api_keys/{}'''.format(file, self.root_path, file)
		sys.exit(error_message)

