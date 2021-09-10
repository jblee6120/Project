import pyzbar.pyzbar as pyzbar
import cv2
import time
import pyautogui
# import playsound
#pyautogui모듈은 웹 ui에 자동으로 입력하기 위한 모듈

cap = cv2.VideoCapture(1)

# 바코드 정보 저장 객체
data_list = []

my_code = ""

while True:
    success, frame = cap.read()

    if success:
        cv2.imshow('cam', frame)
        key = cv2.waitKey(1)
        # ESC 키를 누르면 나가기
        if key == 27:
            break

        for code in pyzbar.decode(frame):
            my_code = code.data.decode('utf-8')

            if my_code not in data_list:

                data_list.append(my_code)
                # 실제 구동 시 주석 처리
                print(my_code)

                # 비프음~~~

                time.sleep(2)

                # DB에서 데이터 불러오고 UI에 정보 제공하는 코드
                pyautogui.write(my_code)
                pyautogui.press('enter')
            else:
                print("이미 인식된 코드입니다.")
                print(data_list)
                time.sleep(2)

                # 비프음 ~~~

cap.release()
cv2.destroyAllWindows()