# opens event lists and writed into new txt file
# this combines only the male event ranking data into 1 txt file 

path = "/Users/newmac/Desktop/Programs and Code/"

filenames = [path + 'AUS_male_100m.txt', path + 'AUS_male_200m.txt', path + 'AUS_male_400m.txt', path + 'AUS_male_800m.txt', path + 'AUS_male_1500m.txt', path + 'AUS_male_3000msc.txt', path + 'AUS_male_5000m.txt', path + 'AUS_male_10000m.txt', path + 'AUS_male_110mh.txt', path + 'AUS_male_400mh.txt', path + 'AUS_male_long-jump.txt', path + 'AUS_male_triple-jump.txt', path + 'AUS_male_high-jump.txt', path + 'AUS_male_pole-vault.txt', path + 'AUS_male_discus-throw.txt', path + 'AUS_male_shot-put.txt', path + 'AUS_male_hammer-throw.txt', path + 'AUS_male_javelin-throw.txt', path + 'AUS_male_decathlon.txt', path + 'AUS_male_20km-race-walking.txt', path + 'AUS_male_marathon.txt']  # concatenate all events
with open('/Users/newmac/Desktop/Programs and Code/AUS_men_COMBINEDFILE.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line.replace(" : ", ":"))
