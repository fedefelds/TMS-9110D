import parser

#Estos son los valores (redondeados) de frecuencia y amplitud sacados de la ISO-8041 
freq_values_iso = [1,1.259,1.995,3.981,7.943,15.85,31.62,63.10,79.43,125.9]
amp_values_iso = [0.1, 0.3, 0.5, 0.8, 1, 2.5, 5, 7.5, 10, 25, 50]

parser.pvc_parse(amp_values_iso,freq_values_iso)