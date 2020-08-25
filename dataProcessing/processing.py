# 이거는 전처리하는 코드들 모아놓은 파일로 쓰자 .

from time import sleep

def process_data(data) :
    print("~~ 데이터 전처리 함수를 실행합니다!")
    modified_data = data + "가 수정 완료 !"
    sleep(3)
    print(" 전처리 끝")
    return modified_data



# 이렇게 data 전처리 루틴한 일을 일케 해놓으면 되는거. 이 파일만 실행하면 알아서 data 전처리를 해주는 것이니까.