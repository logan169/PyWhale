# PyWhale

![Alt text](/whale2.png?raw=true "pywhale logo")

## Python3 wrapper for whaleclub rest api

This repo contains a python3 wrapper for whaleclub rest api. It allows user to get mulptiple information and place live and turbo trades. For better user experience, I've paste/reformat whaleclub.co [api](http://docs.whaleclub.co/#list-turbo-positions) documentation for each function doc string. See usage section to see how it works.

This project was created on my own free time, so if you wish to support my work you could start by staring it and either:

* Consider creating an account using my whaleclub's referral link, so you'll get a 30% deposit bonus: 
  * https://whaleclub.co/join/pnI1A
* leave me a tip at:
  * (BTC) 19nm2SJW7zmNcePePW6pyZBh7FMcWZdYeY
  * (DASH) XpdDgn28F3GcwyBjHwb6yKXqJ9nYHbrdup

## License

GNU Lesser General Public

2017 Logan Schwartz logan1691987@gmail.com

pywhale is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

pywhale is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Dependencies

* Requests

## Installation
    $ pip3 install requests 
    $ git clone git@github.com:logan169/PyWhale.git
    $ cd PyWhale/app

## How to use it

After creating an account, get your API token from your API Settings panel which is available from the top right menu in your trading dashboard. You get one token for live trading and another for demo trading.

Then complet every following files with their respective api key:

- pywhale/app/BTC_demo_key.txt
- pywhale/app/BTC_real_key.txt
- pywhale/app/DASH_demo_key
- pywhale/app/DASH_real_key

#### Beware to not invert api key, I strongly advise that you verify twice that you've entered the right key in each file.

## Usage

    #Start ipython
    $ ipython3
    
    #Import module and create a PyWhale() instance
    $ from PyWhale import PyWhale
    $ pw = PyWhale()    
    
![Alt text](/pw.jpg?raw=true "pywhale logo")

    #Print help
    $ pw.help()
    
![Alt text](/help.jpg?raw=true "pywhale logo")
    
    #Get more information about a function
    $  print (pw.getBalance.__doc__)
    
![Alt text](/balance.jpg?raw=true "pywhale logo")
    
    #Remove print output function
    $ pw.verbose = False
    
    
### Default key

#### Pease note that if you don't pass a key parameter while calling a function, default.key 'BTC_demo_key' will be used.

    #Display actual default key that is going to be used (if key parameter is not specified)
    $ pw.default_key
    
    #Change default key 
    #Key parameter could either be 'BTC_real_key', 'BTC_demo_key', 'DASH_real_key' or 'DASH_demo_key'.
    $ pw.default_key = 'BTC_real_key'
    
    




