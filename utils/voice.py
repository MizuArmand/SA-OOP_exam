import pyttsx3

def dub(string: str) -> bool:

    """
    Озвучивание

    :param string: строка
    :return:
    """
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()

    return True
