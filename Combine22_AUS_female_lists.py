# opens event lists and writes into new txt file
# this combines only the female event ranking data into 1 txt file 

path = "/Users/newmac/Desktop/Programs and Code/"

filenames = [path + 'AUS_female_22_100m_Toplist.txt', path + 'AUS_female_22_200m_Toplist.txt', path + 'AUS_female_22_400m_Toplist.txt', path + 'AUS_female_22_800m_Toplist.txt', path + 'AUS_female_22_1500m_Toplist.txt', path + 'AUS_female_22_3000msc_Toplist.txt', path + 'AUS_female_22_5000m_Toplist.txt', path + 'AUS_female_22_10000m_Toplist.txt', path + 'AUS_female_22_100mh_Toplist.txt', path + 'AUS_female_22_400mh_Toplist.txt', path + 'AUS_female_22_long-jump_Toplist.txt', path + 'AUS_female_22_triple-jump_Toplist.txt', path + 'AUS_female_22_high-jump_Toplist.txt', path + 'AUS_female_22_pole-vault_Toplist.txt', path + 'AUS_female_22_discus-throw_Toplist.txt', path + 'AUS_female_22_shot-put_Toplist.txt', path + 'AUS_female_22_hammer-throw_Toplist.txt', path + 'AUS_female_22_javelin-throw_Toplist.txt', path + 'AUS_female_22_race-walking_Toplist.txt', path + 'AUS_female_22_marathon_Toplist.txt']  # , path + 'AUS_female_22_heptathlon_Toplist.txt'
with open('/Users/newmac/Desktop/Programs and Code/AUS22_women_COMBINEDFILE_Toplist.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line.replace(" : ", ":"))
