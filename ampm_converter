def ampm_to_24h(x):
    
    '''This functions convert a non-zero padding 12 hour AM/PM string format to 
    an 24 hours militar datetime (H:M:S) string ready to convert to datetime type'''
    
    dia, hora, am_pm = x.split()
    hora = hora.split(":")[0]
    hora = '{0:0>2}'.format(hora)
    
    if (hora == '12') and (am_pm == 'AM'):
        
        hora = '00'
    
    elif (hora != '12') and (am_pm == 'PM'):
        
        hora = str(int(hora)+12)
        
    date_time = f'{dia} {hora}:00:00'
    
    return date_time
