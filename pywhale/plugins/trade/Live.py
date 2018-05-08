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

class Live (object):
	"""	Whaleclub.co cryptocurrency Exchange API Pyhon Client Live trading functions:"""

	#TODO Test all parameter
	def newPosition(self, direction=None, market=None, leverage=None, size=None, entry_price=None, stop_loss=None, stop_loss_trailing=None, take_profit=None, key=None):
		"""
Submit a new position.
To submit a limit or stop order, set the entry_price parameter in your request. We’ll automatically detect whether it’s a limit order or a stop order based on the current market price.
To submit a market order, simply omit the entry_price parameter from your request. Your order will execute at the best available price.

args:
-----
direction		string 	Required Can be long or short.
market			string 	Required Market this position is executed on.
leverage		number 	Required Position’s leverage level.
size			integer Required Your position’s size, in satoshis. This is the total size including leverage, not the margin size.
entry_price		number 	Optional Set this to submit a limit/stop order. If omitted, your position will execute at the best available market price.
stop_loss		number 	Optional Price at which your position will auto-close in case of loss.
stop_loss_trailing	boolean Optional Set to true to enable the stop loss to trail. Works only if stop_loss is set.
take_profit		number 	Optional Price at which your position will auto-close in profit.
key   			string 	Optional One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id			string 	Unique ID for the position.
parent_id		string 	ID of parent position. Appears only if this position has been split.
slug			string 	A URL-friendly position identifier. Your position can be shared publicly at https://whaleclub.co/position/:slug.
direction		string 	Can be long or short.
market			string 	Market this position was executed on.
leverage		number 	Position’s leverage level.
type			string 	Order type. Can be market, limit, or stop.
state			string 	Can be pending, active, or closed.
size			integer Position’s size, in satoshis.
margin_size		integer Position’s margin size, in satoshis.
entry_price		number 	Price at which the position was executed (if at market) or will execute (if limit or stop).
stop_loss		number 	Price at which the position will auto-close in case of loss. Appears only if the position’s stop-loss is set.
stop_loss_trailing	object 	Returns {set: true} if the stop loss is a trailing stop loss.
take_profit		number 	Price at which the position will auto-close in profit. Appears only if the position’s take-profit is set.
close_reason		string 	How the position was closed. Can be at_market, at_stop, at_target, or liquidation. Appears only if the position is closed.
close_price		number 	Price at which the position was closed. Appears only if the position is closed.
profit			integer Profit made on the trade, in satoshis. Negative in case of loss. Appears only if the position is closed.
created_at		integer When the position was created.
entered_at		integer When the position was executed. Appears only if the position is active or closed.
closed_at		integer When the position was closed. Appears only if the position is closed.
ast_updated		integer When the position’s stop-loss and/or take-profit was last updated. Appears only if the position is manually updated after it’s been submitted.
liquidation_price	number 	Price at which the position will auto-close to cover your margin in case of loss.
financing		integer Leverage financing charged on the position, in satoshis. Appears only if the position is active or closed.
currency		string 	Base currency.
		"""

		d = {}
		#test direction value
		if direction is None or direction not in ['short','long']:
			print ("\nError, direction parameter value should either be 'short','long' \n")
			return
		else:
			d['direction'] = str(direction)

		#test market value
		if market is None:
			print ("\nError, please enter a market parameter value. Remember that you can also fetch available market symbol using getMarkets().\n")
			return
		else:
			d['market'] = str(market)

		#test leverage value
		if leverage is None or leverage < 0:
			print ("\nError, please enter a correct leverage value. Remember that you can also fetch available market leverage max using getMarkets().\n")
			return
		else:
			d['leverage'] = leverage

		#test size value
		if size is None or size < 0:
			print ("\nError, please enter a correct positive size value in satoshis. This is the total size including leverage, not the margin size.\n")
			return
		else:
			d['size'] = str(size)

		#test entry_price value
		if entry_price is not None:
			if entry_price > 0:
				d['entry_price'] = entry_price
			else:
				print ("\nError, please enter a positive entry_price value in satoshis.\n")
				return

		#test stop_loss value
		if stop_loss is not None:
			if stop_loss > 0:
				d['stop_loss'] = stop_loss
			else:
				print ("\nError, please enter a positive stop_loss value in satoshis.\n")
				return

		#test stop_loss_trailing value
		if stop_loss_trailing is not None:
			if stop_loss_trailing in [True,False]:
				d['stop_loss_trailing'] = stop_loss_trailing
			else:
				print ("\nError, please enter a correct stop_loss_trailing value in satoshis. May either be True or False, works only if stop_loss is set.\n")
				return

		#test take_profit value
		if take_profit is not None:
			if take_profit > 0:
				d['take_profit'] = take_profit
			else:
				print ("\nError, please enter a positive stop_loss value in satoshis.\n")
				return

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return


		#Create request elements
		url = self.start_url+'position/new'
		h = {"Authorization":"Bearer "+key,"Partner-Id":"fAoRwgvNoQjekD3Hk"}
		r = requests.post(url,headers=h,data=d)

		if self.verbose:
			print ('\nCreating a Position:')

		return self._checkResp(r)

	def getPosition(self, position_id=None, key=None):
		"""
Fetch information about an existing position.

args:
-----
position_id 		string 	Id of the Position we want to get informations about
key 			string 	Optional One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id			string 	Unique ID for the position.
parent_id		string 	ID of parent position. Appears only if this position has been split.
slug			string 	A URL-friendly position identifier. Your position can be shared publicly at https://whaleclub.co/position/:slug.
direction		string 	Can be long or short.
market			string 	Market this position was executed on.
leverage		number 	Position’s leverage level.
type			string 	Order type. Can be market, limit, or stop.
state			string 	Can be pending, active, or closed.
size			integer Position’s size, in satoshis.
margin_size		integer Position’s margin size, in satoshis.
entry_price		number 	Price at which the position was executed (if at market) or will execute (if limit or stop).
stop_loss		number 	Price at which the position will auto-close in case of loss. Appears only if the position’s stop-loss is set.
stop_loss_trailing	object 	Returns {set: true} if the stop loss is a trailing stop loss.
take_profit		number 	Price at which the position will auto-close in profit. Appears only if the position’s take-profit is set.
close_reason		string 	How the position was closed. Can be at_market, at_stop, at_target, or liquidation. Appears only if the position is closed.
close_price		number 	Price at which the position was closed. Appears only if the position is closed.
profit			integer Profit made on the trade, in satoshis. Negative in case of loss. Appears only if the position is closed.
created_at		integer When the position was created.
entered_at		integer When the position was executed. Appears only if the position is active or closed.
closed_at		integer When the position was closed. Appears only if the position is closed.
ast_updated		integer When the position’s stop-loss and/or take-profit was last updated. Appears only if the position is manually updated after it’s been submitted.
liquidation_price	number 	Price at which the position will auto-close to cover your margin in case of loss.
financing		integer Leverage financing charged on the position, in satoshis. Appears only if the position is active or closed.
currency		string 	Base currency.
		"""

		#Test position_id 
		if position_id is None:
			print ('\nError, enter an position_id value.')

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'position/'+position_id
		h = {"Authorization":"Bearer "+key}
		r = requests.get(url,headers=h)

		if self.verbose:
			print ('\nGet position information: \n')

		return self._checkResp(r)

	def updatePosition(self, position_id=None, stop_loss=None, stop_loss_trailing=None, take_profit=None, key=None):
		"""
Fetch information about an existing position.

args:
position_id 		string 				Required. 	Id of the Position we want to get informations about
stop_loss 		number 				Optional. 	Price at which the position will auto-close in case of loss. Must be set if take_profit is not. Set to 0 to remove an existing stop-loss.
stop_loss_trailing 	boolean or number 		Optional. 	Set to true to enable the stop loss to trail. Works only if stop_loss is set. Set to 0 to disable trailing.
take_profit 		number 				Optional. 	rice at which the position will auto-close in profit. Must be set if stop_loss is not. Set to 0 to remove an existing take-profit.
key 			string 				Optional. 	One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id			string 	Unique ID for the position.
parent_id		string 	ID of parent position. Appears only if this position has been split.
slug			string 	A URL-friendly position identifier. Your position can be shared publicly at https://whaleclub.co/position/:slug.
direction		string 	Can be long or short.
market			string 	Market this position was executed on.
leverage		number 	Position’s leverage level.
type			string 	Order type. Can be market, limit, or stop.
state			string 	Can be pending, active, or closed.
size			integer Position’s size, in satoshis.
margin_size		integer Position’s margin size, in satoshis.
entry_price		number 	Price at which the position was executed (if at market) or will execute (if limit or stop).
stop_loss		number 	Price at which the position will auto-close in case of loss. Appears only if the position’s stop-loss is set.
stop_loss_trailing	object 	Returns {set: true} if the stop loss is a trailing stop loss.
take_profit		number 	Price at which the position will auto-close in profit. Appears only if the position’s take-profit is set.
close_reason		string 	How the position was closed. Can be at_market, at_stop, at_target, or liquidation. Appears only if the position is closed.
close_price		number 	Price at which the position was closed. Appears only if the position is closed.
profit			integer Profit made on the trade, in satoshis. Negative in case of loss. Appears only if the position is closed.
created_at		integer When the position was created.
entered_at		integer When the position was executed. Appears only if the position is active or closed.
closed_at		integer When the position was closed. Appears only if the position is closed.
ast_updated		integer When the position’s stop-loss and/or take-profit was last updated. Appears only if the position is manually updated after it’s been submitted.
liquidation_price	number 	Price at which the position will auto-close to cover your margin in case of loss.
financing		integer Leverage financing charged on the position, in satoshis. Appears only if the position is active or closed.
currency		string 	Base currency.
		"""

		d = {}

		#Test position_id 
		if position_id is None:
			print ('\nError, enter an position_id value.')

		#test stop_loss value
		if stop_loss is not None:
			if stop_loss > 0:
				d['stop_loss'] = stop_loss
			else:
				print ("\nError, please enter a positive stop_loss value in satoshis.\n")
				return

		#test stop_loss_trailing value
		if stop_loss_trailing is not None:
			if stop_loss_trailing in [True,False,1,0]:
				d['stop_loss_trailing'] = stop_loss_trailing
			else:
				print ("\nError, please enter a correct stop_loss_trailing value in satoshis. May either be True or False, works only if stop_loss is set.\n")
				return

		#test take_profit value
		if take_profit is not None:
			if take_profit > 0:
				d['take_profit'] = take_profit
			else:
				print ("\nError, please enter a positive stop_loss value in satoshis.\n")
				return


		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'position/update/'+position_id
		h = {"Authorization":"Bearer "+key,"Partner-Id":"fAoRwgvNoQjekD3Hk"}
		r = requests.put(url, headers=h, data=d)

		if self.verbose:
			print ('\nUpdating position : \n')

		return self._checkResp(r)

	def closePosition(self, position_id=None, key=None):
		"""
Close one or multiple active positions at market price.
position_id is a list of one or more comma-separated position IDs.
Use this function to close existing active positions at the best available market price.
Positions are closed sequentially as they hit our system (not in parallel). 
If you’re closing a large number of positions at once, the market price may move in the time it takes to close them all.
If you’re looking to close at a specific market price, close your positions individually or use a take-profit or stop-loss.


args:
-----
position_id 		string 				Required. 	Id of the Position we want to get informations about
stop_loss 		number 				Optional. 	Price at which the position will auto-close in case of loss. Must be set if take_profit is not. Set to 0 to remove an existing stop-loss.
stop_loss_trailing 	boolean or number 		Optional. 	Set to true to enable the stop loss to trail. Works only if stop_loss is set. Set to 0 to disable trailing.
take_profit 		number 				Optional. 	rice at which the position will auto-close in profit. Must be set if stop_loss is not. Set to 0 to remove an existing take-profit.
key 			string 				Optional. 	One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id			string 	Unique ID for the position.
parent_id		string 	ID of parent position. Appears only if this position has been split.
slug			string 	A URL-friendly position identifier. Your position can be shared publicly at https://whaleclub.co/position/:slug.
direction		string 	Can be long or short.
market			string 	Market this position was executed on.
leverage		number 	Position’s leverage level.
type			string 	Order type. Can be market, limit, or stop.
state			string 	Can be pending, active, or closed.
size			integer Position’s size, in satoshis.
margin_size		integer Position’s margin size, in satoshis.
entry_price		number 	Price at which the position was executed (if at market) or will execute (if limit or stop).
stop_loss		number 	Price at which the position will auto-close in case of loss. Appears only if the position’s stop-loss is set.
stop_loss_trailing	object 	Returns {set: true} if the stop loss is a trailing stop loss.
take_profit		number 	Price at which the position will auto-close in profit. Appears only if the position’s take-profit is set.
close_reason		string 	How the position was closed. Can be at_market, at_stop, at_target, or liquidation. Appears only if the position is closed.
close_price		number 	Price at which the position was closed. Appears only if the position is closed.
profit			integer Profit made on the trade, in satoshis. Negative in case of loss. Appears only if the position is closed.
created_at		integer When the position was created.
entered_at		integer When the position was executed. Appears only if the position is active or closed.
closed_at		integer When the position was closed. Appears only if the position is closed.
ast_updated		integer When the position’s stop-loss and/or take-profit was last updated. Appears only if the position is manually updated after it’s been submitted.
liquidation_price	number 	Price at which the position will auto-close to cover your margin in case of loss.
financing		integer Leverage financing charged on the position, in satoshis. Appears only if the position is active or closed.
currency		string 	Base currency.
		"""

		#Test position_id 
		if position_id is None:
			print ('\nError, enter an position_id value.')

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'position/close/'+position_id
		h = {"Authorization":"Bearer "+key,"Partner-Id":"fAoRwgvNoQjekD3Hk"}
		r = requests.put(url, headers=h)

		if self.verbose:
			print ('\nClosing position : \n')

		return self._checkResp(r)

	def cancelPosition(self, position_id=None, key=None):
		"""
Cancel one or multiple pending positions.
position_id is a list of one or more comma-separated position IDs.
This function allows you to cancel limit or stop orders that haven’t yet executed. Once cancelled, your positions will be deleted and will no longer be accessible.


args:
position_id 		string 		Required. 	Id of the Position we want to get informations about
key 			string 		Optional. 	One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id			string 	Unique ID for the position.
parent_id		string 	ID of parent position. Appears only if this position has been split.
slug			string 	A URL-friendly position identifier. Your position can be shared publicly at https://whaleclub.co/position/:slug.
direction		string 	Can be long or short.
market			string 	Market this position was executed on.
leverage		number 	Position’s leverage level.
type			string 	Order type. Can be market, limit, or stop.
state			string 	Can be pending, active, or closed.
size			integer Position’s size, in satoshis.
margin_size		integer Position’s margin size, in satoshis.
entry_price		number 	Price at which the position was executed (if at market) or will execute (if limit or stop).
stop_loss		number 	Price at which the position will auto-close in case of loss. Appears only if the position’s stop-loss is set.
stop_loss_trailing	object 	Returns {set: true} if the stop loss is a trailing stop loss.
take_profit		number 	Price at which the position will auto-close in profit. Appears only if the position’s take-profit is set.
close_reason		string 	How the position was closed. Can be at_market, at_stop, at_target, or liquidation. Appears only if the position is closed.
close_price		number 	Price at which the position was closed. Appears only if the position is closed.
profit			integer Profit made on the trade, in satoshis. Negative in case of loss. Appears only if the position is closed.
created_at		integer When the position was created.
entered_at		integer When the position was executed. Appears only if the position is active or closed.
closed_at		integer When the position was closed. Appears only if the position is closed.
ast_updated		integer When the position’s stop-loss and/or take-profit was last updated. Appears only if the position is manually updated after it’s been submitted.
liquidation_price	number 	Price at which the position will auto-close to cover your margin in case of loss.
financing		integer Leverage financing charged on the position, in satoshis. Appears only if the position is active or closed.
currency		string 	Base currency.
		"""

		#Test position_id 
		if position_id is None:
			print ('\nError, enter an position_id value.')

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'position/cancel/'+position_id
		h = {"Authorization":"Bearer "+key}
		r = requests.put(url, headers=h)

		if self.verbose:
			print ('\nCanceling position: \n')

		return self._checkResp(r)

	def splitPosition(self, position_id=None, ratio=None, key=None):
		"""
Split an existing pending or active position.
This function  allows you to split an existing position according to a ratio you provide. It can only be called on a pending or active position.

args:
position_id 		string 		Required. 	Id of the Position we want to get informations about
ratio			integer		Required 	Pourcent you want to split your position. Must be between 5 and 95.
key 			string 		Optional. 	One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id			string 	Unique ID for the position.
parent_id		string 	ID of parent position. Appears only if this position has been split.
slug			string 	A URL-friendly position identifier. Your position can be shared publicly at https://whaleclub.co/position/:slug.
direction		string 	Can be long or short.
market			string 	Market this position was executed on.
leverage		number 	Position’s leverage level.
type			string 	Order type. Can be market, limit, or stop.
state			string 	Can be pending, active, or closed.
size			integer Position’s size, in satoshis.
margin_size		integer Position’s margin size, in satoshis.
entry_price		number 	Price at which the position was executed (if at market) or will execute (if limit or stop).
stop_loss		number 	Price at which the position will auto-close in case of loss. Appears only if the position’s stop-loss is set.
stop_loss_trailing	object 	Returns {set: true} if the stop loss is a trailing stop loss.
take_profit		number 	Price at which the position will auto-close in profit. Appears only if the position’s take-profit is set.
close_reason		string 	How the position was closed. Can be at_market, at_stop, at_target, or liquidation. Appears only if the position is closed.
close_price		number 	Price at which the position was closed. Appears only if the position is closed.
profit			integer Profit made on the trade, in satoshis. Negative in case of loss. Appears only if the position is closed.
created_at		integer When the position was created.
entered_at		integer When the position was executed. Appears only if the position is active or closed.
closed_at		integer When the position was closed. Appears only if the position is closed.
ast_updated		integer When the position’s stop-loss and/or take-profit was last updated. Appears only if the position is manually updated after it’s been submitted.
liquidation_price	number 	Price at which the position will auto-close to cover your margin in case of loss.
financing		integer Leverage financing charged on the position, in satoshis. Appears only if the position is active or closed.
currency		string 	Base currency.
		"""
		d = {}

		#Test position_id 
		if position_id is None:
			print ('\nError, enter an position_id value.')
			return

		#Test ratio parameter
		if ratio is None or ratio < 5 or ratio > 95:
			print ('\nError, enter a ratio value between 5 and 95.')
			return
		else:
			d['ratio'] = ratio

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'position/split/'+position_id
		h = {"Authorization":"Bearer "+key,"Partner-Id":"fAoRwgvNoQjekD3Hk"}
		r = requests.post(url, headers=h,data=d)

		if self.verbose:
			print ('\nSplitting position : \n')

		return self._checkResp(r)

	def listPositions(self, position_state='active',limit=5, key=None):
		"""
List positions.
Use this function to request a list of positions. state can be 'pending', 'active', or 'closed'. Defaults to active.
It’s strongly recommended that you maintain your own list of positions and use the Price endpoint to keep it updated instead of polling this endpoint to track the state of your positions.
Pending positions are sorted by created_at, active positions are sorted by entered_at, and closed positions are sorted by closed_at.

args:
position_state		string 		Optional. 	State can be 'pending', 'active', or 'closed'. Defaults to active
limit 			integer 	Optional. 	Number of results per request. Defaults to 5. Max is 30.
key     		string 		Optional. 	One API token to use in order to send the request, could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'. DEFAULT is BTC_demo_key

resp:
-----
id			string 	Unique ID for the position.
parent_id		string 	ID of parent position. Appears only if this position has been split.
slug			string 	A URL-friendly position identifier. Your position can be shared publicly at https://whaleclub.co/position/:slug.
direction		string 	Can be long or short.
market			string 	Market this position was executed on.
leverage		number 	Position’s leverage level.
type			string 	Order type. Can be market, limit, or stop.
state			string 	Can be pending, active, or closed.
size			integer Position’s size, in satoshis.
margin_size		integer Position’s margin size, in satoshis.
entry_price		number 	Price at which the position was executed (if at market) or will execute (if limit or stop).
stop_loss		number 	Price at which the position will auto-close in case of loss. Appears only if the position’s stop-loss is set.
stop_loss_trailing	object 	Returns {set: true} if the stop loss is a trailing stop loss.
take_profit		number 	Price at which the position will auto-close in profit. Appears only if the position’s take-profit is set.
close_reason		string 	How the position was closed. Can be at_market, at_stop, at_target, or liquidation. Appears only if the position is closed.
close_price		number 	Price at which the position was closed. Appears only if the position is closed.
profit			integer Profit made on the trade, in satoshis. Negative in case of loss. Appears only if the position is closed.
created_at		integer When the position was created.
entered_at		integer When the position was executed. Appears only if the position is active or closed.
closed_at		integer When the position was closed. Appears only if the position is closed.
ast_updated		integer When the position’s stop-loss and/or take-profit was last updated. Appears only if the position is manually updated after it’s been submitted.
liquidation_price	number 	Price at which the position will auto-close to cover your margin in case of loss.
financing		integer Leverage financing charged on the position, in satoshis. Appears only if the position is active or closed.
currency		string 	Base currency.
		"""		
		d = {}

		#test limit parameter value
		if limit < 1 or limit > 30:
			print ('\nError, limit parameter value should be between 0 and 30')
			return
		else:
			d['limit'] = limit

		#test position_state parameter value
		if position_state not in ['pending', 'active', 'closed']:
			print ("\nError, position_state parameter value should be either 'pending', 'active', or 'closed'")
			return

		#test key parameter value is an accepted input
		test0 =  self._updateKey(key)
		if test0[0] is True:
			key = test0[1]
		else:
			return

		#Create request elements
		url = self.start_url+'positions/'+ position_state
		h = {"Authorization":"Bearer "+key}
		r = requests.get(url,headers=h,data = d)

		if self.verbose:
			print ('\nListing all Transactions: \n')

		return self._checkResp(r)
