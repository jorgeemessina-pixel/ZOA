import speech_recognition as sr
import cv2

print("ZOA iniciada. Decí 'ZOA' para hablar o 'mirá esto ZOA' para foto")

r = sr.Recognizer()
mic = sr.Microphone()
cap = cv2.VideoCapture(0)

while True:
    with mic as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='es-ES')
        print("Escuché:", text)
        
        if "mirá esto ZOA" in text.lower():
            ret, frame = cap.read()
            cv2.imwrite("foto_zoa.jpg", frame)
            print("Foto tomada")
    except:
        pass
