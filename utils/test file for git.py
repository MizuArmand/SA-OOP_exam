"""
survey_date() - При обращении пользователя к какой-либо услуге формирует дату для опроса качеством сервиса по ней.
"""

import datetime

def survey_date():
    now = datetime.date.today()
    survey_d = now + datetime.timedelta(days=5)
    return (survey_d)  # дата для записи в базу данных

survey_date()

