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

import json
from plugins.connection.Api import Api
from plugins.trade.General import General
from plugins.trade.Live import Live
from plugins.trade.Turbo import Turbo


class PyWhale(Api,General,Live,Turbo):
	"""Whaleclub.co cryptocurrency Exchange API Pyhon Client"""

	def __init__(self, start_url = 'https://api.whaleclub.co/v1/'):
		Api.__init__(self) # inherit token from API class for our connection class instance
		General.__init__(self) # inherit token from API class for our connection class instance
		Live.__init__(self) # inherit token from API class for our connection class instance
		Turbo.__init__(self) # inherit token from API class for our connection class instance

		self.start_url = start_url
		self.default_key = 'BTC_demo_key' #set the key that will be used when no value is given in key parameter
		self.verbose = True # set to True if you get output twice
	
	def _checkResp(self, resp):
		"""Check whenever an response return an error"""
		parsed = json.loads(resp.text)
		
		# every thing is ok
		if resp.status_code == 200 or resp.status_code == 201:
			if self.verbose:
				print (json.dumps(parsed, indent=4, sort_keys=True))
			return parsed
		
		# we have an error
		else:
			
			print ('\nOOps, somethings went Wrong!\n')
			
			try:
				print (parsed['error']['name'])
				print (parsed['error']['message'])
			except:
				print (parsed)

	def _testSymbols(self,symb):
		if symb != '' and len(symb.split(',')) > 5:
			print ('Error, You can only request information for up to 5 elements at once. Lower your input number and retry\n')
			return False
		else:
			return True

	def _updateKey(self,key):	
		
		if key is None:
			key = self.default_key
		
		#test if key parameter value is an accepted input
		l = ['BTC_real_key', 'BTC_demo_key', 'DASH_real_key','DASH_demo_key']
		if key in l:
			i = l.index(key)
			k = [self.BTC_real_key, self.BTC_demo_key, self.DASH_real_key, self.DASH_demo_key]
			key = k[i]	
		else:
			print ("\nError, enter an acctepted value for key parameter, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key' \n")
			return (False,key)
		
		return (True,key)

	
		
pw = PyWhale()


