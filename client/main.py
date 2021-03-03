import requests
from include.config import user_url
import json


def intro():
    print()
    print()
    print("끝말잇기를 시작합니다.")


def user_check(username):
    """
    DB에 등록된 유저인지 확인
    :param username: 게임을 시작전 유저이름
    :return:
    """
    # TODO : else > user create
    info = requests.get(url=user_url + username)
    if info.text != "null":
        json_parsing = json.loads(info.text)
        print(json_parsing["point"])
    else:
        user_input = {"user_name": username}
        data = json.dumps(user_input)
        requests.post(url=user_url, data=data)
        print(f"환영합니다 {username}")


def main():
    intro()
    user = input("이름을 입력해주세요 : ")
    user_check(username=user)


if __name__ == '__main__':
    main()
