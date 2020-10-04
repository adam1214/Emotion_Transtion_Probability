import joblib
def emo_trans_prob(emo_dict):
    # only estimate anger, happiness, neutral, sadness
    total_transit = 0

    ang2ang = 0
    ang2hap = 0
    ang2neu = 0
    ang2sad = 0
    
    hap2ang = 0
    hap2hap = 0
    hap2neu = 0
    hap2sad = 0

    neu2ang = 0
    neu2hap = 0
    neu2neu = 0
    neu2sad = 0

    sad2ang = 0
    sad2hap = 0
    sad2neu = 0
    sad2sad = 0

    pre_emo = ''
    pre_dialog_id = ''

    for utt in emo_dict.keys():
        dialog_id = utt[0:-5]

        if emo_dict[utt] != 'ang' and emo_dict[utt] != 'hap' and emo_dict[utt] != 'neu' and emo_dict[utt] != 'sad': 
            # only estimate anger, happiness, neutral, sadness
            pre_dialog_id = dialog_id
            continue

        if pre_emo == '' and pre_dialog_id == '': #begining of the traversal
            pre_emo = emo_dict[utt]
            pre_dialog_id = dialog_id
            total_transit += 1
            continue

        if pre_dialog_id != dialog_id: #new dialog
            total_transit -= 1
            pre_emo = ''

        if pre_emo == 'ang' and emo_dict[utt] == 'ang':
            ang2ang += 1
        if pre_emo == 'ang' and emo_dict[utt] == 'hap':
            ang2hap += 1
        if pre_emo == 'ang' and emo_dict[utt] == 'neu':
            ang2neu += 1
        if pre_emo == 'ang' and emo_dict[utt] == 'sad':
            ang2sad += 1

        if pre_emo == 'hap' and emo_dict[utt] == 'ang':
            hap2ang += 1
        if pre_emo == 'hap' and emo_dict[utt] == 'hap':
            hap2hap += 1
        if pre_emo == 'hap' and emo_dict[utt] == 'neu':
            hap2neu += 1
        if pre_emo == 'hap' and emo_dict[utt] == 'sad':
            hap2sad += 1

        if pre_emo == 'neu' and emo_dict[utt] == 'ang':
            neu2ang += 1
        if pre_emo == 'neu' and emo_dict[utt] == 'hap':
            neu2hap += 1
        if pre_emo == 'neu' and emo_dict[utt] == 'neu':
            neu2neu += 1
        if pre_emo == 'neu' and emo_dict[utt] == 'sad':
            neu2sad += 1

        if pre_emo == 'sad' and emo_dict[utt] == 'ang':
            sad2ang += 1
        if pre_emo == 'sad' and emo_dict[utt] == 'hap':
            sad2hap += 1
        if pre_emo == 'sad' and emo_dict[utt] == 'neu':
            sad2neu += 1
        if pre_emo == 'sad' and emo_dict[utt] == 'sad':
            sad2sad += 1
        
        pre_dialog_id = dialog_id
        pre_emo = emo_dict[utt]
        total_transit += 1
    
    total_transit -= 1
    return {'a2a':ang2ang/total_transit, 'a2h':ang2hap/total_transit, 'a2n':ang2neu/total_transit, 'a2s':ang2sad/total_transit, \
                    'h2a':hap2ang/total_transit, 'h2h':hap2hap/total_transit, 'h2n':hap2neu/total_transit, 'h2s':hap2sad/total_transit, \
                    'n2a':neu2ang/total_transit, 'n2h':neu2hap/total_transit, 'n2n':neu2neu/total_transit, 'n2s':neu2sad/total_transit, \
                    's2a':sad2ang/total_transit, 's2h':sad2hap/total_transit, 's2n':sad2neu/total_transit, 's2s':sad2sad/total_transit}

if __name__ == '__main__':
    emo_dict = joblib.load('emo_all_iemocap.pkl')
    print(emo_trans_prob(emo_dict))
