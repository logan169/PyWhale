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

import requests

class Turbo (object):

	def getTurboActiveContracts (self,	key = None):
		"""
Fetch a list of currently active turbo contracts.
This endpoint will return information about currently active contracts such as the purchase deadline and expiry time.
When you submit a new turbo position, it’ll be on one of the active contracts you get from here.

arg:
----
key		string 		Optional. 	One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id 			string		Unique ID for the contract.
type			string 		Can be 1min or 5min.
created_at		integer 	When the contract first became active.
purchase_deadline	integer 	Time before which a turbo position must be submitted to be included in the contract.
expires_at		integer		When the contract expires and turbo positions settle.
		"""

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'contracts'
		h = {"Authorization":"Bearer "+key}
		r = requests.get(url,headers=h)

		if self.verbose:
			print ('\nListing available active turbo contract: \n')

		return self._checkResp(r)

	def createNewTurboPosition(self, position_direction = None, market=None, position_type=None, size=None, key = None):
		"""
Open a new turbo position.
This endpoint allows you to open a new turbo position.
All turbo positions are executed at the market price, so there is no entry price to set.

arg:
----
position_direction	string 		Required. 	Can be "long" or "short"
market 			string 		Required. 	Market where you want to create a position
position_type 		string 		Required. 	Contract type. Can be 1min or 5min
size                	integer 	Required. 	Turbo position’s size, in satoshis.
key			string 		Optional. 	One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id 		string   	Unique ID for the turbo position.
contract_id	string	 	ID of the contract this turbo position belongs to.
direction 	string 	 	Can be long or short.
market 		string 		Market this turbo position was executed on.
state 		string 		Can be active, or closed.
size 		integer 	Position’s size, in satoshis.
entry_price 	number 		Price at which the turbo position was executed.
payoff 		number 		Payoff in case of correct prediction. Multiply by size to get payoff in satoshis.
close_price 	number 		Price at which the position was closed. Appears only if the position is closed.
profit 		number 		Profit made on the trade, in satoshis. Is negative in case of loss. Appears only if the position is closed.
created_at 	integer 	When the position was created.
closed_at 	integer 	When the position was closed. Appears only if the position is closed.
currency 	string 		Base currency.
		"""
		d = {}

		#test position_direction value
		if position_direction is None or position_direction not in ['short','long']:
			print ("\nError, position_direction parameter value should either be 'short','long' \n")
			return
		else:
			d['direction'] = str(position_direction)

		#test market value
		if market is None:
			print ("\nError, please enter a market parameter value. Remember that you can also fetch available market symbol using getMarkets().\n")
			return
		else:
			d['market'] = str(market)

		#test position_type value
		if position_type is None:
			print ("\nError, please enter a position_type parameter value. Can be '1min' or '5min' .\n")
			return
		else:
			d['type'] = str(position_type)

		#test size value
		if size is None:
			print ("\nError, please enter a size parameter value. Should be a turbo position’s size, in satoshis.  .\n")
			return
		else:
			d['size'] = size

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'position-turbo/new'
		h = {"Authorization":"Bearer "+key,"Partner-Id":"fAoRwgvNoQjekD3Hk"}
		r = requests.post(url, headers=h, data=d)

		if self.verbose:
			print ('\nOpening a turbo position: \n')

		return self._checkResp(r)

	def getTurboPosition(self, position_id=None, key = None):
		"""
Fetch information about an existing turbo position.

arg:
----
position_id 	unique 	 Required.  ID that identify your position
key		string 	 Optional.  One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id 		string   	Unique ID for the turbo position.
contract_id	string	 	ID of the contract this turbo position belongs to.
direction 	string 	 	Can be long or short.
market 		string 		Market this turbo position was executed on.
state 		string 		Can be active, or closed.
size 		integer 	Position’s size, in satoshis.
entry_price 	number 		Price at which the turbo position was executed.
payoff 		number 		Payoff in case of correct prediction. Multiply by size to get payoff in satoshis.
close_price 	number 		Price at which the position was closed. Appears only if the position is closed.
profit 		number 		Profit made on the trade, in satoshis. Is negative in case of loss. Appears only if the position is closed.
created_at 	integer 	When the position was created.
closed_at 	integer 	When the position was closed. Appears only if the position is closed.
currency 	string 		Base currency.
		"""

		#test position_direction value
		if position_id is None:
			print ("\nError, please enter a position_id parameter value.\n")
			return

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'position-turbo/'+ position_id
		h = {"Authorization":"Bearer "+key}
		r = requests.get(url, headers=h)

		if self.verbose:
			print ('\nTurbo position informations: \n')

		return self._checkResp(r)

	def listturboPositions(self, position_state='active',limit=5, key=None):
		"""
List turbo positions.
Use this function to request a list of turbo positions. state can be active or closed. Defaults to activeself. 
Active positions are sorted by created_at and closed positions are sorted by closed_at.

args:
-----
position_state 	string 	Optional. State can be 'active', or 'closed'. Defaults to active
limit 		integer Optional. Number of results per request. Defaults to 5. Max is 30.
key     	string 	Optional. One API token to use, could be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
----
id 		string   	Unique ID for the turbo position.
contract_id	string	 	ID of the contract this turbo position belongs to.
direction 	string 	 	Can be long or short.
market 		string 		Market this turbo position was executed on.
state 		string 		Can be active, or closed.
size 		integer 	Position’s size, in satoshis.
entry_price 	number 		Price at which the turbo position was executed.
payoff 		number 		Payoff in case of correct prediction. Multiply by size to get payoff in satoshis.
close_price 	number 		Price at which the position was closed. Appears only if the position is closed.
profit 		number 		Profit made on the trade, in satoshis. Is negative in case of loss. Appears only if the position is closed.
created_at 	integer 	When the position was created.
closed_at 	integer 	When the position was closed. Appears only if the position is closed.
currency 	string 		Base currency.
		"""	
		d = {}

		#test limit parameter value
		if limit < 1 or limit > 30:
			print ('\nError, limit parameter value should be between 0 and 30')
			return
		else:
			d['limit'] = limit

		#test position_state parameter value
		if position_state not in ['active', 'closed']:
			print ("\nError, position_state parameter value should be either 'active', or 'closed'")
			return

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'positions-turbo/'+ position_state
		h = {"Authorization":"Bearer "+key}
		r = requests.get(url,headers=h,data = d)

		if self.verbose:
			print ('\nListing all turbo positions: \n')

		return self._checkResp(r)
