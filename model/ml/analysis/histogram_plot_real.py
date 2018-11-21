import numpy as np
import matplotlib.pyplot as plt

#fscores = [0.10000000000000002, 0.14, 0.16, 0.12, 0.12, 0.15, 0.12, 0.13, 0.14, 0.10000000000000002, 0.11, 0.10000000000000002, 0.12, 0.12, 0.14, 0.15, 0.12, 0.15, 0.14, 0.06, 0.13, 0.14, 0.12, 0.11, 0.16, 0.15, 0.14, 0.12, 0.12, 0.12, 0.16, 0.15, 0.09, 0.10000000000000002, 0.14, 0.11, 0.12, 0.13, 0.16, 0.10000000000000002, 0.14, 0.15, 0.14, 0.14, 0.13, 0.18, 0.09, 0.12, 0.12, 0.12, 0.14, 0.09, 0.14, 0.14, 0.10000000000000002, 0.10000000000000002, 0.15, 0.13, 0.09, 0.07, 0.13, 0.10000000000000002, 0.11, 0.07, 0.10000000000000002, 0.14, 0.14, 0.11, 0.17, 0.11, 0.13, 0.14, 0.11, 0.18, 0.17, 0.16, 0.08, 0.11, 0.06, 0.10000000000000002, 0.11, 0.14, 0.14, 0.11, 0.09, 0.14, 0.16, 0.13, 0.17, 0.12, 0.13, 0.14, 0.13, 0.14, 0.09, 0.13, 0.17, 0.18, 0.10000000000000002, 0.16]
#fscores = [0.13, 0.14, 0.13, 0.08, 0.07, 0.08, 0.09, 0.15, 0.13, 0.09, 0.12, 0.12, 0.13, 0.10000000000000002, 0.12, 0.09, 0.11, 0.11, 0.07, 0.14, 0.09, 0.13, 0.09, 0.14, 0.10000000000000002, 0.11, 0.12, 0.12, 0.10000000000000002, 0.09, 0.10000000000000002, 0.09, 0.09, 0.10000000000000002, 0.16, 0.12, 0.13, 0.08, 0.09, 0.12, 0.11, 0.11, 0.17, 0.08, 0.13, 0.15, 0.07, 0.16, 0.14, 0.12, 0.13, 0.07, 0.09, 0.10000000000000002, 0.10000000000000002, 0.08, 0.04, 0.12, 0.07, 0.12, 0.13, 0.07, 0.11, 0.10000000000000002, 0.14, 0.09, 0.11, 0.16]
#fscores = [0.09, 0.08, 0.15, 0.15, 0.11, 0.09, 0.11, 0.12, 0.13, 0.12, 0.14, 0.10000000000000002, 0.10000000000000002, 0.13, 0.10000000000000002, 0.13, 0.10000000000000002, 0.11, 0.10000000000000002, 0.09, 0.11, 0.15, 0.12, 0.08, 0.15, 0.13, 0.14, 0.12, 0.09, 0.13, 0.09, 0.06, 0.10000000000000002, 0.12, 0.07, 0.12, 0.13, 0.09, 0.10000000000000002, 0.11, 0.08, 0.15, 0.15, 0.12, 0.12, 0.15, 0.13, 0.14, 0.15, 0.10000000000000002, 0.13, 0.11, 0.10000000000000002, 0.12, 0.11, 0.09, 0.13, 0.11, 0.11, 0.13]
#fscores = [0.13, 0.12, 0.16, 0.10000000000000002, 0.13, 0.13, 0.10000000000000002, 0.11, 0.11, 0.15, 0.08, 0.11, 0.10000000000000002, 0.10000000000000002, 0.13, 0.09, 0.10000000000000002, 0.14, 0.13, 0.03, 0.11, 0.11, 0.13, 0.06, 0.09, 0.09, 0.13, 0.07, 0.11, 0.10000000000000002, 0.11, 0.14, 0.15, 0.09, 0.10000000000000002, 0.17, 0.07, 0.11, 0.11, 0.13, 0.13, 0.13, 0.15, 0.09, 0.11, 0.09, 0.10000000000000002, 0.13, 0.09, 0.12, 0.12, 0.15, 0.10000000000000002, 0.11, 0.13, 0.10000000000000002, 0.11, 0.14, 0.11, 0.07, 0.11, 0.14, 0.12, 0.08, 0.11, 0.11, 0.11, 0.13, 0.15, 0.07, 0.06, 0.13, 0.15, 0.11, 0.09, 0.10000000000000002, 0.15, 0.12, 0.10000000000000002, 0.13, 0.06, 0.11, 0.11, 0.13, 0.10000000000000002, 0.14, 0.11, 0.13, 0.13, 0.14, 0.13, 0.11, 0.11, 0.12, 0.11, 0.19, 0.18, 0.09, 0.10000000000000002, 0.08, 0.09, 0.08, 0.11, 0.14, 0.10000000000000002, 0.11, 0.09, 0.06, 0.13, 0.07, 0.10000000000000002, 0.23, 0.15, 0.08, 0.10000000000000002, 0.12, 0.11, 0.09, 0.09, 0.11, 0.11, 0.11, 0.08, 0.07, 0.15, 0.11, 0.12, 0.13, 0.12, 0.12, 0.13, 0.10000000000000002, 0.09, 0.11, 0.12, 0.09, 0.13, 0.14, 0.10000000000000002, 0.09, 0.15, 0.11, 0.11, 0.11, 0.11, 0.11, 0.16, 0.13, 0.11, 0.10000000000000002, 0.10000000000000002, 0.14, 0.09, 0.10000000000000002, 0.08, 0.12, 0.10000000000000002, 0.13, 0.09, 0.14, 0.07, 0.09, 0.12, 0.16, 0.11, 0.11, 0.11, 0.12, 0.12, 0.11, 0.10000000000000002, 0.11]
#fscores = [0.11, 0.13, 0.12, 0.09, 0.12, 0.10000000000000002, 0.13, 0.12, 0.11, 0.15, 0.07, 0.10000000000000002, 0.10000000000000002, 0.10000000000000002, 0.14, 0.11, 0.09, 0.10000000000000002, 0.09, 0.07, 0.08, 0.11, 0.10000000000000002, 0.11, 0.14, 0.12, 0.10000000000000002, 0.13, 0.11, 0.12, 0.09, 0.14, 0.12, 0.15, 0.13, 0.08, 0.09, 0.07, 0.10000000000000002, 0.10000000000000002, 0.09, 0.10000000000000002, 0.09, 0.11, 0.11, 0.14, 0.13, 0.10000000000000002, 0.12, 0.13, 0.12, 0.16, 0.08, 0.14, 0.16, 0.14, 0.13, 0.10000000000000002, 0.14, 0.12, 0.15, 0.14, 0.08, 0.13, 0.12, 0.08, 0.13, 0.12, 0.12, 0.10000000000000002, 0.11, 0.16, 0.08, 0.09, 0.13, 0.15, 0.10000000000000002, 0.11, 0.16, 0.10000000000000002, 0.10000000000000002, 0.12, 0.11, 0.08, 0.16, 0.12, 0.10000000000000002, 0.10000000000000002, 0.08, 0.14, 0.15, 0.16, 0.07, 0.08, 0.13, 0.10000000000000002, 0.15, 0.08, 0.10000000000000002, 0.09, 0.13, 0.06, 0.12, 0.11, 0.11, 0.08, 0.10000000000000002, 0.12, 0.06, 0.09, 0.12, 0.17, 0.06, 0.08, 0.12, 0.06, 0.12, 0.13, 0.06, 0.10000000000000002, 0.06, 0.15, 0.10000000000000002, 0.05000000000000001, 0.09, 0.12, 0.12, 0.11, 0.10000000000000002, 0.11, 0.17, 0.11, 0.12, 0.11, 0.08, 0.14, 0.12, 0.12, 0.09, 0.11, 0.13, 0.15, 0.13, 0.17, 0.09, 0.11, 0.12, 0.10000000000000002, 0.10000000000000002, 0.13, 0.09, 0.10000000000000002, 0.13, 0.14, 0.12, 0.09, 0.10000000000000002, 0.12, 0.11, 0.07, 0.12, 0.14, 0.11, 0.14, 0.11, 0.14, 0.12, 0.12, 0.11, 0.13, 0.12, 0.11, 0.15, 0.14, 0.15, 0.14, 0.08, 0.14, 0.10000000000000002, 0.07, 0.18, 0.06, 0.15, 0.15, 0.07, 0.13, 0.08, 0.10000000000000002, 0.11, 0.07, 0.10000000000000002, 0.09, 0.09, 0.10000000000000002, 0.13, 0.14, 0.13, 0.03, 0.12, 0.03, 0.13, 0.10000000000000002, 0.10000000000000002, 0.12, 0.15, 0.12, 0.11, 0.10000000000000002, 0.12, 0.10000000000000002, 0.15, 0.13, 0.10000000000000002, 0.11, 0.12, 0.11, 0.14, 0.11, 0.09, 0.12, 0.11, 0.13, 0.10000000000000002, 0.14, 0.07, 0.08, 0.08, 0.13, 0.11, 0.11, 0.10000000000000002, 0.08, 0.11, 0.10000000000000002, 0.17, 0.14, 0.16, 0.13, 0.10000000000000002, 0.10000000000000002, 0.09, 0.13, 0.09, 0.14, 0.13, 0.12, 0.09, 0.14, 0.08, 0.14, 0.16, 0.06, 0.13, 0.13, 0.13, 0.10000000000000002, 0.12, 0.09, 0.11, 0.14, 0.13, 0.11, 0.11, 0.13, 0.14, 0.11, 0.08, 0.08, 0.16, 0.11, 0.10000000000000002, 0.11, 0.12, 0.09, 0.08, 0.07, 0.10000000000000002, 0.09, 0.14, 0.10000000000000002, 0.10000000000000002, 0.10000000000000002, 0.08, 0.11, 0.14, 0.07, 0.09, 0.13, 0.10000000000000002, 0.11, 0.10000000000000002, 0.09, 0.09, 0.09, 0.12, 0.09, 0.10000000000000002, 0.10000000000000002, 0.09, 0.08, 0.11, 0.16, 0.10000000000000002, 0.08, 0.07, 0.08, 0.12, 0.18, 0.15, 0.14, 0.10000000000000002, 0.15, 0.12, 0.15, 0.15, 0.10000000000000002, 0.09, 0.08, 0.09, 0.09, 0.13, 0.14, 0.09, 0.07, 0.19, 0.09, 0.17, 0.13, 0.12, 0.14, 0.13]

#heart
#default dboost
#fscores = [0.6976744186046512, 0.7160493827160495, 0.5432098765432098, 0.6582278481012659, 0.691358024691358, 0.6987951807228916, 0.6923076923076924, 0.6575342465753424, 0.6829268292682926, 0.6829268292682926, 0.7341772151898734, 0.7500000000000001, 0.7228915662650603, 0.6749999999999999, 0.7160493827160495, 0.746987951807229, 0.5952380952380952, 0.8045977011494253, 0.7619047619047619, 0.717948717948718, 0.7560975609756099, 0.6829268292682926, 0.759493670886076, 0.6818181818181819, 0.717948717948718, 0.7317073170731706, 0.625, 0.5454545454545454, 0.6987951807228916, 0.7209302325581395, 0.6067415730337079, 0.5945945945945946, 0.7228915662650603, 0.6904761904761905, 0.6590909090909092, 0.6571428571428571, 0.7012987012987013, 0.725, 0.7, 0.7088607594936708, 0.746987951807229, 0.7, 0.6666666666666667, 0.7906976744186046, 0.7435897435897436, 0.7012987012987013, 0.6923076923076924, 0.7272727272727272, 0.6976744186046512, 0.6265060240963854, 0.6585365853658537, 0.6419753086419754, 0.7272727272727272, 0.7088607594936708, 0.689655172413793, 0.6823529411764705, 0.7073170731707318, 0.44776119402985076, 0.7654320987654322, 0.6842105263157895, 0.7435897435897436, 0.7954545454545455, 0.7058823529411765, 0.7, 0.7032967032967032, 0.7529411764705882, 0.7160493827160495, 0.7727272727272727, 0.7073170731707318, 0.6590909090909092, 0.7, 0.746987951807229, 0.7012987012987013, 0.6987951807228916, 0.7045454545454546, 0.6097560975609756, 0.6923076923076924, 0.7532467532467533, 0.7466666666666666, 0.6987951807228916, 0.6875000000000001, 0.6923076923076924, 0.8292682926829269, 0.6666666666666666, 0.7532467532467533, 0.7142857142857143, 0.7272727272727272, 0.674698795180723, 0.6756756756756757, 0.7045454545454546, 0.7058823529411765, 0.6593406593406593, 0.6153846153846153, 0.7012987012987013, 0.5454545454545454, 0.7368421052631577, 0.7407407407407408, 0.7058823529411765, 0.7228915662650603, 0.5897435897435898, 0.7341772151898734, 0.6582278481012659, 0.7341772151898734, 0.7160493827160495, 0.6818181818181819, 0.6923076923076924, 0.6835443037974683, 0.6835443037974683, 0.689655172413793, 0.6585365853658537, 0.6410256410256411, 0.6027397260273972, 0.7191011235955055, 0.7529411764705882, 0.7, 0.689655172413793, 0.7294117647058824, 0.7012987012987013, 0.6835443037974683, 0.7906976744186046, 0.7058823529411765, 0.7441860465116279, 0.7228915662650603, 0.6823529411764705, 0.6842105263157895, 0.6753246753246753, 0.6419753086419754, 0.6842105263157895, 0.7105263157894737, 0.7272727272727272, 0.7058823529411765, 0.7088607594936708, 0.7804878048780488, 0.6315789473684211, 0.7951807228915663, 0.6741573033707866, 0.6582278481012659, 0.6744186046511628, 0.691358024691358, 0.725, 0.746987951807229, 0.725, 0.691358024691358, 0.7640449438202246, 0.6923076923076924, 0.6578947368421053, 0.6582278481012659, 0.7317073170731706, 0.6744186046511628, 0.725, 0.7088607594936708, 0.7466666666666666, 0.5588235294117647, 0.6666666666666666, 0.7123287671232876, 0.725, 0.647887323943662, 0.725, 0.7088607594936708, 0.6842105263157895, 0.605263157894737, 0.7500000000000001, 0.7200000000000001, 0.6923076923076924, 0.7088607594936708, 0.6419753086419754, 0.735632183908046, 0.7160493827160495, 0.6506024096385543, 0.7407407407407408, 0.6428571428571429, 0.7380952380952381, 0.7073170731707318, 0.7317073170731706, 0.6976744186046512, 0.7441860465116279, 0.6, 0.6585365853658537, 0.6666666666666666, 0.7045454545454546, 0.6987951807228916, 0.717948717948718, 0.7058823529411765, 0.7848101265822786, 0.611764705882353, 0.6813186813186813, 0.5925925925925927, 0.6829268292682926, 0.7142857142857143, 0.6419753086419754, 0.6666666666666666, 0.717948717948718, 0.7532467532467533, 0.725, 0.689655172413793, 0.6511627906976744, 0.7, 0.7142857142857143, 0.6666666666666666, 0.7608695652173915, 0.7951807228915663, 0.6744186046511628, 0.7126436781609196, 0.6666666666666666, 0.7073170731707318, 0.5, 0.725, 0.6835443037974683, 0.6315789473684211, 0.7209302325581395, 0.7272727272727272, 0.611111111111111, 0.6666666666666666, 0.7045454545454546, 0.6582278481012659, 0.6585365853658537, 0.7435897435897436, 0.6590909090909092, 0.5588235294117647, 0.6749999999999999, 0.7160493827160495, 0.5, 0.7209302325581395, 0.7, 0.7073170731707318, 0.7341772151898734, 0.6585365853658537, 0.7142857142857143, 0.7058823529411765, 0.7073170731707318, 0.717948717948718, 0.7294117647058824, 0.7532467532467533, 0.625, 0.6749999999999999, 0.7142857142857143, 0.7, 0.6976744186046512, 0.7088607594936708, 0.6388888888888888, 0.6216216216216217, 0.7111111111111111, 0.7012987012987013, 0.6829268292682926, 0.7200000000000001, 0.6666666666666666, 0.7073170731707318, 0.7710843373493976, 0.5301204819277109, 0.6666666666666666, 0.6666666666666666, 0.625, 0.7111111111111111, 0.6578947368421053, 0.7435897435897436, 0.775, 0.7058823529411765, 0.7012987012987013, 0.691358024691358, 0.605263157894737, 0.7500000000000001, 0.5952380952380952, 0.6578947368421053, 0.717948717948718, 0.759493670886076, 0.6666666666666666, 0.6388888888888888, 0.7500000000000001, 0.7500000000000001, 0.7317073170731706, 0.7228915662650603, 0.717948717948718, 0.7407407407407408, 0.6153846153846153, 0.7341772151898734, 0.6410256410256411, 0.7, 0.6428571428571429, 0.6419753086419754, 0.7435897435897436, 0.725, 0.7058823529411765, 0.6835443037974683, 0.7111111111111111, 0.5507246376811594, 0.7407407407407408, 0.7160493827160495, 0.7500000000000001, 0.7160493827160495, 0.6666666666666666, 0.7088607594936708, 0.7317073170731706, 0.6493506493506493, 0.6976744186046512, 0.7126436781609196, 0.6829268292682926, 0.7435897435897436, 0.6506024096385543, 0.6493506493506493, 0.7441860465116279, 0.6666666666666666, 0.6582278481012659, 0.7, 0.8192771084337348, 0.7, 0.6904761904761905, 0.6823529411764705, 0.6744186046511628]
#plt.axvline(x=0.7294117647058824) #best single column features

#horse
#fscores = [0.875, 0.9052631578947369, 0.8712871287128713, 0.787878787878788, 0.7578947368421053, 0.7835051546391752, 0.875, 0.8865979381443299, 0.6990291262135923, 0.8958333333333334, 0.845360824742268, 0.9052631578947369, 0.8865979381443299, 0.8659793814432989, 0.7254901960784315, 0.8631578947368421, 0.8712871287128713, 0.8842105263157894, 0.8400000000000001, 0.8865979381443299, 0.9090909090909091, 0.7450980392156864, 0.8, 0.8400000000000001, 0.8247422680412372, 0.9090909090909091, 0.8958333333333334, 0.7346938775510204, 0.9052631578947369, 0.8571428571428572, 0.8913043478260869, 0.8080808080808081, 0.875, 0.7010309278350516, 0.7766990291262137, 0.8817204301075269, 0.8775510204081632, 0.7722772277227722, 0.8958333333333334, 0.9072164948453607, 0.7368421052631579, 0.9052631578947369, 0.76, 0.8514851485148515, 0.8842105263157894, 0.8686868686868686, 0.851063829787234, 0.7766990291262137, 0.8723404255319149, 0.9183673469387755, 0.7961165048543689, 0.8541666666666666, 0.7766990291262137, 0.8659793814432989, 0.7959183673469388, 0.8631578947368421, 0.875, 0.9090909090909091, 0.8041237113402061, 0.8514851485148515, 0.836734693877551, 0.7551020408163266, 0.8695652173913043, 0.8659793814432989, 0.8541666666666666, 0.7142857142857142, 0.8659793814432989, 0.8631578947368421, 0.8631578947368421, 0.74, 0.8686868686868686, 0.8541666666666666, 0.7884615384615384, 0.7676767676767677, 0.8979591836734694, 0.8514851485148515, 0.8958333333333334, 0.8817204301075269, 0.7999999999999999, 0.7843137254901961, 0.7959183673469388, 0.7920792079207922, 0.8316831683168316, 0.7474747474747475, 0.8247422680412372, 0.9183673469387755, 0.8723404255319149, 0.8842105263157894, 0.8484848484848485, 0.9090909090909091, 0.888888888888889, 0.8958333333333334, 0.8842105263157894, 0.8484848484848485, 0.8958333333333334, 0.8080808080808081, 0.8631578947368421, 0.8979591836734694, 0.8842105263157894, 0.8958333333333334, 0.8958333333333334, 0.9072164948453607, 0.8, 0.8979591836734694, 0.8659793814432989, 0.836734693877551, 0.888888888888889, 0.7628865979381444, 0.8659793814432989, 0.8659793814432989, 0.9263157894736843, 0.6599999999999999, 0.888888888888889, 0.7291666666666665, 0.8039215686274509, 0.787878787878788, 0.9052631578947369, 0.742857142857143, 0.8712871287128713, 0.9148936170212766, 0.8571428571428572, 0.845360824742268, 0.787878787878788, 0.875, 0.8865979381443299, 0.7924528301886793, 0.9166666666666666, 0.8775510204081632, 0.8979591836734694, 0.8659793814432989, 0.8316831683168316, 0.7326732673267327, 0.7722772277227722, 0.9072164948453607, 0.8958333333333334, 0.8842105263157894, 0.9166666666666666, 0.8958333333333334, 0.8979591836734694, 0.8775510204081632, 0.7526881720430108, 0.7647058823529411, 0.8627450980392156, 0.8842105263157894, 0.8247422680412372, 0.7291666666666665, 0.9166666666666666, 0.9072164948453607, 0.875, 0.78, 0.8775510204081632, 0.8775510204081632, 0.86, 0.9032258064516129, 0.8958333333333334, 0.7708333333333333, 0.7766990291262137, 0.875, 0.8631578947368421, 0.8631578947368421, 0.8484848484848485, 0.9052631578947369, 0.8775510204081632, 0.8936170212765957, 0.8484848484848485, 0.7843137254901961, 0.9183673469387755, 0.8484848484848485, 0.7663551401869159, 0.7920792079207922, 0.8541666666666666, 0.8913043478260869, 0.8865979381443299, 0.8865979381443299, 0.8775510204081632, 0.7835051546391752, 0.8, 0.7578947368421053, 0.888888888888889, 0.8865979381443299, 0.816326530612245, 0.8316831683168316, 0.7326732673267327, 0.7692307692307692, 0.8842105263157894, 0.8842105263157894, 0.7920792079207922, 0.9072164948453607, 0.7676767676767677, 0.7755102040816326, 0.8936170212765957, 0.8571428571428572, 0.8631578947368421, 0.7551020408163266, 0.7722772277227722, 0.8936170212765957, 0.8316831683168316, 0.723404255319149, 0.7708333333333333, 0.875, 0.875, 0.7415730337078651, 0.875, 0.7450980392156864, 0.8659793814432989, 0.7254901960784315, 0.8936170212765957, 0.7722772277227722, 0.7524752475247525, 0.888888888888889, 0.8571428571428572, 0.836734693877551, 0.78, 0.8842105263157894, 0.7961165048543689, 0.816326530612245, 0.8631578947368421, 0.875, 0.7572815533980584, 0.7199999999999999, 0.7628865979381444, 0.9072164948453607, 0.875, 0.8936170212765957, 0.8400000000000001, 0.75, 0.8958333333333334, 0.7216494845360826, 0.8041237113402061, 0.8, 0.86, 0.8936170212765957, 0.9166666666666666, 0.888888888888889, 0.7199999999999999, 0.8076923076923077, 0.7766990291262137, 0.6804123711340205, 0.8936170212765957, 0.8936170212765957, 0.6990291262135923, 0.8865979381443299, 0.7659574468085107, 0.8842105263157894, 0.8913043478260869, 0.9090909090909091, 0.7647058823529411, 0.8333333333333334, 0.9263157894736843, 0.7216494845360826, 0.8659793814432989, 0.7272727272727272, 0.8659793814432989, 0.8958333333333334, 0.8958333333333334, 0.7961165048543689, 0.7572815533980584, 0.8631578947368421, 0.8659793814432989, 0.9183673469387755, 0.8979591836734694, 0.8571428571428572, 0.875, 0.8631578947368421, 0.9166666666666666, 0.8659793814432989, 0.9166666666666666, 0.7722772277227722, 0.8659793814432989, 0.7789473684210526, 0.8842105263157894, 0.7450980392156864, 0.8775510204081632, 0.8958333333333334, 0.8958333333333334, 0.8958333333333334, 0.8297872340425533, 0.7474747474747475, 0.888888888888889, 0.845360824742268, 0.888888888888889, 0.7070707070707071, 0.823529411764706, 0.8865979381443299, 0.7422680412371135, 0.875, 0.8842105263157894, 0.8958333333333334, 0.8958333333333334, 0.7755102040816326, 0.823529411764706, 0.78, 0.8421052631578947, 0.7872340425531915, 0.7676767676767677, 0.8723404255319149, 0.8865979381443299, 0.8865979381443299, 0.8936170212765957, 0.787878787878788, 0.8631578947368421, 0.78, 0.8842105263157894, 0.8775510204081632, 0.8958333333333334, 0.76, 0.8627450980392156, 0.7843137254901961, 0.8723404255319149, 0.8842105263157894, 0.8799999999999999, 0.9263157894736843, 0.8958333333333334, 0.854368932038835, 0.8958333333333334, 0.9052631578947369, 0.7551020408163266, 0.8247422680412372, 0.75, 0.8247422680412372, 0.875, 0.8936170212765957, 0.845360824742268, 0.7216494845360826, 0.8571428571428572, 0.8333333333333334, 0.78, 0.8125, 0.8958333333333334, 0.8602150537634408, 0.8659793814432989, 0.9032258064516129, 0.8039215686274509, 0.7346938775510204, 0.8571428571428572, 0.8979591836734694, 0.7450980392156864, 0.7346938775510204, 0.8958333333333334, 0.8686868686868686, 0.8842105263157894, 0.9072164948453607, 0.8913043478260869, 0.9090909090909091, 0.845360824742268, 0.9278350515463918, 0.7647058823529411, 0.7628865979381444, 0.7572815533980584, 0.7959183673469388, 0.723404255319149, 0.8631578947368421, 0.7735849056603773, 0.8, 0.851063829787234, 0.875, 0.78, 0.8958333333333334, 0.888888888888889, 0.875, 0.8775510204081632, 0.7572815533980584, 0.8247422680412372, 0.717391304347826, 0.9166666666666666, 0.9072164948453607, 0.8936170212765957, 0.7741935483870969, 0.787878787878788, 0.7755102040816326, 0.8247422680412372, 0.9183673469387755, 0.8723404255319149, 0.8200000000000001, 0.845360824742268, 0.76, 0.888888888888889, 0.8484848484848485, 0.9148936170212766, 0.7999999999999999, 0.8723404255319149, 0.7959183673469388, 0.7755102040816326, 0.7578947368421053, 0.8421052631578947, 0.7199999999999999, 0.7524752475247525, 0.8400000000000001, 0.8400000000000001, 0.8478260869565218, 0.7368421052631579, 0.9032258064516129, 0.8958333333333334, 0.9052631578947369, 0.9032258064516129, 0.8842105263157894, 0.78, 0.875, 0.78, 0.8842105263157894, 0.8865979381443299, 0.8958333333333334, 0.8200000000000001, 0.7291666666666665, 0.8478260869565218, 0.7628865979381444, 0.7450980392156864, 0.9278350515463918, 0.836734693877551, 0.7916666666666666, 0.8478260869565218, 0.8039215686274509, 0.8958333333333334, 0.6804123711340205, 0.8865979381443299, 0.7474747474747475, 0.7524752475247525, 0.7346938775510204, 0.8958333333333334, 0.8936170212765957, 0.8936170212765957, 0.7010309278350516, 0.8958333333333334, 0.851063829787234, 0.8979591836734694, 0.8799999999999999, 0.7157894736842105, 0.7959183673469388, 0.8799999999999999, 0.75, 0.8865979381443299, 0.78, 0.7474747474747475, 0.8865979381443299, 0.8, 0.8686868686868686, 0.7524752475247525, 0.7916666666666666, 0.9183673469387755, 0.8541666666666666, 0.8041237113402061, 0.8865979381443299, 0.8936170212765957, 0.9166666666666666, 0.8958333333333334, 0.9375, 0.6938775510204083, 0.875, 0.787878787878788, 0.8936170212765957, 0.8695652173913043, 0.742857142857143, 0.8, 0.8979591836734694, 0.7835051546391752, 0.9052631578947369, 0.7474747474747475, 0.8958333333333334, 0.8865979381443299, 0.8076923076923077, 0.823529411764706, 0.78, 0.8979591836734694, 0.7843137254901961, 0.8, 0.9072164948453607, 0.8, 0.7959183673469388, 0.6947368421052632, 0.9090909090909091, 0.8421052631578947, 0.8865979381443299, 0.7551020408163266, 0.8791208791208791, 0.7628865979381444, 0.8842105263157894, 0.7676767676767677, 0.8659793814432989, 0.836734693877551, 0.8041237113402061, 0.7959183673469388, 0.875, 0.9032258064516129, 0.8865979381443299, 0.8958333333333334, 0.75, 0.8659793814432989, 0.8686868686868686, 0.9166666666666666, 0.8659793814432989, 0.7916666666666666, 0.8400000000000001, 0.8958333333333334, 0.8817204301075269, 0.7628865979381444, 0.7272727272727272, 0.86, 0.9166666666666666, 0.8, 0.7959183673469388, 0.9375, 0.9278350515463918, 0.8571428571428572, 0.8979591836734694, 0.8979591836734694, 0.8936170212765957, 0.9032258064516129, 0.8723404255319149, 0.8865979381443299, 0.875, 0.888888888888889, 0.9166666666666666, 0.8200000000000001, 0.8865979381443299, 0.8723404255319149, 0.712871287128713, 0.8686868686868686, 0.7692307692307692, 0.7920792079207922, 0.8910891089108911, 0.8631578947368421, 0.712871287128713, 0.8817204301075269, 0.8958333333333334, 0.816326530612245, 0.8865979381443299, 0.8602150537634408, 0.8387096774193549, 0.7676767676767677, 0.8421052631578947, 0.823529411764706, 0.7835051546391752, 0.9148936170212766, 0.851063829787234, 0.787878787878788, 0.8958333333333334, 0.7959183673469388, 0.7835051546391752, 0.8, 0.9278350515463918, 0.737864077669903, 0.8571428571428572, 0.78, 0.8080808080808081, 0.875, 0.6813186813186812, 0.7766990291262137, 0.8936170212765957, 0.888888888888889, 0.8514851485148515, 0.7647058823529411, 0.9166666666666666, 0.8775510204081632, 0.7572815533980584, 0.7809523809523811, 0.8775510204081632, 0.7, 0.9072164948453607, 0.875, 0.8979591836734694, 0.8400000000000001, 0.6595744680851064, 0.78, 0.7835051546391752, 0.8631578947368421, 0.9032258064516129, 0.8421052631578947, 0.7835051546391752, 0.8695652173913043, 0.8979591836734694, 0.9052631578947369, 0.875, 0.7659574468085107, 0.7692307692307692, 0.76, 0.8247422680412372, 0.8775510204081632, 0.9166666666666666, 0.8631578947368421, 0.8631578947368421, 0.8958333333333334, 0.787878787878788, 0.7391304347826088, 0.9263157894736843, 0.787878787878788, 0.7450980392156864, 0.7916666666666666, 0.8421052631578947, 0.8842105263157894, 0.7272727272727272, 0.8958333333333334, 0.7961165048543689, 0.888888888888889, 0.8080808080808081, 0.8865979381443299, 0.7526881720430108, 0.7628865979381444, 0.8958333333333334, 0.7755102040816326, 0.8541666666666666, 0.7647058823529411, 0.8039215686274509, 0.7450980392156864, 0.8842105263157894, 0.8791208791208791, 0.7578947368421053, 0.875, 0.7959183673469388, 0.8842105263157894, 0.9263157894736843, 0.7835051546391752, 0.8571428571428572, 0.8514851485148515, 0.8842105263157894, 0.8842105263157894, 0.7920792079207922, 0.8936170212765957, 0.9166666666666666, 0.7474747474747475, 0.7157894736842105, 0.8913043478260869, 0.8958333333333334, 0.8865979381443299, 0.9032258064516129, 0.8080808080808081, 0.9090909090909091, 0.9052631578947369, 0.8282828282828283, 0.8865979381443299, 0.8775510204081632, 0.9090909090909091, 0.9052631578947369, 0.8484848484848485, 0.8659793814432989, 0.8333333333333334, 0.8865979381443299, 0.7884615384615384, 0.8775510204081632, 0.8659793814432989, 0.8775510204081632, 0.78, 0.86, 0.8865979381443299, 0.8958333333333334, 0.8695652173913043, 0.7450980392156864, 0.8979591836734694, 0.8958333333333334, 0.875, 0.823529411764706, 0.8823529411764706, 0.8865979381443299, 0.7961165048543689, 0.8421052631578947, 0.8282828282828283, 0.811881188118812, 0.845360824742268, 0.9090909090909091, 0.8659793814432989, 0.9090909090909091, 0.9072164948453607, 0.8842105263157894, 0.7755102040816326, 0.875, 0.9072164948453607, 0.7843137254901961, 0.8333333333333334, 0.8817204301075269, 0.8865979381443299, 0.811881188118812, 0.9052631578947369, 0.8541666666666666, 0.7999999999999999, 0.9278350515463918, 0.9052631578947369, 0.7722772277227722, 0.6938775510204083, 0.8865979381443299, 0.7157894736842105, 0.8297872340425533, 0.9263157894736843, 0.7450980392156864, 0.8979591836734694, 0.9148936170212766, 0.875, 0.8316831683168316, 0.9183673469387755, 0.7628865979381444, 0.7422680412371135, 0.8842105263157894, 0.8958333333333334, 0.7346938775510204, 0.7572815533980584, 0.7551020408163266, 0.875, 0.8842105263157894, 0.8085106382978724, 0.7628865979381444, 0.7450980392156864, 0.6732673267326733, 0.8723404255319149, 0.7551020408163266, 0.9052631578947369, 0.712871287128713, 0.8842105263157894, 0.8817204301075269, 0.8627450980392156, 0.8842105263157894, 0.8316831683168316, 0.8571428571428572, 0.8842105263157894, 0.7524752475247525, 0.8958333333333334, 0.8865979381443299, 0.76, 0.8041237113402061, 0.8200000000000001, 0.888888888888889, 0.8775510204081632, 0.9072164948453607, 0.75, 0.7959183673469388, 0.8842105263157894, 0.8602150537634408, 0.7835051546391752, 0.8631578947368421, 0.8842105263157894, 0.9072164948453607, 0.8723404255319149, 0.7835051546391752, 0.8936170212765957, 0.9072164948453607, 0.8979591836734694, 0.8865979381443299, 0.8775510204081632, 0.8514851485148515, 0.8631578947368421, 0.9130434782608695, 0.8842105263157894, 0.8659793814432989, 0.7676767676767677, 0.8400000000000001, 0.8484848484848485, 0.8400000000000001, 0.9183673469387755, 0.8125, 0.8979591836734694, 0.8958333333333334, 0.76, 0.7142857142857142, 0.8541666666666666, 0.7722772277227722, 0.8979591836734694, 0.8958333333333334, 0.8627450980392156, 0.8775510204081632, 0.8571428571428572, 0.8817204301075269, 0.7272727272727272, 0.7755102040816326, 0.811881188118812, 0.7766990291262137, 0.9072164948453607, 0.875, 0.7843137254901961, 0.8659793814432989, 0.7326732673267327, 0.8817204301075269, 0.8723404255319149, 0.7959183673469388, 0.8695652173913043, 0.9072164948453607, 0.78, 0.8421052631578947, 0.9166666666666666, 0.7789473684210526, 0.8247422680412372, 0.8865979381443299, 0.875, 0.8775510204081632, 0.8979591836734694, 0.875, 0.8, 0.8775510204081632, 0.9032258064516129, 0.8936170212765957, 0.7676767676767677, 0.8958333333333334, 0.8155339805825242, 0.875, 0.7676767676767677, 0.9032258064516129, 0.712871287128713, 0.8155339805825242, 0.7676767676767677, 0.75, 0.7872340425531915, 0.8842105263157894, 0.8333333333333334, 0.888888888888889, 0.7446808510638298, 0.8602150537634408, 0.7708333333333333, 0.7708333333333333, 0.702127659574468, 0.8484848484848485, 0.8842105263157894, 0.9052631578947369, 0.845360824742268, 0.7835051546391752, 0.7999999999999999, 0.7474747474747475, 0.8080808080808081, 0.8842105263157894, 0.8958333333333334, 0.8799999999999999, 0.8865979381443299, 0.8958333333333334, 0.8659793814432989, 0.7096774193548386, 0.7474747474747475, 0.8979591836734694, 0.7809523809523811, 0.7959183673469388, 0.8842105263157894, 0.8039215686274509, 0.787878787878788, 0.8080808080808081, 0.76, 0.8817204301075269, 0.9, 0.8791208791208791, 0.8400000000000001, 0.8979591836734694, 0.8, 0.86, 0.7692307692307692, 0.8799999999999999, 0.8842105263157894, 0.8478260869565218, 0.8602150537634408, 0.7735849056603773, 0.8958333333333334, 0.8571428571428572, 0.8666666666666666, 0.8958333333333334, 0.8041237113402061, 0.8659793814432989, 0.9052631578947369, 0.6947368421052632, 0.8, 0.8723404255319149, 0.8979591836734694, 0.7692307692307692, 0.8913043478260869, 0.7083333333333334, 0.8723404255319149, 0.7708333333333333, 0.787878787878788, 0.8627450980392156, 0.816326530612245, 0.845360824742268, 0.7628865979381444, 0.8799999999999999, 0.9032258064516129, 0.7346938775510204, 0.888888888888889, 0.7722772277227722, 0.7291666666666665, 0.7326732673267327, 0.8799999999999999, 0.8541666666666666, 0.787878787878788, 0.787878787878788, 0.7058823529411765, 0.875, 0.9166666666666666, 0.8297872340425533, 0.7809523809523811, 0.7959183673469388, 0.8865979381443299, 0.8842105263157894, 0.8282828282828283, 0.8723404255319149, 0.8979591836734694, 0.811881188118812, 0.7959183673469388, 0.836734693877551, 0.9090909090909091, 0.8541666666666666, 0.8979591836734694, 0.8775510204081632, 0.7572815533980584, 0.8958333333333334, 0.9278350515463918, 0.8842105263157894, 0.74, 0.8421052631578947, 0.8484848484848485, 0.9166666666666666, 0.8979591836734694, 0.7659574468085107, 0.8958333333333334, 0.8817204301075269, 0.8723404255319149, 0.9052631578947369, 0.74, 0.8799999999999999, 0.875, 0.8842105263157894, 0.787878787878788, 0.816326530612245, 0.8686868686868686, 0.8514851485148515, 0.8039215686274509, 0.8541666666666666, 0.8913043478260869, 0.9052631578947369, 0.7199999999999999, 0.851063829787234, 0.9263157894736843, 0.75, 0.8514851485148515, 0.8686868686868686, 0.845360824742268, 0.9072164948453607, 0.8723404255319149, 0.7474747474747475, 0.86, 0.8958333333333334, 0.8842105263157894, 0.9263157894736843, 0.8659793814432989, 0.8659793814432989, 0.9, 0.8936170212765957, 0.8200000000000001, 0.7920792079207922, 0.74, 0.851063829787234, 0.76, 0.836734693877551, 0.8865979381443299, 0.8659793814432989, 0.8712871287128713, 0.9072164948453607, 0.8155339805825242, 0.811881188118812, 0.7524752475247525, 0.875, 0.8842105263157894, 0.8865979381443299, 0.7999999999999999, 0.7216494845360826, 0.7659574468085107, 0.8039215686274509, 0.9183673469387755, 0.7578947368421053, 0.8723404255319149, 0.8958333333333334, 0.723404255319149, 0.8979591836734694, 0.888888888888889, 0.9052631578947369, 0.7326732673267327, 0.811881188118812, 0.7254901960784315, 0.8958333333333334, 0.8936170212765957, 0.7835051546391752, 0.8282828282828283, 0.8297872340425533, 0.7446808510638298, 0.8865979381443299, 0.9072164948453607, 0.8349514563106797, 0.7628865979381444, 0.8571428571428572, 0.8659793814432989, 0.9148936170212766, 0.8602150537634408, 0.8541666666666666, 0.9072164948453607, 0.9072164948453607, 0.8659793814432989, 0.8958333333333334, 0.7647058823529411, 0.7676767676767677, 0.8775510204081632, 0.7311827956989247, 0.8799999999999999, 0.8842105263157894, 0.8659793814432989, 0.8936170212765957, 0.8602150537634408, 0.7578947368421053, 0.7524752475247525, 0.7157894736842105, 0.7628865979381444, 0.8037383177570093]

#cancer
fscores =[0.9302325581395349, 0.5477707006369427, 0.0, 0.0, 0.868421052631579, 0.9647058823529412, 0.35000000000000003, 0.0, 0.0, 0.523076923076923, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9382716049382717, 0.9397590361445783, 0.9382716049382717, 0.0, 0.963855421686747, 0.9411764705882352, 0.9411764705882352, 1.0, 0.0, 0.9249999999999999, 0.9523809523809524, 0.9647058823529412, 0.0, 0.0, 0.0, 0.9285714285714286, 0.0, 0.9113924050632911, 0.8831168831168831, 0.5657894736842105, 0.9523809523809524, 0.0, 0.8533333333333333, 0.0, 0.0, 0.08695652173913045, 0.0, 0.0, 0.8974358974358974, 0.0, 0.9113924050632911, 0.9382716049382717, 0.0, 0.9523809523809524, 0.9761904761904763, 0.8378378378378378, 0.9761904761904763, 0.0, 0.0, 0.9523809523809524, 0.2972972972972973, 0.9647058823529412, 0.759493670886076, 0.7714285714285715, 0.9382716049382717, 0.0, 0.9249999999999999, 0.0, 0.9523809523809524, 0.8974358974358974, 0.0, 0.0, 0.0, 0.9647058823529412, 0.8378378378378378, 0.0, 0.0, 0.9411764705882352, 0.0, 0.0, 0.0, 0.9113924050632911, 0.0, 0.0, 0.9655172413793104, 0.8333333333333333, 0.9534883720930233, 0.0, 0.9302325581395349, 0.963855421686747, 0.9249999999999999, 0.04545454545454545, 0.0, 0.5901639344262295, 0.9885057471264368, 0.08888888888888888, 0.988235294117647, 0.676923076923077, 0.0, 0.13043478260869565, 0.963855421686747, 0.0, 0.951219512195122, 0.08888888888888888, 0.9135802469135803, 0.9767441860465116, 0.9523809523809524, 0.0, 0.04545454545454545, 0.8974358974358974, 0.0, 0.0, 0.0, 0.9761904761904763, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9767441860465116, 0.0, 0.0, 0.0, 0.04545454545454545, 0.963855421686747, 0.0, 0.0, 0.0, 0.0, 0.0, 0.7555555555555555, 0.0, 0.0, 0.9411764705882352, 0.20833333333333334, 0.9534883720930233, 0.951219512195122, 0.0, 0.65625, 0.9069767441860465, 0.0, 0.9523809523809524, 0.0, 0.0, 0.0, 0.0, 0.5423728813559322, 0.9662921348314606, 0.9647058823529412, 0.0, 0.0, 0.9647058823529412, 0.9113924050632911, 0.0, 0.9534883720930233, 0.9523809523809524, 0.08695652173913045, 0.963855421686747, 0.951219512195122, 0.9655172413793104, 0.0, 0.9655172413793104, 0.0, 0.9318181818181819, 0.0, 0.0, 0.0, 0.0, 0.9397590361445783, 0.0, 0.0, 0.9411764705882352, 0.8266666666666667, 0.9302325581395349, 0.0, 0.0, 0.7889908256880734, 0.988235294117647, 0.0, 0.9285714285714286, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.1702127659574468, 0.9382716049382717, 0.0, 0.0, 0.9411764705882352, 0.0, 0.7727272727272727, 0.0, 0.988235294117647, 0.0, 0.0, 0.9647058823529412, 0.0, 0.0, 0.0, 0.7945205479452055, 0.7887323943661972, 0.0, 0.0, 0.24489795918367346, 0.8055555555555556, 0.875, 0.9285714285714286, 0.9761904761904763, 0.9523809523809524, 0.9523809523809524, 0.9249999999999999, 0.9397590361445783, 0.0, 0.9767441860465116, 0.0, 0.0, 0.9647058823529412, 0.0, 0.0, 0.0, 0.0, 0.65625, 0.9156626506024096, 0.9411764705882352, 0.0, 0.0, 0.45238095238095233, 0.9302325581395349, 0.0, 0.0, 0.0, 0.9397590361445783, 0.0, 0.0, 0.0, 0.0, 0.951219512195122, 0.0, 0.9176470588235294, 0.0, 0.0, 0.9523809523809524, 0.9249999999999999, 0.9156626506024096, 0.9397590361445783, 0.0, 0.0, 0.8431372549019608, 0.9523809523809524, 0.9268292682926831, 0.9772727272727273, 0.9534883720930233, 0.0, 0.0, 0.0, 0.963855421686747, 0.0, 0.951219512195122, 0.5666666666666667, 0.0, 0.924731182795699, 0.9655172413793104, 0.0, 0.0, 0.04545454545454545, 0.0, 0.0, 0.0, 0.9135802469135803, 0.0, 0.0, 0.0, 0.9523809523809524, 0.868421052631579, 0.9438202247191011, 0.0, 0.9397590361445783, 0.0, 0.0, 0.942528735632184, 0.0, 0.0, 0.0, 0.9647058823529412, 0.0, 0.7547169811320754, 0.0, 0.9249999999999999, 0.0, 0.963855421686747, 0.0, 0.5423728813559322, 0.942528735632184, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.951219512195122, 0.9647058823529412, 0.9523809523809524, 0.04545454545454545, 0.9113924050632911, 0.7887323943661972, 0.0, 0.0, 0.9176470588235294, 0.9767441860465116, 0.9523809523809524, 0.0, 0.0, 0.0, 0.8958333333333334, 0.9411764705882352, 0.0, 0.0, 0.0, 0.9647058823529412, 0.0, 0.0, 0.9523809523809524, 0.0, 0.2894736842105263, 0.9523809523809524, 0.9647058823529412, 0.9662921348314606, 0.9397590361445783, 0.0, 0.9411764705882352, 0.0, 0.0, 0.988235294117647, 0.32432432432432434, 0.759493670886076, 0.9397590361445783, 0.0, 0.9647058823529412, 0.9523809523809524, 0.9249999999999999, 0.8533333333333333, 0.0, 0.3658536585365854, 0.0, 0.0, 0.0, 0.0, 0.951219512195122, 0.0, 0.9382716049382717, 0.0, 0.0, 0.9249999999999999, 0.0, 0.8831168831168831, 0.9534883720930233, 0.9655172413793104, 0.0, 0.0, 0.9024390243902439, 0.0, 0.0, 0.0, 0.9382716049382717, 0.0, 0.9534883720930233, 0.0, 0.9523809523809524, 0.0, 0.9523809523809524, 0.9647058823529412, 0.0, 0.988235294117647, 0.3380281690140845, 0.9249999999999999, 0.9047619047619047, 0.9534883720930233, 0.0, 0.0, 0.9885057471264368, 0.0, 0.9523809523809524, 0.0, 0.0, 0.0, 0.0, 0.8974358974358974, 0.0, 0.8831168831168831, 0.0, 0.0, 0.0, 0.08888888888888888, 0.08888888888888888, 0.9655172413793104, 0.9647058823529412, 0.8378378378378378, 0.963855421686747, 0.9647058823529412, 0.9534883720930233, 0.9761904761904763, 0.9397590361445783, 0.0, 0.0, 0.9411764705882352, 0.9382716049382717, 0.9647058823529412, 0.9285714285714286, 0.0, 0.9545454545454545, 0.0, 1.0, 0.9534883720930233, 0.5901639344262295, 0.0, 0.0, 0.0, 0.9523809523809524, 0.0, 0.0, 0.0, 0.9647058823529412, 0.35294117647058815, 0.0, 0.0, 1.0, 0.9302325581395349, 0.0, 0.9647058823529412, 0.9130434782608695, 0.676923076923077, 0.0, 0.9885057471264368, 0.9397590361445783, 0.9411764705882352, 0.0, 0.0, 0.9767441860465116, 0.0, 0.9767441860465116, 0.0, 0.8157894736842105, 0.24489795918367346, 0.9647058823529412, 0.0, 0.0, 0.9523809523809524, 0.379746835443038, 0.0, 0.988235294117647, 0.0, 0.0, 0.8831168831168831, 0.0, 0.9767441860465116, 0.8349514563106796, 0.0, 0.0, 0.9885057471264368, 0.963855421686747, 0.0, 0.9249999999999999, 0.0, 0.0, 0.9438202247191011, 0.963855421686747, 0.5172413793103449, 0.0, 0.0, 0.9318181818181819, 0.0, 0.951219512195122, 0.04545454545454545, 0.963855421686747, 0.0, 0.9333333333333332, 0.0, 0.0, 0.0, 0.33333333333333337, 0.9761904761904763, 0.951219512195122, 0.0, 0.0, 0.9, 0.0, 0.0, 0.37142857142857144, 0.9411764705882352, 0.0, 0.0, 0.0, 0.523076923076923, 0.9249999999999999, 0.9268292682926831, 0.9156626506024096, 0.9397590361445783, 0.0, 0.46428571428571425, 0.0, 0.9397590361445783, 0.9382716049382717, 0.0, 0.9655172413793104, 0.0, 0.0, 0.0, 0.9285714285714286, 0.8533333333333333, 0.9523809523809524, 0.0, 0.0, 0.9397590361445783, 0.8974358974358974, 0.0, 0.7536231884057971, 0.9761904761904763, 0.9647058823529412, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 0.0, 0.0, 0.0, 0.08695652173913045, 0.8974358974358974, 0.0, 0.0, 0.0, 0.0, 0.951219512195122, 0.0, 0.08888888888888888, 0.6969696969696969, 0.0, 0.0, 0.0, 0.891566265060241, 0.9523809523809524, 0.942528735632184, 0.0, 0.9302325581395349, 0.0, 0.9285714285714286, 0.0, 0.43636363636363634, 0.0, 0.8974358974358974, 0.0, 0.5901639344262295, 0.2898550724637681, 0.9647058823529412, 0.0, 0.35294117647058815, 0.6187050359712231, 0.0, 0.9761904761904763, 0.0, 0.36111111111111105, 0.0, 0.0, 0.0, 0.0, 0.9655172413793104, 0.1702127659574468, 0.08888888888888888, 0.0, 0.0, 0.9534883720930233, 0.7476635514018692, 0.9647058823529412, 0.676923076923077, 0.0, 0.0, 0.0, 0.9523809523809524, 0.9135802469135803, 0.0, 0.0, 0.9382716049382717, 0.9397590361445783, 0.0, 0.9647058823529412, 0.9285714285714286, 0.9523809523809524, 0.0, 0.04545454545454545, 0.0, 0.0, 0.0, 0.9411764705882352, 0.9382716049382717, 0.0, 0.9523809523809524, 0.9285714285714286, 0.9411764705882352, 0.0, 0.0, 0.0, 0.9523809523809524, 0.0, 0.0, 0.9382716049382717, 0.0, 0.0, 0.9382716049382717, 0.9761904761904763, 0.0, 0.0, 0.9523809523809524, 0.988235294117647, 0.9397590361445783, 0.0, 0.9411764705882352, 0.0, 0.0, 0.988235294117647, 0.9382716049382717, 0.8210526315789475, 0.9767441860465116, 0.04545454545454545, 0.9176470588235294, 0.0, 0.9397590361445783, 0.0, 0.0, 0.0, 0.9647058823529412]



# the histogram of the data
n, bins, patches = plt.hist(fscores, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Fscore')
plt.ylabel('Number of Feature Representations')
plt.title('Histogram of Running ' + str(len(fscores)) + " random feature representations")

#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()