# -*- ecoding=utf-8 -*-
# Author:Chen Bolin


import requests


url = 'https://api.codemao.cn/tiger/wood/user/works?'
headers = {'Content-Type': 'application/json',
           'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozNzgzOTIsInVzZXJfdHlwZSI6InN0dWRlbnQiLCJqdGkiOiJlY2Y3Y2U2MC05YjFlLTQ2YjctOTI4Ni01OGIxM2I1MjdhYTMiLCJpYXQiOjE1NDYxNzEzMjl9.U1Y7zk_TGliOHmfK1pepa2NdOISrMgSZQjZ-uMNEg0s'}

para = {
	'language_type': 1,
	'limit': 15,
	'page': 1
}

res = requests.get(url=url, headers=headers, params=para)
print(res.status_code)