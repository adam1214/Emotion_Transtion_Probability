import joblib
import numpy as np
def softmax(x):
    """Compute the softmax of vector x."""
    exp_x = np.exp(x)
    softmax_x = exp_x / np.sum(exp_x)
    return softmax_x 

def emo_trans_prob(emo_dict, val=None):
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
        if val and val == dialog_id[0:5]:
            continue

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
    a = softmax([ang2ang/total_transit, ang2hap/total_transit, ang2neu/total_transit, ang2sad/total_transit])
    h = softmax([hap2ang/total_transit, hap2hap/total_transit, hap2neu/total_transit, hap2sad/total_transit])
    n = softmax([neu2ang/total_transit, neu2hap/total_transit, neu2neu/total_transit, neu2sad/total_transit])
    s = softmax([sad2ang/total_transit, sad2hap/total_transit, sad2neu/total_transit, sad2sad/total_transit])
    return {'a2a':a[0], 'a2h':a[1], 'a2n':a[2], 'a2s':a[3], \
                    'h2a':h[0], 'h2h':h[1], 'h2n':h[2], 'h2s':h[3], \
                    'n2a':n[0], 'n2h':n[1], 'n2n':n[2], 'n2s':n[3], \
                    's2a':s[0], 's2h':s[1], 's2n':s[2], 's2s':s[3]}

def get_val_emo_trans_prob(emo_dict):
    """Get emo_trans_prob estimated from training sessions."""

    session = ['Ses01', 'Ses02', 'Ses03', 'Ses04', 'Ses05']
    emo_trans_prob_dict = {}
    for i in range(len(session)):
      val = session[i]
      train_sessions = session[:i] + session[i+1:]
      emo_trans_prob_com = emo_trans_prob(emo_dict, val)
      emo_trans_prob_dict[val] = emo_trans_prob_com

    return emo_trans_prob_dict

if __name__ == '__main__':
    emo_dict = joblib.load('emo_all_iemocap.pkl')
    emo_trans_prob_ = emo_trans_prob(emo_dict)
    print('ang2ang :', emo_trans_prob_['a2a'])
    print('ang2hap :', emo_trans_prob_['a2h'])
    print('ang2neu :', emo_trans_prob_['a2n'])
    print('ang2sad :', emo_trans_prob_['a2s'])
    print('=============================================')
    print('hap2ang :', emo_trans_prob_['h2a'])
    print('hap2hap :', emo_trans_prob_['h2h'])
    print('hap2neu :', emo_trans_prob_['h2n'])
    print('hap2sad :', emo_trans_prob_['h2s'])
    print('=============================================')
    print('neu2ang :', emo_trans_prob_['n2a'])
    print('neu2hap :', emo_trans_prob_['n2h'])
    print('neu2neu :', emo_trans_prob_['n2n'])
    print('neu2sad :', emo_trans_prob_['n2s'])   
    print('=============================================')
    print('sad2ang :', emo_trans_prob_['s2a'])
    print('sad2hap :', emo_trans_prob_['s2h'])
    print('sad2neu :', emo_trans_prob_['s2n'])
    print('sad2sad :', emo_trans_prob_['s2s'])
    print('=============================================')
    total_prob = 0
    for prob in emo_trans_prob(emo_dict).values():
        total_prob += prob
    print('total prob:', total_prob)
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    get_val_emo_trans_prob_ = get_val_emo_trans_prob(emo_dict)
    print(get_val_emo_trans_prob_['Ses01'])
    print(get_val_emo_trans_prob_['Ses02'])
    print(get_val_emo_trans_prob_['Ses03'])
    print(get_val_emo_trans_prob_['Ses04'])
    print(get_val_emo_trans_prob_['Ses05'])
