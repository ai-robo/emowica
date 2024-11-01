# Импортируем (добавляем) необходимые модули
import pyaudio
import requests
from speechkit import Session, SpeechSynthesis

# https://github.com/TikhonP/yandex-speechkit-lib-python

# Аутентификационная информация для работы с Яндекс СпичКит
oauth_token = ""
catalog_id = ""

# ============================ speechkit ============================
session = Session.from_yandex_passport_oauth_token(oauth_token, catalog_id)

# Создаем экземляр класса `SpeechSynthesis`, передавая `session`,
# который уже содержит нужный нам IAM-токен
# и другие необходимые для API реквизиты для входа
synthesizeAudio = SpeechSynthesis(session)

# ===================================================================
# Функция для воспроизведения аудио
def pyaudio_play_audio_function(audio_data, num_channels=1,
                                sample_rate=16000, chunk_size=5000) -> None:
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=num_channels,
        rate=sample_rate,
        output=True,
        frames_per_buffer=chunk_size
    )

    try:
        for i in range(0, len(audio_data), chunk_size):
            stream.write(audio_data[i:i + chunk_size])
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
# ===================================================================



def say_it(text):
    # synthesizeAudio.synthesize_stream - это функция из API speechkit
    # Голос, которым будет говорить наша программа. Все доступные голоса здесь: https://yandex.cloud/ru/docs/speechkit/tts/voices
    voice = 'zahar'
    sample_rate = 16000
    audio_data = synthesizeAudio.synthesize_stream(
                                text = text + '.  1',
                                voice = voice, format = 'lpcm', sampleRateHertz = sample_rate)
    pyaudio_play_audio_function(audio_data, sample_rate = 16000)
