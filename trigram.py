import joblib
import numpy as np
def softmax(x):
    """Compute the softmax of vector x."""
    exp_x = np.exp(x)
    softmax_x = exp_x / np.sum(exp_x)
    return softmax_x 

def emo_trans_prob_TRI_need_softmax(emo_dict, dialogs, add_one_smooth_or_not, val=None):
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
    if add_one_smooth_or_not == 1:
        total_transit += 64

        aaa += 1
        aah += 1
        aan += 1
        aas += 1
        aha += 1
        ahh += 1
        ahn += 1
        ahs += 1
        ana += 1
        anh += 1
        ann += 1
        ans += 1
        asa += 1
        ash += 1
        asn += 1
        ass += 1

        haa += 1
        hah += 1
        han += 1
        has += 1
        hha += 1
        hhh += 1
        hhn += 1
        hhs += 1
        hna += 1
        hnh += 1
        hnn += 1
        hns += 1
        hsa += 1
        hsh += 1
        hsn += 1
        hss += 1

        naa += 1
        nah += 1
        nan += 1
        nas += 1
        nha += 1
        nhh += 1
        nhn += 1
        nhs += 1
        nna += 1
        nnh += 1
        nnn += 1
        nns += 1
        nsa += 1
        nsh += 1
        nsn += 1
        nss += 1

        saa += 1
        sah += 1
        san += 1
        sas += 1
        sha += 1
        shh += 1
        shn += 1
        shs += 1
        sna += 1
        snh += 1
        snn += 1
        sns += 1
        ssa += 1
        ssh += 1
        ssn += 1
        sss += 1
    print("before softmax:")
    print( (aaa+aah+aan+aas+aha+ahh+ahn+ahs+ana+anh+ann+ans+asa+ash+asn+ass+haa+hah+han+has+hha+hhh+hhn+hhs+hna+hnh+hnn+hns+hsa+hsh+hsn+hss+naa+nah+nan+nas+nha+nhh+nhn+nhs+nna+nnh+nnn+nns+nsa+nsh+nsn+nss+saa+sah+san+sas+sha+shh+shn+shs+sna+snh+snn+sns+ssa+ssh+ssn+sss)/total_transit )
    '''
    print('aaa', aaa)
    print('aah', aah)
    print('aan', aan)
    print('aas', aas)
    print('aha', aha)
    print('ahh', ahh)
    print('ahn', ahn)
    print('ahs', ahs)
    print('ana', ana)
    print('anh', anh)
    print('ann', ann)
    print('ans', ans)
    print('asa', asa)
    print('ash', ash)
    print('asn', asn)
    print('ass', ass)
    #################
    print('haa', haa)
    print('hah', hah)
    print('han', han)
    print('has', has)
    print('hha', hha)
    print('hhh', hhh)
    print('hhn', hhn)
    print('hhs', hhs)
    print('hna', hna)
    print('hnh', hnh)
    print('hnn', hnn)
    print('hns', hns)
    print('hsa', hsa)
    print('hsh', hsh)
    print('hsn', hsn)
    print('hss', hss)
    #################
    print('naa', naa)
    print('nah', nah)
    print('nan', nan)
    print('nas', nas)
    print('nha', nha)
    print('nhh', nhh)
    print('nhn', nhn)
    print('nhs', nhs)
    print('nna', nna)
    print('nnh', nnh)
    print('nnn', nnn)
    print('nns', nns)
    print('nsa', nsa)
    print('nsh', nsh)
    print('nsn', nsn)
    print('nss', nss)
    #################
    print('saa', saa)
    print('sah', sah)
    print('san', san)
    print('sas', sas)
    print('sha', sha)
    print('shh', shh)
    print('shn', shn)
    print('shs', shs)
    print('sna', sna)
    print('snh', snh)
    print('snn', snn)
    print('sns', sns)
    print('ssa', ssa)
    print('ssh', ssh)
    print('ssn', ssn)
    print('sss', sss)
    print('total_transit', total_transit)
    '''
    a_a = softmax([aaa/total_transit, aah/total_transit, aan/total_transit, aas/total_transit])
    a_h = softmax([aha/total_transit, ahh/total_transit, ahn/total_transit, ahs/total_transit])
    a_n = softmax([ana/total_transit, anh/total_transit, ann/total_transit, ans/total_transit])
    a_s = softmax([asa/total_transit, ash/total_transit, asn/total_transit, ass/total_transit])
    ###########################################################################################
    h_a = softmax([haa/total_transit, hah/total_transit, han/total_transit, has/total_transit])
    h_h = softmax([hha/total_transit, hhh/total_transit, hhn/total_transit, hhs/total_transit])
    h_n = softmax([hna/total_transit, hnh/total_transit, hnn/total_transit, hns/total_transit])
    h_s = softmax([hsa/total_transit, hsh/total_transit, hsn/total_transit, hss/total_transit])
    ###########################################################################################
    n_a = softmax([naa/total_transit, nah/total_transit, nan/total_transit, nas/total_transit])
    n_h = softmax([nha/total_transit, nhh/total_transit, nhn/total_transit, nhs/total_transit])
    n_n = softmax([nna/total_transit, nnh/total_transit, nnn/total_transit, nns/total_transit])
    n_s = softmax([nsa/total_transit, nsh/total_transit, nsn/total_transit, nss/total_transit])
    ###########################################################################################
    s_a = softmax([saa/total_transit, sah/total_transit, san/total_transit, sas/total_transit])
    s_h = softmax([sha/total_transit, shh/total_transit, shn/total_transit, shs/total_transit])
    s_n = softmax([sna/total_transit, snh/total_transit, snn/total_transit, sns/total_transit])
    s_s = softmax([ssa/total_transit, ssh/total_transit, ssn/total_transit, sss/total_transit])

    return {'aaa':a_a[0], 'aah':a_a[1], 'aan':a_a[2], 'aas':a_a[3], \
            'aha':a_h[0], 'ahh':a_h[1], 'ahn':a_h[2], 'ahs':a_h[3], \
            'ana':a_n[0], 'anh':a_n[1], 'ann':a_n[2], 'ans':a_n[3], \
            'asa':a_s[0], 'ash':a_s[1], 'asn':a_s[2], 'ass':a_s[3], \
            'haa':h_a[0], 'hah':h_a[1], 'han':h_a[2], 'has':h_a[3], \
            'hha':h_h[0], 'hhh':h_h[1], 'hhn':h_h[2], 'hhs':h_h[3], \
            'hna':h_n[0], 'hnh':h_n[1], 'hnn':h_n[2], 'hns':h_n[3], \
            'hsa':h_s[0], 'hsh':h_s[1], 'hsn':h_s[2], 'hss':h_s[3], \
            'naa':n_a[0], 'nah':n_a[1], 'nan':n_a[2], 'nas':n_a[3], \
            'nha':n_h[0], 'nhh':n_h[1], 'nhn':n_h[2], 'nhs':n_h[3], \
            'nna':n_n[0], 'nnh':n_n[1], 'nnn':n_n[2], 'nns':n_n[3], \
            'nsa':n_s[0], 'nsh':n_s[1], 'nsn':n_s[2], 'nss':n_s[3], \
            'saa':s_a[0], 'sah':s_a[1], 'san':s_a[2], 'sas':s_a[3], \
            'sha':s_h[0], 'shh':s_h[1], 'shn':s_h[2], 'shs':s_h[3], \
            'sna':s_n[0], 'snh':s_n[1], 'snn':s_n[2], 'sns':s_n[3], \
            'ssa':s_s[0], 'ssh':s_s[1], 'ssn':s_s[2], 'sss':s_s[3]  }

def emo_trans_prob_TRI_without_softmax(emo_dict, dialogs, add_one_smooth_or_not, val=None):
    # only estimate anger, happiness, neutral, sadness
    a_a = 0
    a_h = 0
    a_n = 0
    a_s = 0

    h_a = 0
    h_h = 0
    h_n = 0
    h_s = 0

    n_a = 0
    n_h = 0
    n_n = 0
    n_s = 0

    s_a = 0
    s_h = 0
    s_n = 0
    s_s = 0

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
                a_a += 1
            if pre_pre_emo == 'ang' and pre_emo == 'ang' and emo_dict[utt] == 'hap':
                aah += 1
                a_a += 1
            if pre_pre_emo == 'ang' and pre_emo == 'ang' and emo_dict[utt] == 'neu':
                aan += 1
                a_a += 1
            if pre_pre_emo == 'ang' and pre_emo == 'ang' and emo_dict[utt] == 'sad':
                aas += 1
                a_a += 1

            if pre_pre_emo == 'ang' and pre_emo == 'hap' and emo_dict[utt] == 'ang':
                aha += 1
                a_h += 1
            if pre_pre_emo == 'ang' and pre_emo == 'hap' and emo_dict[utt] == 'hap':
                ahh += 1
                a_h += 1
            if pre_pre_emo == 'ang' and pre_emo == 'hap' and emo_dict[utt] == 'neu':
                ahn += 1
                a_h += 1
            if pre_pre_emo == 'ang' and pre_emo == 'hap' and emo_dict[utt] == 'sad':
                ahs += 1
                a_h += 1

            if pre_pre_emo == 'ang' and pre_emo == 'neu' and emo_dict[utt] == 'ang':
                ana += 1
                a_n += 1
            if pre_pre_emo == 'ang' and pre_emo == 'neu' and emo_dict[utt] == 'hap':
                anh += 1
                a_n += 1
            if pre_pre_emo == 'ang' and pre_emo == 'neu' and emo_dict[utt] == 'neu':
                ann += 1
                a_n += 1
            if pre_pre_emo == 'ang' and pre_emo == 'neu' and emo_dict[utt] == 'sad':
                ans += 1
                a_n += 1

            if pre_pre_emo == 'ang' and pre_emo == 'sad' and emo_dict[utt] == 'ang':
                asa += 1
                a_s += 1
            if pre_pre_emo == 'ang' and pre_emo == 'sad' and emo_dict[utt] == 'hap':
                ash += 1
                a_s += 1
            if pre_pre_emo == 'ang' and pre_emo == 'sad' and emo_dict[utt] == 'neu':
                asn += 1
                a_s += 1
            if pre_pre_emo == 'ang' and pre_emo == 'sad' and emo_dict[utt] == 'sad':
                ass += 1
                a_s += 1
            #########################################################################
            if pre_pre_emo == 'hap' and pre_emo == 'ang' and emo_dict[utt] == 'ang':
                haa += 1
                h_a += 1
            if pre_pre_emo == 'hap' and pre_emo == 'ang' and emo_dict[utt] == 'hap':
                hah += 1
                h_a += 1
            if pre_pre_emo == 'hap' and pre_emo == 'ang' and emo_dict[utt] == 'neu':
                han += 1
                h_a += 1
            if pre_pre_emo == 'hap' and pre_emo == 'ang' and emo_dict[utt] == 'sad':
                has += 1
                h_a += 1

            if pre_pre_emo == 'hap' and pre_emo == 'hap' and emo_dict[utt] == 'ang':
                hha += 1
                h_h += 1
            if pre_pre_emo == 'hap' and pre_emo == 'hap' and emo_dict[utt] == 'hap':
                hhh += 1
                h_h += 1
            if pre_pre_emo == 'hap' and pre_emo == 'hap' and emo_dict[utt] == 'neu':
                hhn += 1
                h_h += 1
            if pre_pre_emo == 'hap' and pre_emo == 'hap' and emo_dict[utt] == 'sad':
                hhs += 1
                h_h += 1

            if pre_pre_emo == 'hap' and pre_emo == 'neu' and emo_dict[utt] == 'ang':
                hna += 1
                h_n += 1
            if pre_pre_emo == 'hap' and pre_emo == 'neu' and emo_dict[utt] == 'hap':
                hnh += 1
                h_n += 1
            if pre_pre_emo == 'hap' and pre_emo == 'neu' and emo_dict[utt] == 'neu':
                hnn += 1
                h_n += 1
            if pre_pre_emo == 'hap' and pre_emo == 'neu' and emo_dict[utt] == 'sad':
                hns += 1
                h_n += 1

            if pre_pre_emo == 'hap' and pre_emo == 'sad' and emo_dict[utt] == 'ang':
                hsa += 1
                h_s += 1
            if pre_pre_emo == 'hap' and pre_emo == 'sad' and emo_dict[utt] == 'hap':
                hsh += 1
                h_s += 1
            if pre_pre_emo == 'hap' and pre_emo == 'sad' and emo_dict[utt] == 'neu':
                hsn += 1
                h_s += 1
            if pre_pre_emo == 'hap' and pre_emo == 'sad' and emo_dict[utt] == 'sad':
                hss += 1
                h_s += 1
            #########################################################################
            if pre_pre_emo == 'neu' and pre_emo == 'ang' and emo_dict[utt] == 'ang':
                naa += 1
                n_a += 1
            if pre_pre_emo == 'neu' and pre_emo == 'ang' and emo_dict[utt] == 'hap':
                nah += 1
                n_a += 1
            if pre_pre_emo == 'neu' and pre_emo == 'ang' and emo_dict[utt] == 'neu':
                nan += 1
                n_a += 1
            if pre_pre_emo == 'neu' and pre_emo == 'ang' and emo_dict[utt] == 'sad':
                nas += 1
                n_a += 1

            if pre_pre_emo == 'neu' and pre_emo == 'hap' and emo_dict[utt] == 'ang':
                nha += 1
                n_h += 1
            if pre_pre_emo == 'neu' and pre_emo == 'hap' and emo_dict[utt] == 'hap':
                nhh += 1
                n_h += 1
            if pre_pre_emo == 'neu' and pre_emo == 'hap' and emo_dict[utt] == 'neu':
                nhn += 1
                n_h += 1
            if pre_pre_emo == 'neu' and pre_emo == 'hap' and emo_dict[utt] == 'sad':
                nhs += 1
                n_h += 1

            if pre_pre_emo == 'neu' and pre_emo == 'neu' and emo_dict[utt] == 'ang':
                nna += 1
                n_n += 1
            if pre_pre_emo == 'neu' and pre_emo == 'neu' and emo_dict[utt] == 'hap':
                nnh += 1
                n_n += 1
            if pre_pre_emo == 'neu' and pre_emo == 'neu' and emo_dict[utt] == 'neu':
                nnn += 1
                n_n += 1
            if pre_pre_emo == 'neu' and pre_emo == 'neu' and emo_dict[utt] == 'sad':
                nns += 1
                n_n += 1

            if pre_pre_emo == 'neu' and pre_emo == 'sad' and emo_dict[utt] == 'ang':
                nsa += 1
                n_s += 1
            if pre_pre_emo == 'neu' and pre_emo == 'sad' and emo_dict[utt] == 'hap':
                nsh += 1
                n_s += 1
            if pre_pre_emo == 'neu' and pre_emo == 'sad' and emo_dict[utt] == 'neu':
                nsn += 1
                n_s += 1
            if pre_pre_emo == 'neu' and pre_emo == 'sad' and emo_dict[utt] == 'sad':
                nss += 1          
                n_s += 1
            #########################################################################
            if pre_pre_emo == 'sad' and pre_emo == 'ang' and emo_dict[utt] == 'ang':
                saa += 1
                s_a += 1
            if pre_pre_emo == 'sad' and pre_emo == 'ang' and emo_dict[utt] == 'hap':
                sah += 1
                s_a += 1
            if pre_pre_emo == 'sad' and pre_emo == 'ang' and emo_dict[utt] == 'neu':
                san += 1
                s_a += 1
            if pre_pre_emo == 'sad' and pre_emo == 'ang' and emo_dict[utt] == 'sad':
                sas += 1
                s_a += 1

            if pre_pre_emo == 'sad' and pre_emo == 'hap' and emo_dict[utt] == 'ang':
                sha += 1
                s_h += 1
            if pre_pre_emo == 'sad' and pre_emo == 'hap' and emo_dict[utt] == 'hap':
                shh += 1
                s_h += 1
            if pre_pre_emo == 'sad' and pre_emo == 'hap' and emo_dict[utt] == 'neu':
                shn += 1
                s_h += 1
            if pre_pre_emo == 'sad' and pre_emo == 'hap' and emo_dict[utt] == 'sad':
                shs += 1
                s_h += 1

            if pre_pre_emo == 'sad' and pre_emo == 'neu' and emo_dict[utt] == 'ang':
                sna += 1
                s_n += 1
            if pre_pre_emo == 'sad' and pre_emo == 'neu' and emo_dict[utt] == 'hap':
                snh += 1
                s_n += 1
            if pre_pre_emo == 'sad' and pre_emo == 'neu' and emo_dict[utt] == 'neu':
                snn += 1
                s_n += 1
            if pre_pre_emo == 'sad' and pre_emo == 'neu' and emo_dict[utt] == 'sad':
                sns += 1
                s_n += 1

            if pre_pre_emo == 'sad' and pre_emo == 'sad' and emo_dict[utt] == 'ang':
                ssa += 1
                s_s += 1
            if pre_pre_emo == 'sad' and pre_emo == 'sad' and emo_dict[utt] == 'hap':
                ssh += 1
                s_s += 1
            if pre_pre_emo == 'sad' and pre_emo == 'sad' and emo_dict[utt] == 'neu':
                ssn += 1
                s_s += 1
            if pre_pre_emo == 'sad' and pre_emo == 'sad' and emo_dict[utt] == 'sad':
                sss += 1
                s_s += 1
   
            pre_dialog_id = dialog_id
            pre_pre_emo = pre_emo
            pre_emo = emo_dict[utt]

    if add_one_smooth_or_not == 1:
        a_a += 3
        a_h += 4
        a_n += 4
        a_s += 4

        h_a += 4
        h_h += 4
        h_n += 4
        h_s += 4

        n_a += 4
        n_h += 4
        n_n += 4
        n_s += 4

        s_a += 4
        s_h += 4
        s_n += 4
        s_s += 4

        aaa += 1
        aah += 1
        aan += 1
        aas += 1
        aha += 1
        ahh += 1
        ahn += 1
        ahs += 1
        ana += 1
        anh += 1
        ann += 1
        ans += 1
        asa += 1
        ash += 1
        asn += 1
        ass += 1

        haa += 1
        hah += 1
        han += 1
        has += 1
        hha += 1
        hhh += 1
        hhn += 1
        hhs += 1
        hna += 1
        hnh += 1
        hnn += 1
        hns += 1
        hsa += 1
        hsh += 1
        hsn += 1
        hss += 1

        naa += 1
        nah += 1
        nan += 1
        nas += 1
        nha += 1
        nhh += 1
        nhn += 1
        nhs += 1
        nna += 1
        nnh += 1
        nnn += 1
        nns += 1
        nsa += 1
        nsh += 1
        nsn += 1
        nss += 1

        saa += 1
        sah += 1
        san += 1
        sas += 1
        sha += 1
        shh += 1
        shn += 1
        shs += 1
        sna += 1
        snh += 1
        snn += 1
        sns += 1
        ssa += 1
        ssh += 1
        ssn += 1
        sss += 1
    print( (aaa+aah+aan+aas)/a_a )
    print( (aha+ahh+ahn+ahs)/a_h )
    print( (ana+anh+ann+ans)/a_n )
    print( (asa+ash+asn+ass)/a_s )

    print( (haa+hah+han+has)/h_a )
    print( (hha+hhh+hhn+hhs)/h_h )
    print( (hna+hnh+hnn+hns)/h_n )
    print( (hsa+hsh+hsn+hss)/h_s )

    print( (naa+nah+nan+nas)/n_a )
    print( (nha+nhh+nhn+nhs)/n_h )
    print( (nna+nnh+nnn+nns)/n_n )
    print( (nsa+nsh+nsn+nss)/n_s )

    print( (saa+sah+san+sas)/s_a )
    print( (sha+shh+shn+shs)/s_h )
    print( (sna+snh+snn+sns)/s_n )
    print( (ssa+ssh+ssn+sss)/s_s )
    print('=============================================')
    return {'aaa':aaa/a_a, 'aah':aah/a_a, 'aan':aan/a_a, 'aas':aas/a_a, \
            'aha':aha/a_h, 'ahh':ahh/a_h, 'ahn':ahn/a_h, 'ahs':ahs/a_h, \
            'ana':ana/a_n, 'anh':anh/a_n, 'ann':ann/a_n, 'ans':ans/a_n, \
            'asa':asa/a_s, 'ash':ash/a_s, 'asn':asn/a_s, 'ass':ass/a_s, \
            'haa':haa/h_a, 'hah':hah/h_a, 'han':han/h_a, 'has':has/h_a, \
            'hha':hha/h_h, 'hhh':hhh/h_h, 'hhn':hhn/h_h, 'hhs':hhs/h_h, \
            'hna':hna/h_n, 'hnh':hnh/h_n, 'hnn':hnn/h_n, 'hns':hns/h_n, \
            'hsa':hsa/h_s, 'hsh':hsh/h_s, 'hsn':hsn/h_s, 'hss':hss/h_s, \
            'naa':naa/n_a, 'nah':nah/n_a, 'nan':nan/n_a, 'nas':nas/n_a, \
            'nha':nha/n_h, 'nhh':nhh/n_h, 'nhn':nhn/n_h, 'nhs':nhs/n_h, \
            'nna':nna/n_n, 'nnh':nnh/n_n, 'nnn':nnn/n_n, 'nns':nns/n_n, \
            'nsa':nsa/n_s, 'nsh':nsh/n_s, 'nsn':nsn/n_s, 'nss':nss/n_s, \
            'saa':saa/s_a, 'sah':sah/s_a, 'san':san/s_a, 'sas':sas/s_a, \
            'sha':sha/s_h, 'shh':shh/s_h, 'shn':shn/s_h, 'shs':shs/s_h, \
            'sna':sna/s_n, 'snh':snh/s_n, 'snn':snn/s_n, 'sns':sns/s_n, \
            'ssa':ssa/s_s, 'ssh':ssh/s_s, 'ssn':ssn/s_s, 'sss':sss/s_s  }

def get_val_emo_trans_prob(emo_dict, dialogs, softmax_or_not):
    """Get emo_trans_prob estimated from training sessions."""

    session = ['Ses01', 'Ses02', 'Ses03', 'Ses04', 'Ses05']
    emo_trans_prob_dict = {}
    for i in range(len(session)):
        val = session[i]
        train_sessions = session[:i] + session[i+1:]
        if softmax_or_not == 1:
            emo_trans_prob_com = emo_trans_prob_TRI_need_softmax(emo_dict, dialogs, 1, val)
            emo_trans_prob_dict[val] = emo_trans_prob_com
        elif softmax_or_not == 0:
            emo_trans_prob_com = emo_trans_prob_TRI_without_softmax(emo_dict, dialogs, 0, val)
            emo_trans_prob_dict[val] = emo_trans_prob_com
    return emo_trans_prob_dict

if __name__ == '__main__':
    emo_dict = joblib.load('emo_all_iemocap.pkl')
    dialogs = joblib.load('dialog_iemocap.pkl')
    '''
    print('==========with softmax==========')
    emo_trans_prob_need_softmax_ = emo_trans_prob_TRI_need_softmax(emo_dict, dialogs, 1)
    get_val_emo_trans_prob_ = get_val_emo_trans_prob(emo_dict, dialogs, 1)

    print(get_val_emo_trans_prob_)
    print(get_val_emo_trans_prob_['Ses01'])
    print(get_val_emo_trans_prob_['Ses02'])
    print(get_val_emo_trans_prob_['Ses03'])
    print(get_val_emo_trans_prob_['Ses04'])
    print(get_val_emo_trans_prob_['Ses05'])
    '''

    print('==========without softmax==========')
    emo_trans_prob_without_softmax_ = emo_trans_prob_TRI_without_softmax(emo_dict, dialogs, 0)
    get_val_emo_trans_prob_ = get_val_emo_trans_prob(emo_dict, dialogs, 0)
