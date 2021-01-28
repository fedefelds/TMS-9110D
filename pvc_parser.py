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
    preamble = re.sub("yyy", 'RMS_'+str(amp_values[0]),preamble)
    
    return preamble
    
def pvc_parse(amp_values_iso,freq_values_iso):
    if len(freq_values_iso) <= 30 :
        for amplitud in amp_values_iso:
            Route_Point = 0
            amp_values = [0]
            # Estos son los valores de frecuencia y amplitud que uso en la rutina
            freq_values = freq_values_iso
            amp_values[0] = amplitud

            #Para el valor de amplitud elegido, parseo el string nuevo
            string = preamble_parse(freq_values_iso,amp_values)
            for amp in amp_values:
                for freq in freq_values:
                    string += '\n'
                    string += string_parse(freq,amp,Route_Point)
                    Route_Point += 1
            # agrego \n final
            string += '  \n'

            # Escribo el archivo .pvc
            filename = 'RMS_'+str(amp_values[0])+'.pvc'
            with open(filename, "w", newline='\r\n') as text_file:
                text_file.write(string)    
    else:
        print("El array de frecuencia no puede tener mas de 30 valores.")
