import requests, re


def email_validate(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)


def get_users():
    responce = requests.get('https://reqres.in/api/users?page=2', )
    users = responce.json()['data']
    res = []
    for user in users:
        if None not in [user['id'], user['email'], user['first_name'], user['first_name'], user['avatar']] and email_validate(user['email']):
            res.append(True)
        else:
            res.append(False)
    return res


def post_request():
    request_body = {
    "name": "morpheus",
    "job": "leader"
    }
    response = requests.post('https://reqres.in/api/users?page=2', json=request_body).json()
    return True if response['name'] == request_body['name'] and response['job'] == request_body['job'] else False



