# PyWhale

![Alt text](/whale2.png?raw=true "pywhale logo")

## Python3 wrapper for whaleclub rest api

This repo contains a python3 wrapper for whaleclub rest api. It allows user to get mulptiple information and place live and turbo trades. For better user experience, I've paste/reformat whaleclub.co [api] (http://docs.whaleclub.co/#list-turbo-positions) documentation for each function doc string. See usage section to see how it works.

This project was created on my own free time, so if you wish to support my work you could either:

- Consider creating an account using my whaleclub's referral link, so you'll get a 30% deposit bonus: https://whaleclub.co/join/pnI1A
- leave me a tip at (BTC): 19nm2SJW7zmNcePePW6pyZBh7FMcWZdYeY or (DASH) XpdDgn28F3GcwyBjHwb6yKXqJ9nYHbrdup

## License

The MIT License (MIT)

Copyright (c) 2013 Mike van Rossum mike@mvr.me

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Installation

    $ git clone
    $ cd pywhale/app

## How to use it

After creating an account, get your API token from your API Settings panel which is available from the top right menu in your trading dashboard. You get one token for live trading and another for demo trading.

Then complet every following files with their respective api key:

- pywhale/app/BTC_demo_key.txt
- pywhale/app/BTC_live_key.txt
- pywhale/app/DASH_demo_key
- pywhale/app/DASH_live_key

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
    
    #Display actual default key that is going to be used (if key parameter is not specified)
    #Default is 'BTC_demo_key'
    $ pw.default_key
    
    #Change default key 
    #Key parameter could either be 'BTC_live_key', 'BTC_demo_key', 'DASH_live_key' or 'DASH_demo_key'.
    $ pw.default_key = 'BTC_live_key'
    
    




