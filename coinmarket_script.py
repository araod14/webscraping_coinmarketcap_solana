import pandas as pd
import requests


def get_response_for(page):
    reqUrl = f"https://api.coinmarketcap.com/dexer/v3/platformpage/pair-pages?platform-id=16&dexer-id=1342&sort-field=txs24h&desc=true&page={page}&pageSize=50"
    resp = requests.get( reqUrl)
    if resp.status_code == 200:
        return resp.json()

def get_values(data):
    results = data['data']['pageList']
    results = [page for page in results]
    df = pd.DataFrame(results, columns= ["baseTokenSymbol", "quotoTokenName", "priceUsd", "volumeUsd24h"])
    return df

def evaluate(number): 
    data = get_response_for(number) 
    df = pd.DataFrame() 
    for i in range(1, number+1): 
        data = get_response_for(i) 
        values = get_values(data) 
        df = pd.concat([df, values], ignore_index=True) 
        df.to_csv("testcoin_all.csv") 
    return df

if __name__ == "__main__":
    pages = int(input("Numero de paginas: ",))
    print(evaluate(pages))