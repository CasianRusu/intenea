from scipy.io import wavfile
import math


def initialise_data(wav):
    # I extracted samplerate and data from audio file
    samplerate, data = wavfile.read(wav)
    return data


def rms_calcul(data):  # I calculated the rms basing on a math formula
    square = 0
    n = len(data)
    for i in range(0, n):
        square += int(data[i])**2
    mean = square / n
    root = math.sqrt(mean)
    return root


def dbs_calcul(root):
    # I computed the number of decibels using another math formula
    lvl_of_dbs = 20 * math.log10(root)
    print("The level of dbs has been successfully computed")
    return lvl_of_dbs


def writing_number_of_dbs(lvl_of_dbs):
    # I opened a text file, whose name is level_of_dbs.txt
    f = open("level_of_dbs.txt", "a")
    # I wrote the number of db in that file
    f.write("The level of dbs is: " + str(lvl_of_dbs) + '\n')
    f.close()


def dbs_script():
    data_list = initialise_data("recorded.wav")
    rms = rms_calcul(data_list)
    dbs = dbs_calcul(rms)
    written_dbs = writing_number_of_dbs(dbs)
