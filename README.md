# ko-kr_word
* ## API를 이용한 한국어 끝말잇기 입니다.
* ## 모든 단어는 word.sqlite DataBase를 기준으로 합니다
## Created by Demi 2021-03-06
---
## Version
> ##  python == 3.8.5

---

## Package Install
> ## pip install -r requirements.txt

## How do?
> ## 1. ~backend\ $ uvicorn api:app
> ## 2. ~client\ $ python game.py --start
> ## 3. enjoy!

---
## MANUAL
> ## 1. 점수는 기본점수 5점 + 단어의 길이마다 1점입니다.
> ## 2. 기회는 총 3번 이며 다음과 같은 상황마다 소진됩니다.
>> * 같은 단어를 반복 하였을때
>> * 입력한 단어가 DB상에 존재하지 않을때
>> * 앞서 말한 단어의 끝과 입력한 단어의 시작이 다를때

---
# ETC..
> ## 순위보기 
>> ### ~client\ $ python game.py --rank

