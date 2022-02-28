# opens event lists and writes into new txt file
# this combines only the female event ranking data into 1 txt file 

path = "/Users/newmac/Desktop/Programs and Code/"

filenames = [path + 'AUS_female_21_100m_Toplist.txt', path + 'AUS_female_21_200m_Toplist.txt', path + 'AUS_female_21_400m_Toplist.txt', path + 'AUS_female_21_800m_Toplist.txt', path + 'AUS_female_21_1500m_Toplist.txt', path + 'AUS_female_21_3000msc_Toplist.txt', path + 'AUS_female_21_5000m_Toplist.txt', path + 'AUS_female_21_10000m_Toplist.txt', path + 'AUS_female_21_100mh_Toplist.txt', path + 'AUS_female_21_400mh_Toplist.txt', path + 'AUS_female_21_long-jump_Toplist.txt', path + 'AUS_female_21_triple-jump_Toplist.txt', path + 'AUS_female_21_high-jump_Toplist.txt', path + 'AUS_female_21_pole-vault_Toplist.txt', path + 'AUS_female_21_discus-throw_Toplist.txt', path + 'AUS_female_21_shot-put_Toplist.txt', path + 'AUS_female_21_hammer-throw_Toplist.txt', path + 'AUS_female_21_javelin-throw_Toplist.txt', path + 'AUS_female_21_race-walking_Toplist.txt', path + 'AUS_female_21_marathon_Toplist.txt']  # , path + 'AUS_female_21_heptathlon_Toplist.txt'
with open('/Users/newmac/Desktop/Programs and Code/AUS21_women_COMBINEDFILE_Toplist.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line.replace(" : ", ":"))
