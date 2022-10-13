from django.views.generic import TemplateView, View
from django.urls import reverse
from terra_sdk.client.lcd import LCDClient
from terra_sdk.client.lcd import AsyncLCDClient
import asyncio

from django.http import HttpResponse

class IndexView(TemplateView):

    template_name = "index.html"

    def get_success_url(self):
        return reverse("index")


class ReadAdressLuncBurn(View):
    def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        terra = LCDClient("https://phoenix-lcd.terra.dev", "phoenix-1")
        #block = await
        print(terra.tendermint.block_info()['block']['header']['height'])
        #await terra.session.close  # you must close the session
        return HttpResponse("Hello async world!" + str(terra.tendermint.block_info()['block']['header']['height']))

