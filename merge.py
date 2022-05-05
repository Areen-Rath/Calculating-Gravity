import csv

headers = ["Name", "Distance", "Mass", "Radius"]

with open('brightest.csv', 'r') as f:
    reader = csv.reader(f)
    brightest_star_data = list(reader)[1:]

with open('brown_dwarfs.csv', 'r') as f:
    reader = csv.reader(f)
    brown_dwarf_star_data = list(reader)[1:]

for star in brightest_star_data:
    if star == []:
        brightest_star_data.remove(star)

for star in brown_dwarf_star_data:
    if star == []:
        brown_dwarf_star_data.remove(star)

for star in brown_dwarf_star_data:
    star[3] = float(star[3]) * 0.102763
    star[2] = float(star[2]) * 0.0009954588

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for star in brightest_star_data:
        writer.writerow(star)
    for star in brown_dwarf_star_data:
        writer.writerow(star)