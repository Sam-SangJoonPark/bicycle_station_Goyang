# main py에서 calculation.py 불러오기
# calculation에서 함수 짜 놓았으니, main에서 이걸 쓰기

import calculation as cal


# 이거는 arithmetic이라는 다른 폴더에서 불러오니까 from 쓴다! 우리 패키지 불러오는거랑 비슷.
from arithmetic import plus
from arithmetic import subtract
from dataProcessing import importData
from dataProcessing import processing


a = 3
b = 4


def main() :
    print("안녕하세요")
    print("a +b = ", plus.add(a,b))
    print("a -b = ", subtract.minus(a,b))


if __name__ == "__main__" :     # 이거는 main파일에 꼭 있어야 실행되는 거임
    main()


# 또,  데이터 전처리 시작!  -- processing.py에서 불러옴

data = importData.readDㅎㄹata()
processing.process_data(data)




#### Terminal창은 cmd창 같은건데 , python main.py 일케 치면 main.py를 실행함.





