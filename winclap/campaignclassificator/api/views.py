import os
import json
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserDataSerializer


class CampaignClassificatorAPIView(APIView):
    def get(self, request, format=None):
        serializer = UserDataSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, '..', 'datasets', 'campaigns.json')
        with open(file_path) as f:
            campaigns = json.load(f)
        valid_campaign_list = []
        for campaign in campaigns:
            invalid_gender = campaign['gender'] != 'All' and campaign['gender'] != user_data['gender']
            invalid_age = (campaign['min_age'] is not None and campaign['min_age'] > user_data['age']) or \
            (campaign['max_age'] is not None and campaign['max_age'] < user_data['age'])
            invalid_platform = campaign['platform'] != user_data['platform']
            invalid_connection = campaign['connection'] != 'All' and campaign['connection'] != user_data['connection']

            if not any([invalid_age, invalid_connection, invalid_gender, invalid_platform]):
                valid_campaign_list.append(campaign)

        return Response(random.choice(valid_campaign_list) if valid_campaign_list else None)
