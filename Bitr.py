from bittrex import Bittrex, API_V1_1
from coinmarketcap import CoinMarketCap

def check_coin(name):
    market = CoinMarketCap()
    resp = market.coin_ticker_list(convert="USD", start=1,disable_cache=False)
    names = []
    ids = []
    for i in resp['data'].keys():
        names.append(resp['data'][i]['symbol'])
        ids.append(i)
    if name in names:
        ind = ids[names.index(name)]
        if name!='XRP':
                link = resp['data'][ind]['name']
        else:
                link = 'ripple'
        return(resp['data'][ind]['quotes']['USD']['percent_change_24h'],resp['data'][ind]['quotes']['USD']['percent_change_7d'],link)
    else:
        return(None)
def get_histor(market):
        my_bittrex = Bittrex(None, None, api_version=API_V1_1)  
        result = my_bittrex.get_market_summary(market)
        return(result['result'][0]['High'],result['result'][0]['Low'])

def get_eth():
        market = CoinMarketCap()
        resp = market.coin_ticker_detail(2, convert="USD", disable_cache=False)
        return(resp['data']['quotes']['USD']['price'])

def get_bitr(coin):
    my_bittrex = Bittrex(None, None, api_version=API_V1_1)
    l = []
    p = []
    markets = my_bittrex.get_markets()
    tick = my_bittrex.get_ticker('NEO-USDT')
    i=0
    eth = get_eth()
    while i<289:
        l.append(markets['result'][i]['MarketName'])
        i=i+1
    for i in l:
        if i[:3]=='ETH':
            p.append(i)
    i=0
    tr=False    
    while i<len(p):
        if coin==p[i][4:]:
                tick = my_bittrex.get_ticker(p[i])
                tr=True
                try:
                    highlow = get_histor(p[i])
                except:
                        print('Cant')   
                break
        i=i+1
    if tr==True:
        try:
                tests = check_coin(coin)
                link = 'https://coinmarketcap.com/currencies/{}/'.format(tests[2])
                return('1 ' + coin +' = ' + str(round(tick['result']['Bid']*eth,2)) + " USD\nСамая высокая цена: {} USD,\nСамая низкая цена: {} USD".format(round(highlow[0]*eth,2),round(highlow[1]*eth,2))+'\nИзменение за 24 часа: {} USD'.format(str(tests[0]))+'\nИзменение за 7 дней: {} USD\nСсылка на токен: '.format(str(tests[1]))+link)
        except:
                return('1 ' + coin +' = ' + str(tick['result']['Bid']*eth) + ' USD')
    else:
        return('Информации не найдено')
