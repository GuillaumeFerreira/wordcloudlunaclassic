import asyncio
from terra_sdk.client.lcd import LCDClient
from terra_sdk.core.auth import data
import json, requests


def main():
    '''url = requests.get("https://columbus-lcd.terra.dev/blocks/latest")
    text = url.text
    data = json.loads(text)
    print(data['block']['header']['height'])


    url = requests.get("https://columbus-lcd.terra.dev/cosmos/auth/v1beta1/accounts/terra1sk06e3dyexuq4shw77y3dsv480xv42mq73anxu")
    text = url.text
    data = json.loads(text)
    print(data['account']['name'])'''

    terra = LCDClient(chain_id="phoenix-1", url="https://lcd.terra.dev")
    print(terra.tendermint.block_info()['block']['header']['height'])
    #print(terra.bank.total())
    print(str(terra.bank.balance('terra1sk06e3dyexuq4shw77y3dsv480xv42mq73anxu')[0]))
    #compte terra classic commun
    print(str(float(str(terra.bank.balance('terra1pqgnrz2sz2r7he6fj6zkvtczfzjhcg69zy297p')[0]).split(",")[14][:-5])/1000000)+(" LUNC"))
main()
