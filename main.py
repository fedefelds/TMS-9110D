import pvc_parser

#Estos son los valores (redondeados) de frecuencia y amplitud sacados de la ISO-8041 para VSCE
freq_values_vsce = [1,1.259,1.995,3.981,7.943,15.85,31.62,63.10,79.43,125.9]#REDONDEAR
amp_values_vsce = [0.1, 0.3, 0.5, 0.8, 1, 2.5, 5, 7.5, 10, 25, 50]

#Estos son los valores (redondeados) de frecuencia y amplitud sacados de la ISO-8041 para VSMB
freq_values_vsmb = [5.012, 6.310, 7.943,10,15,85,7.943,31,62]#REDONDEAR
amp_values_vsmb = [5, 7.5, 10, 25, 75, 100]

#Estos son los valores custom
freq_values_custom1 = [1,1.26,1.58,2.00,2.51,3.16,3.98,5.01,6.31,7.94,10.00,12.59,15.85,19.95,25.12,31.62,39.81,50.12,63.10,79.43]
freq_values_custom2 = [100,125.9,158.5,199.5,251.2,316.2,398.1,501.2,631,794.3,1000,1259,1585,1995,2512,3162,3981]
amp_values_custom = [1,3,5,10]

mode = 'vsce'

if mode == 'vsce':
    pvc_parser.pvc_parse(amp_values_vsce,freq_values_vsce)
elif mode == 'vsmb':
    pvc_parser.pvc_parse(amp_values_vsmb,freq_values_vsmb)
elif mode == 'custom1':
    pvc_parser.pvc_parse(amp_values_custom,freq_values_custom1)
elif mode == 'custom2':
    pvc_parser.pvc_parse(amp_values_custom,freq_values_custom2)
