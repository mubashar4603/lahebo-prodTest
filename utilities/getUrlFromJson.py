import json

# Open the JSON file
with open('/home/mubashar4603/PycharmProjects/Metutors/TestData/sdcoll.json', 'r') as f:
    data = json.load(f)
    req = data['variable'][0]['value']
    reqq = data['item'][0]['item'][3]['request']['url']['raw']
    print(reqq)






# Assuming the JSON structure contains an array of requests
# for item in data['item']:
#     print(item)
#     # Check if the item is a request
#     if 'request' in item:
#         # Extract the URL from the request
#         url = item['request']['url']
#         # Print the URL
#         print(url)