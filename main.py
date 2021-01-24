import re
def string_parse(Frequency, Amplitude, Route_Point):
    Frequency_Unit = 'Hertz'
    Amplitude_Unit ='m/s2 RMS'
    Lower_Tolerance = 0
    Upper_Tolerance = 0
    Sensor_Type = 'Voltage'
    return (f'{Route_Point},{Frequency},{Frequency_Unit},{int(Amplitude*100)},'
            f'{Amplitude_Unit},{Lower_Tolerance},{Upper_Tolerance},'
            f'{Sensor_Type}')

def preamble_parse(freq_values,amp_values):
    preamble = """Route Points,Route Name
xxx,yyy
Test Sensor Model
ADXL-345






Route Point,Frequency,Frequency Unit,Amplitude,Amplitude Unit,Lower Tolerance,Upper Tolerance,Sensor Type"""
    #Defino cuantos Route Points hay a partir de freq_values
    preamble = re.sub("xxx", str(len(freq_values)), preamble)

    #Defino el nombre de la rutina a partir del valor rms elegido
    preamble = re.sub("yyy", 'RMS_'+str(amp_values[0])+"m/s2",preamble)
    
    return preamble
    
    

#Estos son los valores (redondeados) de frecuencia y amplitud sacados de la ISO-8041 
freq_values_iso = [1,1.259,1.995,3.981,7.943,15.85,31.62,63.10,79.43,125.9]
amp_values_iso = [0.1, 0.3, 0.5, 0.8, 1, 2.5, 5, 7.5, 10, 25, 50]

for amplitud in amp_values_iso:
    Route_Point = 0
    amp_values = [0]
    # Estos son los valores de frecuencia y amplitud que uso en la rutina
    freq_values = freq_values_iso
    amp_values[0] = amplitud

    



    # retocar aca
    string = preamble_parse(freq_values_iso,amp_values)
    for amp in amp_values:
        for freq in freq_values:
            string += '\n'
            string += string_parse(freq,amp,Route_Point)
            Route_Point += 1
    # agrego \n
    string += """  
"""
    # print(string)

    filename = 'RMS_'+str(amp_values[0])+'ms2.pvc'
    with open(filename, "w", newline='\r\n') as text_file:
        text_file.write(string)
