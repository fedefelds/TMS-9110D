import parser

#Estos son los valores (redondeados) de frecuencia y amplitud sacados de la ISO-8041 para VSCE
freq_values_vsce = [1,1.259,1.995,3.981,7.943,15.85,31.62,63.10,79.43,125.9]#REDONDEAR
amp_values_vsce = [0.1, 0.3, 0.5, 0.8, 1, 2.5, 5, 7.5, 10, 25, 50]

#Estos son los valores (redondeados) de frecuencia y amplitud sacados de la ISO-8041 para VSMB
freq_values_vsmb = [5.012, 6.310, 7.943,10,15,85,7.943,31,62]#REDONDEAR
amp_values_vsmb = [5, 7.5, 10, 25, 75, 100]

#Estos son los valores custom
freq_values_custom = [1,1.259,1.995,3.981,7.943,15.85,31.62,63.10,79.43,125.9]
amp_values_custom = [30]

mode = 'vsce'

if mode == 'vsce':
    parser.pvc_parse(amp_values_vsce,freq_values_vsce)
elif mode == 'vsmb':
    parser.pvc_parse(amp_values_vsmb,freq_values_vsmb)
else:
    parser.pvc_parse(amp_values_custom,freq_values_custom)
