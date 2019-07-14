import random


class person:

    def __init__(self, name, a, b):
        self.name = name
        self.str = a
        self.int = b

    def jobs(self):
        if a < b:
            job = '법사'
        elif a == b:
            job = '궁수'
        elif a > b:
            job = '전사'
        print('캐릭터 직업 : %s' % job)


name = input('캐릭터의 이름을 입력하세요.')
a = random.randint(6, 8)
b = random.randint(6, 8)
birth = person(name, a, b)
print('캐릭터 이름 :', birth.name)
print('캐릭터 정보 : ', '힘(', birth.str, ')', '지력(', birth.str, ')', sep='')
birth.jobs()
