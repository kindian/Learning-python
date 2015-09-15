def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOErroe as ioerr:
        print('File error: ' +str(ioerr))
        return(None)

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

james_data = {}
james_data['Name'] = james.pop(0)
james_data['DOB'] = james.pop(0) 
james_data['Times'] = james

julie_data = {}
julie_data['Name'] = julie.pop(0)
julie_data['DOB'] = julie.pop(0) 
julie_data['Times'] = julie

mikey_data = {}
mikey_data['Name'] = mikey.pop(0)
mikey_data['DOB'] = mikey.pop(0) 
mikey_data['Times'] = mikey

sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0) 
sarah_data['Times'] = sarah


print(james_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in james_data['Times']]))[0:3]))
print(julie_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in julie_data['Times']]))[0:3]))
print(mikey_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in mikey_data['Times']]))[0:3]))
print(sarah_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
