import requests
import json

url = 'https://api.novaposhta.ua/v2.0/json/'


# apiKey - your personal api key from NP, but we can get status code without api key
# DocumentNumber - track number
# Phone - you need this parameter for advanced info


class TrackingNP:
    """Main class"""

    def __init__(self, trackID, phone):
        self.trackID = trackID
        self.phone = phone


    def status_check(self):
        """Send request for NP with our track number and get status"""
        param = {
            "apiKey": '',
            "modelName": "TrackingDocument",
            "calledMethod": "getStatusDocuments",
                 "methodProperties": {
                     "Documents": [{"DocumentNumber": str(self.trackID), "Phone": str(self.phone)}]
                 }
        }
        json_param = json.dumps(param)
        resp = requests.get(url, data=json_param)
        r = resp.json()  # parse json
        data_list = r['data']
        data_dict = data_list[0]
        status_code = int(data_dict.get('StatusCode'))
        if status_code == 3:
            not_found = 'Посилку з даним номером не знайдено!'
            return not_found
        if status_code == 7 or 8:
            in_warehouse = 'Посилка прибула на відділення'
            return in_warehouse
        if status_code == 11 or 9 or 10 or 106:
            success = 'Посилку отримано!'
            return success
        if status_code == 4 or 41 or 5 or 6 or 101:
            delivering = 'Посилка ще в дорозі'
            return delivering
        else:
            not_delivered = 'Посилка ще не отримана'
            return not_delivered

if __name__ == '__main__':
    trackID = '59000000000000'
    phone = '09877777777'
    get_track = TrackingNP(trackID, phone)
    g = get_track.status_check()
    print(g)
