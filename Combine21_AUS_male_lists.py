# opens event lists and writes into new txt file
# this combines only the male event ranking data into 1 txt file 

path = "/Users/newmac/Desktop/Programs and Code/"

filenames = [path + 'AUS_male_21_100m_Toplist.txt', path + 'AUS_male_21_200m_Toplist.txt', path + 'AUS_male_21_400m_Toplist.txt', path + 'AUS_male_21_800m_Toplist.txt', path + 'AUS_male_21_1500m_Toplist.txt', path + 'AUS_male_21_3000msc_Toplist.txt', path + 'AUS_male_21_5000m_Toplist.txt', path + 'AUS_male_21_10000m_Toplist.txt', path + 'AUS_male_21_110mh_Toplist.txt', path + 'AUS_male_21_400mh_Toplist.txt', path + 'AUS_male_21_long-jump_Toplist.txt', path + 'AUS_male_21_triple-jump_Toplist.txt', path + 'AUS_male_21_high-jump_Toplist.txt', path + 'AUS_male_21_pole-vault_Toplist.txt', path + 'AUS_male_21_discus-throw_Toplist.txt', path + 'AUS_male_21_shot-put_Toplist.txt', path + 'AUS_male_21_hammer-throw_Toplist.txt', path + 'AUS_male_21_javelin-throw_Toplist.txt', path + 'AUS_male_21_20km-race-walking_Toplist.txt', path + 'AUS_male_21_marathon_Toplist.txt']  # , path + 'AUS_male_21_decathlon_Toplist.txt'
with open('/Users/newmac/Desktop/Programs and Code/AUS21_male_COMBINEDFILE_Toplist.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line.replace(" : ", ":"))
