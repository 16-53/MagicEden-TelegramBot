import requests
import json


def result(skip_n):
    return requests.get('https://api-mainnet.magiceden.dev/rpc/getListedNFTsByQuery', params={'q': json.dumps({'$match': {'collectionSymbol': 'magicticket'}, "$skip":skip_n, "$limit":20})})


def prices():
    n = 0
    min_normie = 165316531653
    min_degen = 165316531653
    min_og = 165316531653

    while len(result(n).json()['results']) == 20:
        now = result(n)
        for i in range(20):
            if now.json()['results'][i]['attributes'][1]['value'] == 'Normie' and\
                    now.json()['results'][i]['price'] < min_normie:
                min_normie = now.json()['results'][i]['price']

            elif now.json()['results'][i]['attributes'][1]['value'] == 'Degen' and\
                    now.json()['results'][i]['price'] < min_degen:
                min_degen = now.json()['results'][i]['price']

            elif now.json()['results'][i]['attributes'][1]['value'] == 'OG' and\
                    now.json()['results'][i]['price'] < min_og:
                min_og = now.json()['results'][i]['price']

        n += 20
        if n > 100:
            break

    return [min_normie, min_degen, min_og]