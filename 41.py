#특별한 상황일 때 함수를 빠져나가고 싶다면 ==>return 단독 사용

def say_nick(nick):
    if nick == "바보":
         return
    print("나의 별명은 %s입니다." % nick)

say_nick('야호')
say_nick('바보')

#이렇게 하면 가능!
