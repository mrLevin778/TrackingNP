import requests
import json

url = 'https://api.novaposhta.ua/v2.0/json/'
trackID = '20400318832057'  # these goods are delivered


# apiKey - your personal api key from NP, but we can get status code without api key
# DocumentNumber - track number
# Phone - you need this parameter for advanced info


class TrackingNP:
    """Main class"""

    def __init__(self, trackID):
        self.trackID = trackID

    @staticmethod
    def statusCheck():
        """Send request for NP with our track number and get status"""
        param = {"apiKey": "", "modelName": "TrackingDocument", "calledMethod": "getStatusDocuments",
                 "methodProperties": {"Documents": [{"DocumentNumber": str(trackID), "Phone": ""}]}}
        json_param = json.dumps(param)
        resp = requests.get(url, data=json_param)
        r = resp.json()  # parse json
        data_list = r["data"]
        data_dict = data_list[0]
        status_code = int(data_dict.get("StatusCode"))
        if status_code == 11 or status_code == 9 or status_code == 10 or status_code == 106:
            success = 'Посилку отримано!'
            return success
        else:
            not_delivered = 'Посилка ще не отримана'
            return not_delivered


get_track = TrackingNP(trackID)
g = get_track.statusCheck()
print(g)
