from api_tools import api_tools

import requests

headers = {
"x-nxopen-api-key": 'test_09072c1b3466d1bb208e56bb6fd7f5bb18551c5976a7caa89695e738912d5c2a89635e0a863e1909dc86bbbe7f33c0a8',
}
tools = api_tools(headers)

all_match_data = []

matchtype = 50
limit = 100  # 한 번에 가져올 수 있는 최대 데이터 수
total_data = 10000  # 가져오고 싶은 총 데이터 수
number_of_calls = total_data // limit  # API를 호출해야 하는 횟수

for i in range(number_of_calls):
    offset = i * limit
    match_data = tools.get_match_data(matchtype, offset, limit, 'desc')
    
    # API 호출로 받아온 데이터에서 각 아이템을 all_match_data 리스트에 추가
    all_match_data.extend(match_data)


match_detail = tools.get_match_detail_data(all_match_data[4])
print(match_detail)
# all_match_data_details = []
# for matchid in all_match_data:
#     match_detail = tools.get_match_detail_data(matchid)
#     if match_detail:
#         ############우선은 모든 데이터를 다 저장하지만, 데이터 정의를 보고 필요한 것만 뽑아서 정리 할 것 여기서##############
#         all_match_data_details.append(match_detail)    ['matchDetail']['player']