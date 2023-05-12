import pandas as pd

NOTES = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'] #NOTES index from 0 : 11


n = int(3) #root note (The note that scale is started with) and also it'll work as a pointer to NOTES
scale_name = "major" #name of the scale from dataset

data = pd.read_csv("music_scales.csv")
data = data.fillna(0)


def scale_finder(n, scale_name):
    
    DISTANCE = data[scale_name].values.tolist()
    scale = str()

    for i in range(len(DISTANCE)):
            if n > len(NOTES) - 1:
                n = n - len(NOTES)
                scale = scale + NOTES[n]
            else:
                scale = scale + NOTES[n] 
            n = n + int(DISTANCE[i])


            
    return scale