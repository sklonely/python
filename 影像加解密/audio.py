# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave

NUM_SAMPLES = 2000  # pyAudio内部缓存的块的大小
SAMPLING_RATE = 8000  # 取样频率
LEVEL = 1500  # 声音保存的阈值
COUNT_NUM = 20  # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 8  # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样
TIME = 10


def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLING_RATE)
    wf.writeframes("".join(data))
    wf.close()


def my_record():
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=NUM_SAMPLES)
    my_buf = []
    count = 0
    while count < TIME * 20:  #控制錄音時間
        string_audio_data = stream.read(NUM_SAMPLES)  #一次性錄音取樣位元組大小
        my_buf.append(string_audio_data)
        count = 1
        print('.')
        save_wave_file('01.wav', my_buf)
        stream.close()


my_record()