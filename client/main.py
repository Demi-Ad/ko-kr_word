import requests
from include.config import user_url, word_url, check_url
import json
from urllib import parse
from random import randint
from typing import Union


class Game:
    """
    기반 클래스
    """
    word_result = []  # 서로 대답한 단어
    call_word_list = []  # API 에 호출한 단어리스트

    def call_word(self, word: str):
        """
        API로 단어 저장
        :param word: API에 호출할 단어
        :return:
        """
        self.call_word_list.clear()
        word_call = requests.get(url=word_url + parse.quote(word)).json()
        for i in word_call:
            self.call_word_list.append(i)

    @staticmethod
    def intro():
        print("안녕하세요 끝말잇기에 오신걸 환영합니다")
        print("규칙은 다음과 같습니다")
        print("1.단어는 DB에 등록된 단어를 기준으로 합니다")
        print("2.점수는 기본점수 5점 + 단어의 길이 마다 1점씩")
        print("3.레드 카드는 총 3번 입니다")
        print("끝말잇기를 시작합니다.")


class Player(Game):
    """
    플레이어
    """
    red_card = 0  # 사용자가 실수 했을때 올릴 변수

    def __init__(self, username: str):
        self.user = username
        self.point: int = 0

    def user_check(self):
        """
        DB에 등록된 유저인지 확인
        :param self: 게임을 시작전 유저이름
        :return:
        """
        info = requests.get(url=user_url + self.user)
        if info.text != "null":
            json_parsing = json.loads(info.text)
            print("또 보니 반가워요 {0} 가장 높은 점수는 {1}이에요".format(json_parsing["user_name"],
                                                          json_parsing["point"]))
        else:
            user_input = {"user_name": self.user}
            data = json.dumps(user_input)
            requests.post(url=user_url, data=data)
            print(f"환영합니다 {self.user}")

    def word_speak(self, speak_word: str) -> Union[str, bool]:
        """
        :param speak_word: 유저가 말한 단어
        :returns: str, bool
        """
        if speak_word not in self.word_result:  # 말한적이 없다면
            word_check = requests.get(url=check_url + parse.quote(speak_word)).text  # 유저가 말한 단어가 DB에 등록되있는지 확인
            if word_check == "true":  # 등록 되있다면
                self.word_result.append(speak_word)
                return speak_word[-1]
            else:
                self.red_card += 1
                print("그런말은 없네요")
                return False
        else:
            print("이미 말햇어요")
            self.red_card += 1
            return False

    def update_point(self):
        print(f"이번 게임에 점수는... {self.point}입니다!")
        requests.put(url=user_url + self.user + "/" + str(self.point))


class Pc(Game):
    """
    PC
    """
    def speck(self) -> str:
        """
        Pc가 대답 할 때
        :return: 대답한 단어에 마지막 어절
        """
        answer = self.call_word_list[randint(0, len(self.call_word_list) - 1)]["WORD"]
        self.word_result.append(answer)
        print(answer)
        return answer[-1]


def main() -> None:
    """
    메인함수
    :return: None
    """
    base_point = 5  # 기본 점수
    answer = None
    Game.intro()  # 게임 시작 인트로
    input_user = input("당신의 이름을 알려주세요 : ")
    player = Player(username=input_user)
    pc = Pc()
    player.user_check()

    while True:
        if player.red_card == 3:
            player.update_point()
            break
        input_word = input("단어 : ")
        if len(input_word) == 0:
            print("공백은 안되요!")
            continue
        else:
            pass
        if answer is None:
            pass
        else:
            if answer != input_word[0]:
                print("마지막 말이랑 달라요")
                player.red_card += 1
                continue
        user_speck = player.word_speak(speak_word=input_word)
        if not user_speck:
            continue
        player.call_word(word=input_word)
        player.point += (base_point + len(input_word))
        answer = pc.speck()


if __name__ == '__main__':
    main()
