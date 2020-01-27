import matplotlib.pyplot as plt
import numpy as np


def plot_it(skyline, name, dashed=False):
	skyline_a = np.array(skyline)
	ids = np.argsort(skyline_a[:,0])

	line = plt.plot(skyline_a[ids, 0], skyline_a[ids, 1], label=name)
	if dashed:
		plt.setp(line, linestyle='--')



weighted_ranking_sky =[[0.8669333333333333, 0.7007142857142857], [0.9130666666666667, 0.6326587301587301], [0.9001333333333335, 0.6947619047619048], [0.90896614069691, 0.6822619047619047], [0.9098290598290598, 0.6632142857142858], [0.8475999999999999, 0.7118253968253968]]
times= [46.41842865943909, 58.12263059616089, 76.68611001968384, 88.09023427963257, 172.2991237640381, 247.9971466064453]
iterations= [73, 92, 120, 139, 272, 394]
plot_it(weighted_ranking_sky, 'weighted ranking')

fairness_sky =[[0.9122666666666667, 0.5965873015873016], [0.9114666666666666, 0.6096428571428572], [0.9069333333333334, 0.6632142857142858], [0.9074666666666666, 0.6471428571428571]]
times= [5.478947401046753, 18.53501272201538, 21.22649049758911, 26.280875205993652]
iterations= [8, 28, 32, 40]
plot_it(fairness_sky, 'fairness ranking')

acc_sky =[[0.9053994082840238, 0.6632142857142858], [0.8669333333333333, 0.7007142857142857], [0.9001333333333335, 0.6947619047619048], [0.9073635765943457, 0.6239285714285714], [0.9066666666666666, 0.6346428571428571]]
times= [1.7637531757354736, 3.486793041229248, 4.052125930786133, 7.005539894104004, 16.646475553512573]
iterations= [3, 6, 7, 12, 28]
plot_it(acc_sky, 'accuracy ranking')

var_sky =[[0.8558666666666668, 0.671984126984127], [0.9032, 0.6489285714285714]]
times= [9.723489046096802, 13.603410720825195]
iterations= [15, 20]
plot_it(var_sky, 'variance ranking')

evolution_sky = [[0.9070348454963838, 0.6775], [0.8515861275476659, 0.8217460317460318], [0.8914666666666666, 0.7427777777777778], [0.8779010519395136, 0.7917857142857143], [0.9056000000000001, 0.709047619047619], [0.9013333333333333, 0.7374078624078624], [0.8696252465483235, 0.8074603174603174], [0.8757396449704142, 0.7942260442260443], [0.9080785667324129, 0.6632142857142858], [0.8621219592373439, 0.8212530712530712], [0.9064, 0.6923809523809523], [0.8482666666666666, 0.8292857142857143], [0.8463999999999999, 0.8439803439803439], [0.9159999999999999, 0.6405952380952381], [0.8893333333333333, 0.7871621621621622], [0.8749671268902037, 0.8055896805896806]]
times= [1.15816068649292, 76.64327383041382, 96.84419393539429, 110.4859447479248, 271.4974932670593, 286.52747774124146, 296.20880365371704, 303.1251292228699, 304.9045765399933, 339.95813035964966, 474.3665041923523, 489.18617510795593, 530.3019866943359, 563.9682495594025, 568.9313464164734, 608.1914708614349]
iterations= [2, 123, 157, 180, 433, 458, 475, 487, 490, 544, 763, 789, 855, 909, 917, 984]
plot_it(evolution_sky, 'evolution')


hyperopt_sky = [[0.8485333333333334, 0.8167857142857142], [0.8947978303747537, 0.7275], [0.9002666666666667, 0.7132142857142857], [0.9098666666666667, 0.6798809523809524], [0.9102399737015121, 0.6548809523809523], [0.8632, 0.7828624078624078], [0.854922748191979, 0.7949603174603175], [0.9008, 0.6989285714285715], [0.8373333333333334, 0.8326167076167077], [0.8644970414201183, 0.7714987714987716], [0.8564, 0.7838492063492064]]
times= [24.636295080184937, 41.53310251235962, 53.19852066040039, 58.83807635307312, 70.95686864852905, 79.17749071121216, 81.17008543014526, 84.38197112083435, 105.73924255371094, 123.59719800949097, 447.65887236595154]
iterations= [37, 63, 80, 89, 108, 121, 124, 129, 162, 189, 657]
plot_it(hyperopt_sky, 'hyperparameter opt.')


plt.xlabel('AUC (Accuracy)')
plt.ylabel('Fairness')

plt.legend()
plt.show()
