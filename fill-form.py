import requests

def submit_form(url, data):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(url, headers=headers, data=data)

    print(f"Response Status Code: {response.status_code}")
    # print(response.text)


base_url = "https://docs.google.com/forms/d/e/1FAIpQLSdaUfE4Sz7xWC2TsZ0bNMbNd3_JpSnIXxGCAQcwfLqnqJnpow/formResponse"

data_page_1 = {
'entry.2037705817': 'mairazarate91@gmail.com',
'entry.609658634': 'Weeks',
'entry.1708870756': '5',
'entry.1693956301': 'Ethan Sanabria',
'fvv': '1',
'partialResponse': '[null,null,"-8880704152920510830"]',
'pageHistory': '0',
'fbzx': '-8880704152920510830',
'continue': '1',
}

data_page_2 = {
'entry.742638120': 'Yes',
'entry.407070387': 'Yes',
'entry.570786258': 'Yes',
'entry.1871733372': 'Yes',
'entry.2109921311': 'Yes',
'entry.742638120_sentinel': '',
'entry.407070387_sentinel': '',
'entry.570786258_sentinel': '',
'entry.1871733372_sentinel': '',
'entry.2109921311_sentinel': '',
'fvv': '1',
'partialResponse': '[[[null,2037705817,["mairazarate91@gmail.com"],0],[null,609658634,["Weeks"],0],[null,1708870756,["5"],0],[null,1693956301,["Ethan Sanabria"],0]],null,"-8880704152920510830"]',
'pageHistory': '0,1',
'fbzx': '-8880704152920510830',
}

submit_form(base_url, data_page_1)
submit_form(base_url, data_page_2)