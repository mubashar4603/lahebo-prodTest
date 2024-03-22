import requests
# import json
# import pandas as pd
# import excelutils

# url = "https://2iwu10oltb.execute-api.ap-southeast-2.amazonaws.com/staging/legislation/acts"
url = "https://wevmqe5p4i.execute-api.ap-southeast-2.amazonaws.com/prod/auth/login"

payload = {"username":"ElizabethHucker","password":"Marcus3004$"}

headers = {}




# headers = { "Authorization": "Bearer ""eyJraWQiOiI2bnRqVGR5aWJ4OVFmdGNPeThOYTQ2NXpuSXc3ekpPeWFvVm5iNE1CXC83ST0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxYjZhNThlZi0zNGE3LTQwZDMtODNmOC1jMTlkYTkyNGVhNzQiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoZWFzdC0yLmFtYXpvbmF3cy5jb21cL2FwLXNvdXRoZWFzdC0yX0MxS1Zvb2ljSSIsImNvZ25pdG86dXNlcm5hbWUiOiJQcmFzaGFudFNoYXJtYSIsIm9yaWdpbl9qdGkiOiI5YTE4MjUzMy1hNTYzLTQ0NjItOTBjNi04Y2U1MjUxZjg1NTgiLCJhdWQiOiIxbGIzMGpvM2R1YTk2dWY1bDNrcjI3cGczbiIsImV2ZW50X2lkIjoiNjBmOGUwMmUtZDZjZS00ZmM0LWI1NDMtOTBjZDcxMjFjYjgwIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE3MDg0MzU0NzksImV4cCI6MTcwODUyMTg3OSwiaWF0IjoxNzA4NDM1NDc5LCJqdGkiOiJkNGY0M2ExZS0wY2ViLTRlOWEtOTI2My05ZTkzNWEyZmYyNWQiLCJlbWFpbCI6InN1cHBvcnQrNjU0NjE2MkBsYWhlYm8uY29tIn0.BvULJjPm7EXUJc1EbDyYtFUx5q0x7WBG3BTKW56EVBoBM5fAwg0IYQwY08jSSuSoeqZsSOkj1L_i6MEnsmuPX3ISrzWKxweDdlAXXABsxTtVMApbuN8oiVnsr1iCgrxWDURkytzfJ6pE4TAd1uDwxAet8aFH9JVAdTpeHocU5y9rkkAsPOQ9bFu8_DVqvhfrR_xSLrD7eWUlpTmaf6WxkYOAddr_GoJfWgiK6R-D0Z4ljfCALW1DEn5Y1KbxF3hv-P4U9vJ9Zn0D9ZIvB3o5f34e0wSkIFoCQ4MHuIT8zSm8eFQE9XyPxe_Td_DIKAwCBiy9ekY3IAYkJnsfmAVOqw"}

response_data = requests.post(url, headers=headers, data=payload)

# myjson = response_data.json()
# print('resss:',myjson)

# req_data = []
if response_data.status_code == 201:
    # Extract the bearer token from the response
    token = response_data.json()["idToken"]["jwtToken"]
    print(token)
else:
    # If the request failed, print the error message
    print("Error:", response_data.text)
    print("Response code is not 200, API failed")





# for x in myjson["records"]:
#     json_data = x["legislation"]["name"]
#     req_data.append([json_data])
#
# print(req_data)