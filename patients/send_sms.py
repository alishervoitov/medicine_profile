import requests
def send_sms(phone_number, message):
    url = "http://notify.eskiz.uz/api/message/sms/send"

    payload={'mobile_phone': phone_number,
             'message': message,
             'from': '4546',
             'callback_url': 'http://0000.uz/test.php'}
    files=[

    ]
    headers = {
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjUsInJvbGUiOiJ1c2VyIiwiZGF0YSI6eyJpZCI6NSwibmFtZSI6Ilx1MDQyN1x1MDQxZiBCZXN0IEludGVybmV0IFNvbHV0aW9uIiwiZW1haWwiOiJ0ZXN0QGVza2l6LnV6Iiwicm9sZSI6InVzZXIiLCJhcGlfdG9rZW4iOm51bGwsInN0YXR1cyI6ImFjdGl2ZSIsInNtc19hcGlfbG9naW4iOiJlc2tpejIiLCJzbXNfYXBpX3Bhc3N3b3JkIjoiZSQkayF6IiwidXpfcHJpY2UiOjUwLCJiYWxhbmNlIjoxNzkwMCwiaXNfdmlwIjowLCJob3N0Ijoic2VydmVyMSIsImNyZWF0ZWRfYXQiOm51bGwsInVwZGF0ZWRfYXQiOiIyMDIyLTA3LTAzVDE5OjE1OjA0LjAwMDAwMFoifSwiaWF0IjoxNjU2OTM4OTM3LCJleHAiOjE2NTk1MzA5Mzd9.XWdhbmyQBJtouTcLm1s0Q2cdhSZWKICdKlPDRh_mCFE'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)