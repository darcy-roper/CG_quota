# opens event lists and writes into new txt file
# this combines only the female comms ranking data into 1 txt file 

path = "/Users/newmac/Desktop/Programs and Code/"

filenames = [path + 'Toplist22_female_100m_CommsRank.txt', path + 'Toplist22_female_200m_CommsRank.txt', path + 'Toplist22_female_400m_CommsRank.txt', path + 'Toplist22_female_800m_CommsRank.txt', path + 'Toplist22_female_1500m_CommsRank.txt', path + 'Toplist22_female_3000msc_CommsRank.txt', path + 'Toplist22_female_5000m_CommsRank.txt', path + 'Toplist22_female_10000m_CommsRank.txt', path + 'Toplist22_female_100mh_CommsRank.txt', path + 'Toplist22_female_400mh_CommsRank.txt', path + 'Toplist22_female_long-jump_CommsRank.txt', path + 'Toplist22_female_triple-jump_CommsRank.txt', path + 'Toplist22_female_high-jump_CommsRank.txt', path + 'Toplist22_female_pole-vault_CommsRank.txt', path + 'Toplist22_female_discus-throw_CommsRank.txt', path + 'Toplist22_female_shot-put_CommsRank.txt', path + 'Toplist22_female_hammer-throw_CommsRank.txt', path + 'Toplist22_female_javelin-throw_CommsRank.txt', path + 'Toplist22_female_race-walking_CommsRank.txt', path + 'Toplist22_female_marathon_CommsRank.txt']  # concatenate all events # add path + 'Toplist22_female_heptathlon_CommsRank.txt' once hep included
with open('/Users/newmac/Desktop/Programs and Code/COMMS22_female_COMBINEDFILE.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line.replace(" : ", ":"))
