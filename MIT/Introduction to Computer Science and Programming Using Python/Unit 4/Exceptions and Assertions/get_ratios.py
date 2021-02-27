def get_ratios(L1, L2):
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bad args')
    return ratios

L1 = [1,2,3,4]
L2 = [5,6,7,8]
L3 = [5,6,7]
L4 = [5,6,7,0]
#print(get_ratios(L1, L2))
print(get_ratios(L1, L3))
#print(get_ratios(L1, L4))
