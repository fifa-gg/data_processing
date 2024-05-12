
from api_tools import api_tools

headers = {
"x-nxopen-api-key": 'test_09072c1b3466d1bb208e56bb6fd7f5bb18551c5976a7caa89695e738912d5c2a89635e0a863e1909dc86bbbe7f33c0a8',
}
tools = api_tools(headers)
##########매치 종류(matchtype) 메타데이터를 조회##################
matchtype_url = "https://open.api.nexon.com/static/fconline/meta/matchtype.json"

# matchtype = requests.get(matchtype_url, headers = headers)

# matchtype_data = matchtype.json()

# print(matchtype_data)
matchtype_data = tools.get_data_with_api_json(matchtype_url)


##########선수 고유 식별자(spid) 메타데이터 조회#############
'''
해당 API는 Path 정보만 제공합니다. 별도 클라이언트를 통해 확인할 수 있습니다.
선수 고유 식별자는 시즌 아이디 (seasonid) 3자리 + 선수 아이디 (pid) 6자리로 구성되어 있습니다.
시즌 아이디는 /metadata/seasonid API로 조회할 수 있습니다.
'''
spid_url = "https://open.api.nexon.com/static/fconline/meta/spid.json"

# spid = requests.get(spid_url, headers = headers)

# spid_data = spid.json()

spid_data = tools.get_data_with_api_json(spid_url)

organized_data = defaultdict(lambda: {'pid': set(), 'seasonid': set()})
for entry in spid_data:
    player_id = str(entry['id'])
    season_id = player_id[:3]    # 앞 세자리가 시즌 번호
    unique_id = player_id[3:]    # 뒷 여섯자리가 선수 고유 번호
    name = entry['name']
    
    # 각 선수의 이름에 대해 고유 번호와 시즌 번호를 저장
    organized_data[name]['pid'].add(unique_id)
    organized_data[name]['seasonid'].add(season_id)

# # defaultdict를 일반 dictionary로 변환하고 결과 출력
# result = {name: {'pid': list(data['pid']), 'seasonid': list(data['seasonid'])} for name, data in organized_data.items()}
# #######result : '손흥민': {'pid': ['274967'], 'seasonid': ['811', '813']}와 같은 데이터들로 정리##############

#########선수 액션, 일반 이미지 불러오기###############
action_folder_path = './image/action'
normal_folder_path = './image/normal'
tools.get_images(action_folder_path, normal_folder_path, spid_data)
# for spid in spid_data:
#     action_image_url = "https://fco.dn.nexoncdn.co.kr/live/externalAssets/common/playersAction/p{id}.png".format(id = spid['id'])
#     normal_image_url = "https://fco.dn.nexoncdn.co.kr/live/externalAssets/common/players/p{id}.png".format(id = spid['id'])
    
#     action_image = requests.get(action_image_url, headers = headers)
#     normal_image = requests.get(normal_image_url, headers = headers)

#     if action_image.status_code == 200:
#         action_file_path = os.path.join(action_folder_path, f"{spid['id']}.png")
#         # 이미지 파일로 저장
#         with open(action_file_path, "wb") as file:
#             file.write(action_image.content)
#         print(f"이미지 저장 성공: {action_file_path}")
#     else:
#         print(f"이미지 저장 실패: {spid['id']}, HTTP 상태 코드: {action_image.status_code}")

#     if normal_image.status_code == 200:
#         normal_file_path = os.path.join(normal_folder_path, f"{spid['id']}.png")
#         # 이미지 파일로 저장
#         with open(normal_file_path, "wb") as file:
#             file.write(normal_image.content)
#         print(f"이미지 저장 성공: {normal_file_path}")
#     else:
#         print(f"이미지 저장 실패: {spid['id']}, HTTP 상태 코드: {normal_image.status_code}")

##########시즌 아이디(seasonId) 메타데이터 조회##############
'''
시즌 아이디는 선수가 속한 클래스를 나타냅니다.
'''
seasonid_url = "https://open.api.nexon.com/static/fconline/meta/seasonid.json"

# seasonid = requests.get(seasonid_url, headers = headers)

# seasonid_data = seasonid.json()
# print(seasonid_data)

seasonid_data = tools.get_data_with_api_json(seasonid_url)

##########선수 포지션(spposition) 메타데이터 조회############
'''
선수 포지션(spposition) 메타데이터를 조회합니다.
'''
spposition_url = "https://open.api.nexon.com/static/fconline/meta/spposition.json"

# spposition = requests.get(spposition_url, headers = headers)

# spposition_data = spposition.json()
# print(spposition_data)

spposition_data = tools.get_data_with_api_json(spposition_url)

##########등급 식별자(division) 메타데이터 조회#############
'''
등급 식별자(division) 메타데이터를 조회합니다.
'''
division_url = "https://open.api.nexon.com/static/fconline/meta/division.json"

# division = requests.get(division_url, headers = headers)

# division_data = division.json()
# print(division_data)
division_data = tools.get_data_with_api_json(division_url)

############볼타 공식경기 등급 식별자 메타데이터 조회#############
'''
볼타 공식경기의 등급 식별자(division) 메타데이터를 조회합니다.
'''
division_volta_url = "https://open.api.nexon.com/static/fconline/meta/division-volta.json"

# division_volta = requests.get(division_volta_url, headers = headers)

# division_volta_data = division_volta.json()
# print(division_volta_data)

division_volta_data = tools.get_data_with_api_json(division_volta_url)


tools.make_csv('matchtype.csv', matchtype_data)
tools.make_csv('spid.csv', spid_data)
tools.make_csv('seasonid.csv', seasonid_data)
tools.make_csv('spposition.csv', spposition_data)
tools.make_csv('division.csv', division_data)
tools.make_csv('division_volta.csv', division_volta_data)