from bs4 import BeautifulSoup
import requests
import time
from pygame import mixer

mixer.init()    
alert_sound = mixer.Sound('cat.wav')

# URL for page to been examined. Change this URL for page you wish. Use scrapers responsibly. Do not automate access to websites without permission. DDOS attacks are a crime.
url = 'https://www.binance.com/en-GB/price/bitcoin' 

while True:
   
    time.sleep(10) # Higher value set to avoid DDOS attacks interpretation by the server.
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')

    # Get all the text from the BeautifulSoup object
    text = doc.get_text()

    # Find the first occurrence of the dollar sign in the text
    dollar_index = text.find('$')

    amount = 0

    # If the dollar sign was found, print it and the following 10 characters
    if dollar_index != -1:
        print(text[dollar_index:dollar_index+10])
        amount = text[dollar_index+1:dollar_index+10]
        try:
            amount = float(amount.replace(',', ''))  # Convert amount to a float, removing commas if necessary. 
            if amount < 53000: # To test this code, change this value to a higher value than the current price of Bitcoin.
                print('Bitcoin is below $53,000!! Maybe it is time to buy some more!')
                alert_sound.play()
            elif amount < 40000:
                print('Bitcoin is below $40,000!! Cut your losses and sell! This ship is going down!')
                alert_sound.play()
            else:
                continue
        except ValueError:
            print("Could not convert amount to a float")
    else:
        print("Dollar sign not found")