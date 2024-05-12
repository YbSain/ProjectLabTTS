import speech_recognition as sr
import pyttsx3

output_file = "information.mp3"
output_file2 = "output.mp3"
def text_to_speech(text, output_file):
    # pyttsx3 엔진 초기화
    engine = pyttsx3.init()

    # 텍스트를 음성으로 변환하여 파일에 저장
    engine.save_to_file(text, output_file)

    # 변환 작업 수행
    engine.runAndWait()

r = sr.Recognizer()
def listen_and_convert():
    with sr.Microphone() as source:
        input_text = "마이크에 입을 대고 말을 하시오."
        text_to_speech(input_text, output_file)
        r.adjust_for_ambient_noise(source, duration = 0.5)
        audio = r.listen(source)
    try:
        print("Recognizing. . .")
        text = r.recognize_google(audio)
        text_to_speech(text, output_file2)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from google Web Speech API; {0}".format(e))

listen_and_convert()
