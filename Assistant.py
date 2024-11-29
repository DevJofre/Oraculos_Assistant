import speech_recognition as sr


def capturar_transcrever():

    reconhecedor = sr.Recognizer()

    with sr.Microphone() as source:
        print("Aguarde... ajustando microfone")
        reconhecedor.adjust_for_ambient_noise(source)
        print("Pode falar agora!")

    try:
        audio = reconhecedor.listen(source, timeout=5)
        print("Processando...")

        texto = reconhecendor.recognize_google(audio, language="pt-BR")
