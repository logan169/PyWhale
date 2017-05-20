# PyWhale

![Alt text](/whale2.png?raw=true "pywhale logo")

## Python3 wrapper for whaleclub rest api


This repo contains a python3 wrapper for whaleclub rest api. The main goal was to make it as simple as possible.

For better user experience, I've paste/reformat whaleclub.co [api] (http://docs.whaleclub.co/#list-turbo-positions) documentation for each function doc string. Please refer to the link above for up to date documentation.

This project was created on my own free time, so if you wish to support my work you could either:

- Consider creating an account using my whaleclub's referral link, so you'll get a 30% deposit bonus: https://whaleclub.co/join/pnI1A
- leave me a tip at (BTC): 19nm2SJW7zmNcePePW6pyZBh7FMcWZdYeY or (DASH) XpdDgn28F3GcwyBjHwb6yKXqJ9nYHbrdup

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
    
    #Import module
    $ from PyWhale import PyWhale
        
    #Create a PyWhale() instance
    $ pw = PyWhale()    

    #Print help
    $ print(pw.help())
    
    #Remove print output function
    $ pw.verbose = False
    
    #Remove print output function
    $ pw.verbose = False



