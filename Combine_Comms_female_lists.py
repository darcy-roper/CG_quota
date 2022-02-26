# opens event lists and writes into new txt file

path = "/Users/newmac/Desktop/NFT collection/Programs and Code/"

filenames = [path + 'AUS_female_100m_CommsRank.txt', path + 'AUS_female_200m_CommsRank.txt', path + 'AUS_female_400m_CommsRank.txt', path + 'AUS_female_800m_CommsRank.txt', path + 'AUS_female_1500m_CommsRank.txt', path + 'AUS_female_3000msc_CommsRank.txt', path + 'AUS_female_5000m_CommsRank.txt', path + 'AUS_female_10000m_CommsRank.txt', path + 'AUS_female_100mh_CommsRank.txt', path + 'AUS_female_400mh_CommsRank.txt', path + 'AUS_female_long-jump_CommsRank.txt', path + 'AUS_female_triple-jump_CommsRank.txt', path + 'AUS_female_high-jump_CommsRank.txt', path + 'AUS_female_pole-vault_CommsRank.txt', path + 'AUS_female_discus-throw_CommsRank.txt', path + 'AUS_female_shot-put_CommsRank.txt', path + 'AUS_female_hammer-throw_CommsRank.txt', path + 'AUS_female_javelin-throw_CommsRank.txt', path + 'AUS_female_heptathlon_CommsRank.txt', path + 'AUS_female_race-walking_CommsRank.txt', path + 'AUS_female_marathon_CommsRank.txt']  # concatenate all events
with open('/Users/newmac/Desktop/NFT collection/Programs and Code/COMMS_women_COMBINEDFILE.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line.replace(" : ", ":"))
