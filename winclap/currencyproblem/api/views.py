import os
import json
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from rest_framework.views import APIView
from rest_framework.response import Response


class CurrencyProblemAPIView(APIView):
    def get(self, request, format=None):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, '..', 'datasets', 'campaigns.json')
        with open(file_path) as f:
            campaigns = json.load(f)
        campaign_list = []
        for campaign in campaigns:
            total_profit = (campaign['revenue'] - campaign['cost']) * campaign['conversions']
            currency = campaign['currency']
            url = 'https://www.google.com/finance/converter?a=%s&from=%s&to=USD' % (total_profit, currency)
            content = urlopen(url).read()
            soup = BeautifulSoup(content)
            div_result = soup.find("div", {"id": "currency_converter_result"})
            span_result = div_result.find("span")
            total_profit = re.findall("\d+\.\d+", span_result.getText())[0]
            campaign_list.append({'id': campaign['id'], 'name': campaign['name'], 'total_profit': total_profit})

        return Response(campaign_list if campaign_list else None)


