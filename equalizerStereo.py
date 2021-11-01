from scipy.io.wavfile import write, read
import numpy as np
from scipy.fft import fft , ifft,  fftfreq


freq, input_samples = read("TestSound.wav")


mono_sample = np.zeros(shape=(len(input_samples)), dtype=np.int16)

for i in range(len(input_samples)):
    mono_sample[i] =  input_samples[i][0]


fft_input = fft(mono_sample)

N = mono_sample.size

sample_freq = fftfreq(N , 1 / freq)


for i in range(len(sample_freq)):


    if abs(sample_freq[i]) <= 63:
        fft_input[i] = fft_input[i] * 1
    
    elif 63 < abs(sample_freq[i]) <= 125:
        fft_input[i] = fft_input[i] * 1
        
    elif 125 < abs(sample_freq[i]) <= 250:
        fft_input[i] = fft_input[i] * 1
        
    elif 250 < abs(sample_freq[i]) <= 500:
        fft_input[i] = fft_input[i] * 1
       
    elif 500 < abs(sample_freq[i]) <= 1000:
        fft_input[i] = fft_input[i] * 1
        
    elif 1000 < abs(sample_freq[i]) <= 2000:
        fft_input[i] = fft_input[i] * 1

    elif 2000 < abs(sample_freq[i]) <= 4000:
        fft_input[i] = fft_input[i] * 1

    elif 4000 < abs(sample_freq[i]) <= 8000:
        fft_input[i] = fft_input[i] * 1

    elif 8000 < abs(sample_freq[i]) <= 16000:
        fft_input[i] = fft_input[i] * 1 



output_comp = ifft(fft_input)
output = np.zeros(shape=(len(output_comp)), dtype=np.int16)

for i in range(len(output_comp)):
    output[i] = output_comp[i].real

   
write("TestSoundMono.wav", freq, output)


