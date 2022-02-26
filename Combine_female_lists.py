# opens event lists and writes into new txt file

path = "/Users/newmac/Desktop/Programs and Code/"

filenames = [path + 'AUS_female_100m.txt', path + 'AUS_female_200m.txt', path + 'AUS_female_400m.txt', path + 'AUS_female_800m.txt', path + 'AUS_female_1500m.txt', path + 'AUS_female_3000msc.txt', path + 'AUS_female_5000m.txt', path + 'AUS_female_10000m.txt', path + 'AUS_female_100mh.txt', path + 'AUS_female_400mh.txt', path + 'AUS_female_long-jump.txt', path + 'AUS_female_triple-jump.txt', path + 'AUS_female_high-jump.txt', path + 'AUS_female_pole-vault.txt', path + 'AUS_female_discus-throw.txt', path + 'AUS_female_shot-put.txt', path + 'AUS_female_hammer-throw.txt', path + 'AUS_female_javelin-throw.txt', path + 'AUS_female_heptathlon.txt', path + 'AUS_female_race-walking.txt', path + 'AUS_female_marathon.txt']  # concatenate all events
with open('/Users/newmac/Desktop/Programs and Code/AUS_women_COMBINEDFILE.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line.replace(" : ", ":"))
