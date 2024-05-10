import pyttsx3

def text_to_speech(text, output_file):
    # pyttsx3 엔진 초기화
    engine = pyttsx3.init()

    # 텍스트를 음성으로 변환하여 파일에 저장
    engine.save_to_file(text, output_file)

    # 변환 작업 수행
    engine.runAndWait()

# 텍스트 입력
input_text = "안녕하세요, 반갑습니다."

# 출력 파일 설정
output_file = "output.mp3"

# 텍스트를 음성으로 변환
text_to_speech(input_text, output_file)