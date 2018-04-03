celsius=20
fahrenheit = celsius * 9 / 5 + 32
formatted = '{t} celsius is equal to {f} fahrenheit\n'.format(t=celsius, f=fahrenheit)

print(formatted)

id = "IAD"
location = "Dulles Intl Airport"
max_temp = 32
min_temp = 13
precipitation = 0.4

print('{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format(id=id,
                                                                                               location=location,
                                                                                               max_temp=max_temp,
                                                                                               min_temp=min_temp,
                                                                                               precipitation=precipitation))

data = dict(id=id, location=location, max_temp=max_temp, min_temp=min_temp, precipitation=precipitation)

print('{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(data))

# vars() create a dictionary from all local variables
print('{id:3s} : {location:19s} : {max_temp:3d} / {min_temp:3d} / {precipitation:5.2f}'.format_map(vars()))
