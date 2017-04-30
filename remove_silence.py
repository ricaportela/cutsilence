from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
[Fs, x] = aIO.readAudioFile("/home/ricardo/projetos/matlibaudio/teste3.wav")
segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, Weight = 0.3, plot = True)

#[Fs, x] = audioBasicIO.readAudioFile("/home/ricardo/projetos/matlibaudio/teste.wav");
#duration = x.shape[0] / float(Fs)               
#t1 = time.clock()
#[Fs, x] = audioBasicIO.readAudioFile("/home/ricardo/projetos/matlibaudio/teste.wav");
#segments = aS.silenceRemoval(x, Fs, 0.050, 0.050, smoothWindow = 1.0, Weight = 0.3, plot = False)
#t2 = time.clock()
#perTime1 =  duration / (t2-t1); print "Silence removal \t {0:.1f} x realtime".format(perTime1)
