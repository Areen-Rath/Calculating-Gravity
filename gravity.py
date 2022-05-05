import csv

headers = ["Name", "Distance", "Mass", "Radius", "Gravity"]

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)[1:]

star_gravity = []

def gravity(star):
    gravity = star[2]/star[3] * 6.674e-11
    star_gravity.append(gravity)

for index, star in enumerate(data):
    if star != []:
        star[2] = star[2] * 1.989e+30
        star[3] = star[3] * 6.957e+8
        gravity(star)
        star.append(star_gravity[index])
    else:
        data.remove(star)

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for star in data:
        writer.writerow(star)