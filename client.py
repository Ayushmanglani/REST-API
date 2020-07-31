import requests

URL = "http://127.0.0.1:8000"

def get_token():
	url = "http://127.0.0.1:8000/api/auth/"
	response = requests.post(url, data={'username': 'DJANGO_ADMIN_USERNAME','password': 'DJANGO_ADMIN_PASSWORD'})
	# print(response.json())
	return response.json()

def get_data():
	url = "http://127.0.0.1:8000/api/info_list/"
	header = {'Authorization': f'Token {get_token()}'}
	response = requests.get(url, headers = header)
	emp_data = response.json()
	# print(emp_data)
	for e in emp_data:
		print(e)

def create_new():
	url = "http://127.0.0.1:8000/api/info_list/"
	header = {'Authorization': f'Token {get_token()}'}
	data = (
		{
		"employee_name": "Arpit",
        "employee_id": 7,
        "age": 22
        }
    )
	response = requests.post(url, data = data ,headers = header)
	print(response.text)

def update(employee_id):
	url = f"http://127.0.0.1:8000/api/info_list/{employee_id}/"
	header = {'Authorization': f'Token {get_token()}'}
	data = (
		{
		"age": 24
        }
    )
	response = requests.put(url, data = data ,headers = header)
	print(response.text)

def delete_data(employee_id):
	url = f"http://127.0.0.1:8000/api/info_list/{employee_id}/"
	header = {'Authorization': f'Token {get_token()}'}
	response = requests.delete(url,headers = header)
	print(response.status_code)
# create_new()
# get_data()
# update(7)
for e in range(3,7):
	delete_data(e)
