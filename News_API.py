
# importing json and requests
import requests
import json

API_KEY='ENTER_API_KEY_HERE'

#Sources Request Function
def request_sources():
    #Dictionary of possible categories
    categories = {
        1. : 'entertainment',
        2. : 'general',
        3. : 'health',
        4. : 'science',
        5. : 'sports',
        6. : 'technology'

    }
    
    #List Possible Switches
    print('[*] 1 => entertainment')
    print('[*] 2 => general')
    print('[*] 3 => health')
    print('[*] 4 => science')
    print('[*] 5 => sports')
    print('[*] 6 => technology')

    query = int(input("[?] Enter Sources Category Number => "))
    
    #If query is not in range circle back to initializer
    if (query >= 0) and (query < 7):
        category = categories[query]

        #Sources Request Call
        sources = requests.get('https://newsapi.org/v2/sources?category=%s&apiKey=%s' % (category, API_KEY))
        data = json.loads(sources.text)

        #Loop through sources key
        for source in data['sources']:
            print('[*] ID => %s' %(source['id']))
            print('[*] DESCRIPTION => %s' %(source['description']))
            print('\n')
    else:
        print('[!] Bad Category request')

#Article Request Function
def request_article():
    #Input  Query
    print('\n')
    query = raw_input("[?] Enter Article Request => ")
    print('\n')

    #Articles Request Call
    articles = requests.get('https://newsapi.org/v2/everything?q=%s&apiKey=%s' % (query, API_KEY))
    
    #JSON Convertion
    data = json.loads(articles.text)
    
    #Loop through articles key
    for article in data['articles']:
        print('[*] ARTICLE => %s' %(article['content']))
        print('[*] URL => %ss' %(article['url']))
        print('\n')

#Initializer
if (__name__ == "__main__"):
   #Function call switch statement
   api_function ={
       1. : request_sources,
       2. : request_article
   }

    #Selection Loop
   selection = 0
   while(selection != 3):
       print('[*] 1 => request sources')
       print('[*] 2 => request articles')
       print('[*] 3 => quit')
       print('\n')

       selection = int(input("[?] Select a API Option Number: "))

        #Will Quit if Input is greater than 3 
       if (selection >= 0) and (selection < 3):
            api_function[selection]()


   

