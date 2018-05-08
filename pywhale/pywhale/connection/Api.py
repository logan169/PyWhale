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

import sys

class Api (object):
	"""	Whaleclub.co cryptocurrency Exchange API Pyhon Client Connection Handler methods:"""
	
	def __init__(self, BTC_real_key='', BTC_demo_key='', DASH_real_key='', DASH_demo_key=''):
		"""Create an object with authentication information.
		API Token could be find from your API Settings panel which is available from the top right menu in your trading dashboard.

		Args:
			DASH_demo_key -- DASH API Token for demo mode
			DASH_real_key -- DASH API Token for real mode
			BTC_demo_key  -- BTC API Token for demo mode
			BTC_real_key  -- BTC API Token for real mode


		"""
		self.BTC_demo_key = BTC_demo_key
		self.BTC_real_key = BTC_real_key
		self.DASH_demo_key = DASH_demo_key
		self.DASH_real_key = DASH_real_key
		self.load_tokens()

	def load_tokens(self):
		"""Load API token from files
		BTC_demo_key.txt,BTC_real_key.txt,DASH_demo_key.txt,DASH_real_key.txt
		"""
		files = ["BTC_demo_key.txt","BTC_real_key.txt","DASH_demo_key.txt","DASH_real_key.txt"]
		keys = []

		#open files and save token
		for file in files:
			f = open(file,'r')
			for lines in file:
				key = f.readline().rstrip('\n')
				keys.append(key)
				break	#only read 1st line

		#check if token exist
		for key in keys:
			if len(key) == 0:
				error_message = '''Error, at least one API token is missing\nCheck that you've correctly enter your API token in following files and try again:\nBTC_demo_key.txt,BTC_real_key.txt,DASH_demo_key.txt,DASH_real_key.txt'''
				print (error_message)
				sys.exit(1)
			
		#update token with token loaded
		self.BTC_demo_key,self.BTC_real_key,self.DASH_demo_key,self.DASH_real_key = keys
		welcome_message = '\n'+'#'*49+'\n'+'#'*6+'          Welcome to PyWhale         '+'#'*6+'\n'+'#'*6+'   Python wrapper for whaleclub.co   '+'#'*6+'\n'+'#'*49+'\n\n'
		message = """API token loaded, ready to trade!\ntype PyWhale.help() at anytime to see available functions"""
		print (welcome_message + message)
