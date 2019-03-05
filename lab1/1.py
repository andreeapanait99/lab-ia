#variabile
# v_1 = 5
# print v_1
# print type(v_1)
# v_1 /= 3
# print (v_1)

#liste
# l_1 = [1, 5, 2, 15, 13]
# print l_1[3]
# print len(l_1)
# print l_1[-1]
# print l_1[len(l_1) - len(l_1)]
# l_1.append(10)
# l_1.append([20,30])
# l_1.pop()
# l_1.pop(1)
# l_1.extend([20, 30, 40])
# l_1.insert(1,5000)
# print l_1
# print l_1[1:len(l_1):2]
# print l_1[:4:2]
#
# a = b = c = 0
# for val in l_1:
#     if val < 7:
#         a += val
#     elif val > 7:
#         b += val
#     else:
#         c += 1
# print ('a = %d, b = %d, c = %d' %(a, b, c))
#
# l_2 = []
# for val in l_1:
#     for val2 in l_1:
#         if val2 > 7:
#             l_2.append(val * val2)
# print l_2
#
# l_3 = [val * val2 for val in l_1 for val2 in l_1 if val2 > 7]
# print l_3
#
# for idx in range(len(l_1)):
#     print l_1[idx]

#functii
# l_1 = [1, 3, 10, 6]
# print l_1
# def extrage(L):
#     elem = L[-1]
#     L.pop()
#     return elem
# print extrage(l_1)
# print l_1
# L = l_1[:]
# print extrage(L)
# print l_1
# print L

def acc(yr, yp):
    s = 0.0
    for i in range(len(yr)):
        if yr[i] == yp[i]:
            s += 1
    return s/len(yr)

def prec_rec(yr, yp):
    tp = fp = fn = 0.0
    for i in range(len(yr)):
        if yr[i] == yp[i] == 1:
            tp += 1
        elif yr[i] == 1 and yp[i] == 0:
            fn += 1
        elif yr[i] == 0 and yp[i] == 1:
            fp += 1
    return tp / (tp + fn), tp / (tp + fp)

yp = [1, 1, 1, 0, 1, 0, 1, 1, 0, 0]
yr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
print acc(yr, yp)
print prec_rec(yr, yp)