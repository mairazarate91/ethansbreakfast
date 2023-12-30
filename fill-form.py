import requests


def submit_form(url, data):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(url, headers=headers, data=data)

    print(f"Response Status Code: {response.status_code}")
    # print(response.text)


base_url = "https://docs.google.com/forms/d/e/1FAIpQLSfilkTHjMzIuJhM6A60wwWnb1wyxE10EmKI_xQcHHhXqdubnw/formResponse"

"""
entry.964807417=Weeks&entry.2050171288=5&entry.1507825071=Ethan+Sanabria&emailAddress=mairazarate91%40gmail.com&fvv=1&partialResponse=%5Bnull%2Cnull%2C%224127984135122189587%22%5D&pageHistory=0&fbzx=4127984135122189587&continue=1
"""

data_page_1 = {
  'entry.964807417': 'Weeks',
  'entry.2050171288': '5',
  'entry.1507825071': 'Ethan Sanabria',
  'emailAddress': 'mairazarate91@gmail.com',
  'fvv': '1',
  'partialResponse': '[null,null,"4127984135122189587"]',
  'pageHistory': '0',
  'fbzx': '4127984135122189587',
  'continue': '1',
}
"""
entry.1902733890=Yes&entry.1259698694=Yes&entry.2062094595=Yes&entry.495925828=Yes&entry.1373185085=Yes&entry.1675049274=Chocolate&entry.1902733890_sentinel=&entry.1259698694_sentinel=&entry.2062094595_sentinel=&entry.495925828_sentinel=&entry.1373185085_sentinel=&entry.1675049274_sentinel=&fvv=1&partialResponse=%5B%5B%5Bnull%2C964807417%2C%5B%22Weeks%22%5D%2C0%5D%2C%5Bnull%2C2050171288%2C%5B%225%22%5D%2C0%5D%2C%5Bnull%2C1507825071%2C%5B%22Ethan+Sanabria%22%5D%2C0%5D%5D%2Cnull%2C%224127984135122189587%22%2Cnull%2Cnull%2Cnull%2C%22mairazarate91%40gmail.com%22%2C1%5D&pageHistory=0%2C1&fbzx=4127984135122189587
"""
data_page_2 = {
    'entry.1902733890': 'Yes',
    'entry.1259698694': 'Yes',
    'entry.2062094595': 'Yes',
    'entry.495925828': 'Yes',
    'entry.1373185085': 'Yes',
    'entry.1675049274': 'Chocolate',
    'entry.1902733890_sentinel': '',
    'entry.1259698694_sentinel': '',
    'entry.2062094595_sentinel': '',
    'entry.495925828_sentinel': '',
    'entry.1373185085_sentinel': '',
    'entry.1675049274_sentinel': '',
    'fvv': '1',
    'partialResponse': '[[[null,964807417,["Weeks"],0],[null,2050171288,["5"],0],[null,1507825071,["Ethan Sanabria"],0]],null,"4127984135122189587",null,null,null,"mairazarate91@gmail.com",1]',
    'pageHistory': '0,1',
    'fbzx': '4127984135122189587',
}

submit_form(base_url, data_page_1)
submit_form(base_url, data_page_2)