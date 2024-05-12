import os
import csv
import requests

class api_tools:
    def __init__(self, headers):
        self.headers = headers
    
    def make_csv(self, csv_file_name, data_list):
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data_list)
    
    def get_data_with_api_json(self, url):
        raw_data = requests.get(url, headers = self.headers)   
        data = raw_data.json()
        return(data)
    
    def get_images(self, action_folder_path, normal_folder_path, spid_data):
        for spid in spid_data:
            action_image_url = "https://fco.dn.nexoncdn.co.kr/live/externalAssets/common/playersAction/p{id}.png".format(id = spid['id'])
            normal_image_url = "https://fco.dn.nexoncdn.co.kr/live/externalAssets/common/players/p{id}.png".format(id = spid['id'])
            
            action_image = requests.get(action_image_url, headers = self.headers)
            normal_image = requests.get(normal_image_url, headers = self.headers)
            
            if action_image.status_code == 200:
                action_file_path = os.path.join(action_folder_path, f"{spid['id']}.png")
                # 이미지 파일로 저장
                with open(action_file_path, "wb") as file:
                    file.write(action_image.content)
                print(f"이미지 저장 성공: {action_file_path}")
            else:
                print(f"이미지 저장 실패: {spid['id']}, HTTP 상태 코드: {action_image.status_code}")

            if normal_image.status_code == 200:
                normal_file_path = os.path.join(normal_folder_path, f"{spid['id']}.png")
                # 이미지 파일로 저장
                with open(normal_file_path, "wb") as file:
                    file.write(normal_image.content)
                print(f"이미지 저장 성공: {normal_file_path}")
            else:
                print(f"이미지 저장 실패: {spid['id']}, HTTP 상태 코드: {normal_image.status_code}")\
            
    def get_match_data(self, matchtype, offset, limit, orderby):
        response = requests.get(
            'https://open.api.nexon.com/fconline/v1/match',
            headers= self.headers,
            params={
                'matchtype': matchtype,
                'offset': offset,
                'limit': limit,
                'orderby': 'desc'
            }
        )

        data = response.json()
        return data
    
    def get_match_detail_data(self, matchid):
        url = f'https://open.api.nexon.com/fconline/v1/match-detail'
        headers = self.headers
        params = {
            'matchid': matchid
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()  # 성공적으로 데이터를 받아오면 JSON 형태로 반환
        else:
            return None  # 요청이 실패하면 None 반환