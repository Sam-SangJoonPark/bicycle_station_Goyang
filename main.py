# main py에서 calculation.py 불러오기
# calculation에서 함수 짜 놓았으니, main에서 이걸 쓰기


import calculation as cal
a = 3
b = 4


def main() :
    print("안녕하세요")
    print("a+b = ", cal.substract(a, b))
    print("a-b", cal.plus(a, b))








