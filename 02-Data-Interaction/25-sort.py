kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
['Pesawat', 'helikopter', 'mobil', 'motor']
"""

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

"""
Output:
 ['pesawat', 'motor', 'mobil', 'helikopter']

"""

urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
urutan.sort()

print(urutan)

"""
Output:
TypeError: '<' not supported between instances of 'int' and 'str'
"""