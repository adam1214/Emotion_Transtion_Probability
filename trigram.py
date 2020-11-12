import joblib
import numpy as np
def softmax(x):
    """Compute the softmax of vector x."""
    exp_x = np.exp(x)
    softmax_x = exp_x / np.sum(exp_x)
    return softmax_x 

def emo_trans_prob_TRI_need_softmax(emo_dict, dialogs, val=None):
    # only estimate anger, happiness, neutral, sadness
    total_transit = 0

    aaa = 0
    aah = 0
    aan = 0
    aas = 0
    aha = 0
    ahh = 0
    ahn = 0
    ahs = 0
    ana = 0
    anh = 0
    ann = 0
    ans = 0
    asa = 0
    ash = 0
    asn = 0
    ass = 0

    haa = 0
    hah = 0
    han = 0
    has = 0
    hha = 0
    hhh = 0
    hhn = 0
    hhs = 0
    hna = 0
    hnh = 0
    hnn = 0
    hns = 0
    hsa = 0
    hsh = 0
    hsn = 0
    hss = 0

    naa = 0
    nah = 0
    nan = 0
    nas = 0
    nha = 0
    nhh = 0
    nhn = 0
    nhs = 0
    nna = 0
    nnh = 0
    nnn = 0
    nns = 0
    nsa = 0
    nsh = 0
    nsn = 0
    nss = 0

    saa = 0
    sah = 0
    san = 0
    sas = 0
    sha = 0
    shh = 0
    shn = 0
    shs = 0
    sna = 0
    snh = 0
    snn = 0
    sns = 0
    ssa = 0
    ssh = 0
    ssn = 0
    sss = 0

    pre_emo = ''
    pre_pre_emo = ''
    pre_dialog_id = ''
    last_dialog_last_utt_emo = ''

    for dialog in dialogs.values():
        for utt in dialog:
            last_dialog_last_utt_emo = emo_dict[utt]
            dialog_id = utt[0:-5]
            #print(dialog_id)
            if val and val == dialog_id[0:5]:
                continue

            if emo_dict[utt] != 'ang' and emo_dict[utt] != 'hap' and emo_dict[utt] != 'neu' and emo_dict[utt] != 'sad': 
                # only estimate anger, happiness, neutral, sadness
                pre_dialog_id = dialog_id
                continue

            if pre_emo == '' and pre_dialog_id == '': #begining of the traversal
                pre_emo = emo_dict[utt]
                pre_dialog_id = dialog_id
                #total_transit += 1
                continue

            if pre_emo != '' and pre_pre_emo == '': #after one step of new dialog traversal
                pre_pre_emo = pre_emo
                pre_emo = emo_dict[utt]
                pre_dialog_id = dialog_id
                continue

            if pre_dialog_id != dialog_id: #new dialog
                #total_transit -= 1
                pre_emo = ''
                pre_pre_emo = ''
            
            if pre_pre_emo == 'ang' and pre_emo == 'ang' and emo_dict[utt] == 'ang':
                aaa += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'ang' and emo_dict[utt] == 'hap':
                aah += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'ang' and emo_dict[utt] == 'neu':
                aan += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'ang' and emo_dict[utt] == 'sad':
                aas += 1
                total_transit += 1

            if pre_pre_emo == 'ang' and pre_emo == 'hap' and emo_dict[utt] == 'ang':
                aha += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'hap' and emo_dict[utt] == 'hap':
                ahh += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'hap' and emo_dict[utt] == 'neu':
                ahn += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'hap' and emo_dict[utt] == 'sad':
                ahs += 1
                total_transit += 1

            if pre_pre_emo == 'ang' and pre_emo == 'neu' and emo_dict[utt] == 'ang':
                ana += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'neu' and emo_dict[utt] == 'hap':
                anh += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'neu' and emo_dict[utt] == 'neu':
                ann += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'neu' and emo_dict[utt] == 'sad':
                ans += 1
                total_transit += 1

            if pre_pre_emo == 'ang' and pre_emo == 'sad' and emo_dict[utt] == 'ang':
                asa += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'sad' and emo_dict[utt] == 'hap':
                ash += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'sad' and emo_dict[utt] == 'neu':
                asn += 1
                total_transit += 1
            if pre_pre_emo == 'ang' and pre_emo == 'sad' and emo_dict[utt] == 'sad':
                ass += 1
                total_transit += 1
            #########################################################################
            if pre_pre_emo == 'hap' and pre_emo == 'ang' and emo_dict[utt] == 'ang':
                haa += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'ang' and emo_dict[utt] == 'hap':
                hah += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'ang' and emo_dict[utt] == 'neu':
                han += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'ang' and emo_dict[utt] == 'sad':
                has += 1
                total_transit += 1

            if pre_pre_emo == 'hap' and pre_emo == 'hap' and emo_dict[utt] == 'ang':
                hha += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'hap' and emo_dict[utt] == 'hap':
                hhh += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'hap' and emo_dict[utt] == 'neu':
                hhn += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'hap' and emo_dict[utt] == 'sad':
                hhs += 1
                total_transit += 1

            if pre_pre_emo == 'hap' and pre_emo == 'neu' and emo_dict[utt] == 'ang':
                hna += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'neu' and emo_dict[utt] == 'hap':
                hnh += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'neu' and emo_dict[utt] == 'neu':
                hnn += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'neu' and emo_dict[utt] == 'sad':
                hns += 1
                total_transit += 1

            if pre_pre_emo == 'hap' and pre_emo == 'sad' and emo_dict[utt] == 'ang':
                hsa += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'sad' and emo_dict[utt] == 'hap':
                hsh += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'sad' and emo_dict[utt] == 'neu':
                hsn += 1
                total_transit += 1
            if pre_pre_emo == 'hap' and pre_emo == 'sad' and emo_dict[utt] == 'sad':
                hss += 1
                total_transit += 1
            #########################################################################
            if pre_pre_emo == 'neu' and pre_emo == 'ang' and emo_dict[utt] == 'ang':
                naa += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'ang' and emo_dict[utt] == 'hap':
                nah += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'ang' and emo_dict[utt] == 'neu':
                nan += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'ang' and emo_dict[utt] == 'sad':
                nas += 1
                total_transit += 1

            if pre_pre_emo == 'neu' and pre_emo == 'hap' and emo_dict[utt] == 'ang':
                nha += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'hap' and emo_dict[utt] == 'hap':
                nhh += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'hap' and emo_dict[utt] == 'neu':
                nhn += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'hap' and emo_dict[utt] == 'sad':
                nhs += 1
                total_transit += 1

            if pre_pre_emo == 'neu' and pre_emo == 'neu' and emo_dict[utt] == 'ang':
                nna += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'neu' and emo_dict[utt] == 'hap':
                nnh += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'neu' and emo_dict[utt] == 'neu':
                nnn += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'neu' and emo_dict[utt] == 'sad':
                nns += 1
                total_transit += 1

            if pre_pre_emo == 'neu' and pre_emo == 'sad' and emo_dict[utt] == 'ang':
                nsa += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'sad' and emo_dict[utt] == 'hap':
                nsh += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'sad' and emo_dict[utt] == 'neu':
                nsn += 1
                total_transit += 1
            if pre_pre_emo == 'neu' and pre_emo == 'sad' and emo_dict[utt] == 'sad':
                nss += 1          
                total_transit += 1
            #########################################################################
            if pre_pre_emo == 'sad' and pre_emo == 'ang' and emo_dict[utt] == 'ang':
                saa += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'ang' and emo_dict[utt] == 'hap':
                sah += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'ang' and emo_dict[utt] == 'neu':
                san += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'ang' and emo_dict[utt] == 'sad':
                sas += 1
                total_transit += 1

            if pre_pre_emo == 'sad' and pre_emo == 'hap' and emo_dict[utt] == 'ang':
                sha += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'hap' and emo_dict[utt] == 'hap':
                shh += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'hap' and emo_dict[utt] == 'neu':
                shn += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'hap' and emo_dict[utt] == 'sad':
                shs += 1
                total_transit += 1

            if pre_pre_emo == 'sad' and pre_emo == 'neu' and emo_dict[utt] == 'ang':
                sna += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'neu' and emo_dict[utt] == 'hap':
                snh += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'neu' and emo_dict[utt] == 'neu':
                snn += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'neu' and emo_dict[utt] == 'sad':
                sns += 1
                total_transit += 1

            if pre_pre_emo == 'sad' and pre_emo == 'sad' and emo_dict[utt] == 'ang':
                ssa += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'sad' and emo_dict[utt] == 'hap':
                ssh += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'sad' and emo_dict[utt] == 'neu':
                ssn += 1
                total_transit += 1
            if pre_pre_emo == 'sad' and pre_emo == 'sad' and emo_dict[utt] == 'sad':
                sss += 1
                total_transit += 1
   
            pre_dialog_id = dialog_id
            pre_pre_emo = pre_emo
            pre_emo = emo_dict[utt]
    #if last_dialog_last_utt_emo == 'ang' or last_dialog_last_utt_emo == 'hap' or last_dialog_last_utt_emo == 'neu' or last_dialog_last_utt_emo == 'sad':
        #total_transit -= 1
    print("before softmax:")
    print( (aaa+aah+aan+aas+aha+ahh+ahn+ahs+ana+anh+ann+ans+asa+ash+asn+ass+haa+hah+han+has+hha+hhh+hhn+hhs+hna+hnh+hnn+hns+hsa+hsh+hsn+hss+naa+nah+nan+nas+nha+nhh+nhn+nhs+nna+nnh+nnn+nns+nsa+nsh+nsn+nss+saa+sah+san+sas+sha+shh+shn+shs+sna+snh+snn+sns+ssa+ssh+ssn+sss)/total_transit )
    '''
    a = softmax([ang2ang/total_transit, ang2hap/total_transit, ang2neu/total_transit, ang2sad/total_transit])
    h = softmax([hap2ang/total_transit, hap2hap/total_transit, hap2neu/total_transit, hap2sad/total_transit])
    n = softmax([neu2ang/total_transit, neu2hap/total_transit, neu2neu/total_transit, neu2sad/total_transit])
    s = softmax([sad2ang/total_transit, sad2hap/total_transit, sad2neu/total_transit, sad2sad/total_transit])
    return {'a2a':a[0], 'a2h':a[1], 'a2n':a[2], 'a2s':a[3], \
                    'h2a':h[0], 'h2h':h[1], 'h2n':h[2], 'h2s':h[3], \
                    'n2a':n[0], 'n2h':n[1], 'n2n':n[2], 'n2s':n[3], \
                    's2a':s[0], 's2h':s[1], 's2n':s[2], 's2s':s[3]}
    '''

def emo_trans_prob_TRI_without_softmax(emo_dict, dialogs, val=None):
    # only estimate anger, happiness, neutral, sadness
    a2 = 0
    h2 = 0
    n2 = 0
    s2 = 0

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
    last_dialog_last_utt_emo = ''

    for dialog in dialogs.values():
        for utt in dialog:
            last_dialog_last_utt_emo = emo_dict[utt]
            dialog_id = utt[0:-5]
            #print(dialog_id)
            if val and val == dialog_id[0:5]:
                continue

            if emo_dict[utt] != 'ang' and emo_dict[utt] != 'hap' and emo_dict[utt] != 'neu' and emo_dict[utt] != 'sad': 
                # only estimate anger, happiness, neutral, sadness
                pre_dialog_id = dialog_id
                continue

            if pre_emo == '' and pre_dialog_id == '': #begining of the traversal
                pre_emo = emo_dict[utt]
                pre_dialog_id = dialog_id
                if pre_emo == 'ang':
                    a2 += 1
                elif pre_emo == 'hap':
                    h2 += 1
                elif pre_emo == 'neu':
                    n2 += 1
                else:
                    s2 += 1
                continue

            if pre_dialog_id != dialog_id: #new dialog
                if pre_emo == 'ang':
                    a2 -= 1
                elif pre_emo == 'hap':
                    h2 -= 1
                elif pre_emo == 'neu':
                    n2 -= 1
                else:
                    s2 -= 1
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
            if pre_emo == 'ang':
                a2 += 1
            elif pre_emo == 'hap':
                h2 += 1
            elif pre_emo == 'neu':
                n2 += 1
            else:
                s2 += 1
    
    if last_dialog_last_utt_emo == 'ang':
            a2 -= 1
    elif last_dialog_last_utt_emo == 'hap':
        h2 -= 1
    elif last_dialog_last_utt_emo == 'neu':
        n2 -= 1
    elif last_dialog_last_utt_emo == 'sad':
        s2 -= 1
    print(ang2ang/a2+ang2hap/a2+ang2neu/a2+ang2sad/a2)
    print(hap2ang/h2+hap2hap/h2+hap2neu/h2+hap2sad/h2)
    print(neu2ang/n2+neu2hap/n2+neu2neu/n2+neu2sad/n2)
    print(sad2ang/s2+sad2hap/s2+sad2neu/s2+sad2sad/s2)
    print('=============================================')
    return {'a2a':ang2ang/a2, 'a2h':ang2hap/a2, 'a2n':ang2neu/a2, 'a2s':ang2sad/a2, \
                    'h2a':hap2ang/h2, 'h2h':hap2hap/h2, 'h2n':hap2neu/h2, 'h2s':hap2sad/h2, \
                    'n2a':neu2ang/n2, 'n2h':neu2hap/n2, 'n2n':neu2neu/n2, 'n2s':neu2sad/n2, \
                    's2a':sad2ang/s2, 's2h':sad2hap/s2, 's2n':sad2neu/s2, 's2s':sad2sad/s2}

def get_val_emo_trans_prob(emo_dict, dialogs, softmax_or_not):
    """Get emo_trans_prob estimated from training sessions."""

    session = ['Ses01', 'Ses02', 'Ses03', 'Ses04', 'Ses05']
    emo_trans_prob_dict = {}
    for i in range(len(session)):
        val = session[i]
        train_sessions = session[:i] + session[i+1:]
        if softmax_or_not == 1:
            emo_trans_prob_com = emo_trans_prob_TRI_need_softmax(emo_dict, dialogs, val)
            emo_trans_prob_dict[val] = emo_trans_prob_com
        elif softmax_or_not == 0:
            emo_trans_prob_com = emo_trans_prob_TRI_without_softmax(emo_dict, dialogs, val)
            emo_trans_prob_dict[val] = emo_trans_prob_com
    return emo_trans_prob_dict

if __name__ == '__main__':
    emo_dict = joblib.load('emo_all_iemocap.pkl')
    dialogs = joblib.load('dialog_iemocap.pkl')
    
    print('==========with softmax==========')
    emo_trans_prob_need_softmax_ = emo_trans_prob_TRI_need_softmax(emo_dict, dialogs)
    '''
    print('ang2ang :', emo_trans_prob_need_softmax_['a2a'])
    print('ang2hap :', emo_trans_prob_need_softmax_['a2h'])
    print('ang2neu :', emo_trans_prob_need_softmax_['a2n'])
    print('ang2sad :', emo_trans_prob_need_softmax_['a2s'])
    print('=============================================')
    print('hap2ang :', emo_trans_prob_need_softmax_['h2a'])
    print('hap2hap :', emo_trans_prob_need_softmax_['h2h'])
    print('hap2neu :', emo_trans_prob_need_softmax_['h2n'])
    print('hap2sad :', emo_trans_prob_need_softmax_['h2s'])
    print('=============================================')
    print('neu2ang :', emo_trans_prob_need_softmax_['n2a'])
    print('neu2hap :', emo_trans_prob_need_softmax_['n2h'])
    print('neu2neu :', emo_trans_prob_need_softmax_['n2n'])
    print('neu2sad :',emo_trans_prob_need_softmax_['n2s'])   
    print('=============================================')
    print('sad2ang :', emo_trans_prob_need_softmax_['s2a'])
    print('sad2hap :', emo_trans_prob_need_softmax_['s2h'])
    print('sad2neu :', emo_trans_prob_need_softmax_['s2n'])
    print('sad2sad :', emo_trans_prob_need_softmax_['s2s'])
    print('=============================================')
    total_prob = 0
    for prob in emo_trans_prob_TRI_need_softmax(emo_dict, dialogs).values():
        total_prob += prob
    print('total prob:', total_prob)
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    '''
    get_val_emo_trans_prob_ = get_val_emo_trans_prob(emo_dict, dialogs, 1)
    '''
    print(get_val_emo_trans_prob_['Ses01'])
    print(get_val_emo_trans_prob_['Ses02'])
    print(get_val_emo_trans_prob_['Ses03'])
    print(get_val_emo_trans_prob_['Ses04'])
    print(get_val_emo_trans_prob_['Ses05'])
    '''
    '''
    print('==========without softmax==========')
    emo_trans_prob_without_softmax_ = emo_trans_prob_TRI_without_softmax(emo_dict, dialogs)
    print('ang2ang :', emo_trans_prob_without_softmax_['a2a'])
    print('ang2hap :', emo_trans_prob_without_softmax_['a2h'])
    print('ang2neu :', emo_trans_prob_without_softmax_['a2n'])
    print('ang2sad :', emo_trans_prob_without_softmax_['a2s'])
    print(emo_trans_prob_without_softmax_['a2a']+emo_trans_prob_without_softmax_['a2h']+emo_trans_prob_without_softmax_['a2n']+emo_trans_prob_without_softmax_['a2s'])
    print('=============================================')
    print('hap2ang :', emo_trans_prob_without_softmax_['h2a'])
    print('hap2hap :', emo_trans_prob_without_softmax_['h2h'])
    print('hap2neu :', emo_trans_prob_without_softmax_['h2n'])
    print('hap2sad :', emo_trans_prob_without_softmax_['h2s'])
    print(emo_trans_prob_without_softmax_['h2a']+emo_trans_prob_without_softmax_['h2h']+emo_trans_prob_without_softmax_['h2n']+emo_trans_prob_without_softmax_['h2s'])
    print('=============================================')
    print('neu2ang :', emo_trans_prob_without_softmax_['n2a'])
    print('neu2hap :', emo_trans_prob_without_softmax_['n2h'])
    print('neu2neu :', emo_trans_prob_without_softmax_['n2n'])
    print('neu2sad :', emo_trans_prob_without_softmax_['n2s'])   
    print(emo_trans_prob_without_softmax_['n2a']+emo_trans_prob_without_softmax_['n2h']+emo_trans_prob_without_softmax_['n2n']+emo_trans_prob_without_softmax_['n2s'])
    print('=============================================')
    print('sad2ang :', emo_trans_prob_without_softmax_['s2a'])
    print('sad2hap :', emo_trans_prob_without_softmax_['s2h'])
    print('sad2neu :', emo_trans_prob_without_softmax_['s2n'])
    print('sad2sad :', emo_trans_prob_without_softmax_['s2s'])
    print(emo_trans_prob_without_softmax_['s2a']+emo_trans_prob_without_softmax_['s2h']+emo_trans_prob_without_softmax_['s2n']+emo_trans_prob_without_softmax_['s2s'])
    print('=============================================')
    get_val_emo_trans_prob_ = get_val_emo_trans_prob(emo_dict, dialogs, 0)
    print(get_val_emo_trans_prob_['Ses01'])
    print(get_val_emo_trans_prob_['Ses02'])
    print(get_val_emo_trans_prob_['Ses03'])
    print(get_val_emo_trans_prob_['Ses04'])
    print(get_val_emo_trans_prob_['Ses05'])
    '''