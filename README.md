![Alt text](/picts/whale2.png?raw=true "pywhale logo")

## __:whale: Python3 wrapper for whaleclub REST api:__

PyWhale is a python3 wrapper for [whaleclub.co REST api](http://docs.whaleclub.co/#overview). [Whaleclub.co](https://whaleclub.co/) in addition of offering a demo mode for newcomers, is a great trading exchange platform having one of the best UI and support service I've saw so far. 

PyWhale was created to keep things as simple and intuitive as possible while performing complex requests to REST api. It contains all functions available in [whaleclub.co REST api documentation](http://docs.whaleclub.co/#overview) allowing user to get simultaniously up to 5 markets price, place live or turbo trades, easily switch between real/demo mode or BTC/DASH trading and much more. For better user experience, I've took the liberty to reformat whaleclub.co api functions documentation into functions doc string so one could access all relevants informations directly.

As far as I know, PyWhale is the only alternative language available if you can't (or just do not want to) use the javascript wrapper in order to interact with whaleclub REST api. PyWhale was created on my own free time, so if you wish to support my work you could start by staring it and either:

* Consider creating an account using my whaleclub's referral link, so you'll get a 30% deposit bonus: 
  * https://whaleclub.co/join/pnI1A
* leave me a tip at:
  * (BTC) 1MsRAPzQyvoRa5w3oBbPveSg6y6S7Ycogg

## __Dependencies:__

* Requests
* Statistics

## __Installation:__
    $ pip3 install pywhale

## __How to use it:__

After creating an account (just click on above referral links if you don't have one yet), get your API token from your API Settings panel which is available from the top right menu in your trading dashboard. You get one token for live trading and another for demo trading for each BTC/DASH cryptocurrencies.

Then copy/paste each api key in the respective following files:

- {pywhale installation folder}/api_keys/BTC_demo_key.txt
- {pywhale installation folder}/api_keys/BTC_real_key.txt
- {pywhale installation folder}/api_keys/DASH_demo_key.txt
- {pywhale installation folder}/api_keys/DASH_real_key.txt
- {pywhale installation folder}/api_keys/ETH_real_key.txt
- {pywhale installation folder}/api_keys/LTC_real_key.txt

if you don't know your "pywhale installation folder", you could find it in an error message if you type in a ipython3 terminal

    $ from PyWhale import PyWhale

##### __*Beware to not invert api key, this step is critical so I strongly advise that you check that part twice.*__

## __Usage:__

##### __Lets do some Whaly stuff:__
    
    $ from PyWhale import PyWhale
    $ pw = PyWhale()  
    
![Alt text](/picts/pw.jpg?raw=true "pywhale logo")

##### __See all available PyWhale functions:__

    $ pw.help()
    
![Alt text](/picts/help.jpg?raw=true "pywhale logo")

##### __See all relevants functions informations and input parameters:__

    $ print (pw.function_name.__doc__)
    
![Alt text](/picts/balance.jpg?raw=true "pywhale logo")


##### __Switch between real/demo mode & BTC/DASH trading:__

In PyWhale, you could easily switch between real/demo mode & BTC/DASH trading by directly passing key value in function inputs so you don't have to memorize several functions to do the same thing for each mode.

###### __Possible key values:__

- 'BTC_real_key'
- 'BTC_demo_key'
- 'DASH_real_key'
- 'DASH_demo_key'
- 'ETH_real_key'
- 'LTC_real_key'

###### __Examples:__

    # Create a new turbo position for DASH demo mode
    $ pw.createNewTurboPosition(market='BTC-USD',position_direction='long',position_type='5min',size=100000,key='DASH_demo_key')

![Alt text](/picts/passing_key.jpg?raw=true "pywhale logo")

The previous approach works well if you want to change real/demo mode & BTC/DASH trading punctually, but if you have planned just trading using only one mode this could get quickly tedious. For this reason, I've set a default_key attribute that could be changed once and will be then used automatically as the default key parameter value while calling further functions. 

In other words, if you don't pass a key parameter value while calling a function, default.key attribute value will be used.
You should note that after creating a PyWhale instance, default_key attribute value is 'BTC_demo_key' so you could safely call functions without any fears of using your real balance from starts.

    # Display actual default_key attribute
    $ pw.default_key
    
    # Change default_key attribute
    $ pw.default_key = 'DASH_demo_key'
    
![Alt text](/picts/default_key.jpg?raw=true "pywhale logo")


##### __Want just ipython output?:__

$ pw.verbose = False

![Alt text](/picts/verbose.jpg?raw=true "pywhale logo")

## Contributors:

- xmatthias
    
## __License__:

GNU Lesser General Public

2017 Logan Schwartz logan1691987@gmail.com

pywhale is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

pywhale is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
