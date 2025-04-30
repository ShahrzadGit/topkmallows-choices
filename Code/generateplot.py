import numpy as np 
import matplotlib.pyplot as plt
"""
#beta=0.3
Ly=[np.float64(0.5900000000000001), np.float64(0.5799999999999998), np.float64(0.77), np.float64(0.73), np.float64(0.77), np.float64(0.78), np.float64(0.8300000000000001), np.float64(0.8400000000000001), np.float64(0.8300000000000001), np.float64(0.86), np.float64(0.8100000000000002), np.float64(0.8), np.float64(0.8400000000000001), np.float64(0.8800000000000001), np.float64(0.8200000000000001), np.float64(0.9200000000000002), np.float64(0.8600000000000001), np.float64(0.8800000000000001), np.float64(0.8800000000000001), np.float64(0.9400000000000001), np.float64(0.9099999999999999), np.float64(0.9100000000000001), np.float64(0.8800000000000001), np.float64(0.9), np.float64(0.8400000000000001), np.float64(0.8700000000000001), np.float64(0.9), np.float64(0.95), np.float64(0.9099999999999999), np.float64(0.89), np.float64(0.95), np.float64(0.89), np.float64(0.9399999999999998), np.float64(0.93), np.float64(0.9200000000000002), np.float64(0.89), np.float64(0.9199999999999999), np.float64(0.9), np.float64(0.8799999999999999), np.float64(0.9200000000000002), np.float64(0.9199999999999999), np.float64(0.9), np.float64(0.95), np.float64(0.9099999999999999), np.float64(0.9), np.float64(0.9200000000000002), np.float64(0.9199999999999999), np.float64(0.9199999999999999), np.float64(0.97), np.float64(0.89)] 
Lv=[np.float64(0.1445683229480096), np.float64(0.132664991614216), np.float64(0.15524174696260024), np.float64(0.12688577540449522), np.float64(0.14866068747318506), np.float64(0.1077032961426901), np.float64(0.14177446878757827), np.float64(0.08000000000000002), np.float64(0.0640312423743285), np.float64(0.10198039027185571), np.float64(0.10440306508910553), np.float64(0.15491933384829668), np.float64(0.12000000000000001), np.float64(0.08717797887081348), np.float64(0.07483314773547885), np.float64(0.059999999999999984), np.float64(0.10198039027185571), np.float64(0.12489995996796799), np.float64(0.08717797887081345), np.float64(0.06633249580710798), np.float64(0.08306623862918076), np.float64(0.08306623862918074), np.float64(0.09797958971132711), np.float64(0.1264911064067352), np.float64(0.11135528725660045), np.float64(0.09), np.float64(0.07745966692414831), np.float64(0.06708203932499368), np.float64(0.11357816691600549), np.float64(0.06999999999999999), np.float64(0.06708203932499367), np.float64(0.06999999999999999), np.float64(0.09165151389911681), np.float64(0.06403124237432847), np.float64(0.09797958971132713), np.float64(0.12206555615733702), np.float64(0.08717797887081347), np.float64(0.10954451150103324), np.float64(0.11661903789690603), np.float64(0.0748331477354788), np.float64(0.08717797887081348), np.float64(0.0894427190999916), np.float64(0.06708203932499368), np.float64(0.11357816691600547), np.float64(0.1), np.float64(0.0748331477354788), np.float64(0.08717797887081348), np.float64(0.08717797887081347), np.float64(0.04582575694955839), np.float64(0.06999999999999999)] 
y_beta3 = np.array(Ly)
v_3= np.array(Lv)

#beta=0.4
Ly=[np.float64(0.6799999999999999), np.float64(0.77), np.float64(0.82), np.float64(0.8099999999999999), np.float64(0.8400000000000001), np.float64(0.86), np.float64(0.93), np.float64(0.9200000000000002), np.float64(0.9100000000000001), np.float64(0.9199999999999999), np.float64(0.89), np.float64(0.9400000000000001), np.float64(0.9400000000000001), np.float64(0.93), np.float64(0.96), np.float64(0.95), np.float64(0.93), np.float64(0.93), np.float64(0.99), np.float64(0.9099999999999999), np.float64(1.0), np.float64(0.95), np.float64(0.9800000000000001), np.float64(0.9800000000000001), np.float64(1.0), np.float64(0.97), np.float64(0.9800000000000001), np.float64(0.99), np.float64(0.9800000000000001), np.float64(1.0), np.float64(1.0), np.float64(0.97), np.float64(1.0), np.float64(0.9800000000000001), np.float64(0.99), np.float64(1.0), np.float64(0.99), np.float64(0.9800000000000001), np.float64(1.0), np.float64(0.99), np.float64(0.9800000000000001), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(0.9800000000000001)] 
Lv=[np.float64(0.18330302779823363), np.float64(0.11000000000000001), np.float64(0.132664991614216), np.float64(0.1135781669160055), np.float64(0.11135528725660046), np.float64(0.08), np.float64(0.1004987562112089), np.float64(0.09797958971132713), np.float64(0.11357816691600547), np.float64(0.10770329614269009), np.float64(0.13747727084867523), np.float64(0.06633249580710798), np.float64(0.06633249580710798), np.float64(0.06403124237432847), np.float64(0.06633249580710798), np.float64(0.08062257748298547), np.float64(0.07810249675906653), np.float64(0.09), np.float64(0.029999999999999992), np.float64(0.09433981132056604), np.float64(0.0), np.float64(0.04999999999999999), np.float64(0.05999999999999999), np.float64(0.039999999999999994), np.float64(0.0), np.float64(0.04582575694955839), np.float64(0.039999999999999994), np.float64(0.029999999999999992), np.float64(0.039999999999999994), np.float64(0.0), np.float64(0.0), np.float64(0.04582575694955839), np.float64(0.0), np.float64(0.039999999999999994), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.039999999999999994), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.039999999999999994), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.039999999999999994)] 
y_beta4 = np.array(Ly)
v_4= np.array(Lv)

#beta=0.5
Ly=[np.float64(0.78), np.float64(0.8299999999999998), np.float64(0.8400000000000001), np.float64(0.93), np.float64(0.96), np.float64(0.97), np.float64(0.96), np.float64(0.95), np.float64(0.96), np.float64(1.0), np.float64(0.97), np.float64(0.99), np.float64(0.9800000000000001), np.float64(0.97), np.float64(0.99), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)] 
Lv=[np.float64(0.16), np.float64(0.11874342087037917), np.float64(0.12806248474865697), np.float64(0.07810249675906653), np.float64(0.04898979485566356), np.float64(0.045825756949558386), np.float64(0.04898979485566356), np.float64(0.08062257748298547), np.float64(0.04898979485566354), np.float64(0.0), np.float64(0.045825756949558386), np.float64(0.029999999999999992), np.float64(0.039999999999999994), np.float64(0.06403124237432847), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta5 = np.array(Ly)
v_5= np.array(Lv)

#beta=0.6
Ly=[np.float64(0.8400000000000001), np.float64(0.8800000000000001), np.float64(0.89), np.float64(0.93), np.float64(0.96), np.float64(0.97), np.float64(0.96), np.float64(0.96), np.float64(0.99), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(0.9800000000000001), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)]
Lv=[np.float64(0.12000000000000001), np.float64(0.09797958971132713), np.float64(0.09433981132056604), np.float64(0.07810249675906653), np.float64(0.06633249580710798), np.float64(0.04582575694955839), np.float64(0.04898979485566354), np.float64(0.04898979485566356), np.float64(0.029999999999999992), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.039999999999999994), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta6 = np.array(Ly)
v_6= np.array(Lv)

#beta=0.7
Ly=[np.float64(0.8400000000000001), np.float64(0.9400000000000001), np.float64(0.95), np.float64(0.97), np.float64(1.0), np.float64(0.9800000000000001), np.float64(0.9800000000000001), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)] 
Lv=[np.float64(0.11135528725660046), np.float64(0.10198039027185571), np.float64(0.06708203932499368), np.float64(0.06403124237432847), np.float64(0.0), np.float64(0.039999999999999994), np.float64(0.039999999999999994), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta7 = np.array(Ly)
v_7= np.array(Lv)

#beta=0.8 
Ly=[np.float64(0.95), np.float64(0.99), np.float64(0.9800000000000001), np.float64(0.97), np.float64(0.9800000000000001), np.float64(1.0), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)] 
Lv=[np.float64(0.08062257748298547), np.float64(0.029999999999999992), np.float64(0.05999999999999999), np.float64(0.04582575694955839), np.float64(0.039999999999999994), np.float64(0.0), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta8 = np.array(Ly)
v_8= np.array(Lv)

#beta=0.9
Ly=[np.float64(0.95), np.float64(0.96), np.float64(0.99), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)]
Lv=[np.float64(0.04999999999999999), np.float64(0.06633249580710798), np.float64(0.029999999999999992), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta9 = np.array(Ly)
v_9= np.array(Lv)


#beta=1
Ly=[np.float64(0.97), np.float64(0.9700000000000001), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)] 
Lv=[np.float64(0.045825756949558386), np.float64(0.04582575694955839), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta10 = np.array(Ly)
v_10= np.array(Lv)


#beta=1.1
Ly=[np.float64(0.9800000000000001), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)] 
Lv= [np.float64(0.039999999999999994), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta11 = np.array(Ly)
v_11= np.array(Lv)

#beta=1.2
Ly=[np.float64(0.96), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0), np.float64(1.0)] 
Lv=[np.float64(0.06633249580710798), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta12 = np.array(Ly)
v_12= np.array(Lv)


# plots with variance:

x = np.array(range(10, 510,10))
plt.figure()

plt.errorbar(x, y_beta4, v_4, fmt='o-', capsize=1,color="blue",label="beta=0.4")
plt.errorbar(x, y_beta6, v_6, fmt='o-', capsize=1,color="red",label="beta=0.6")
plt.errorbar(x, y_beta8, v_8, fmt='o-', capsize=1, color="orange",label="beta=0.8")
plt.errorbar(x, y_beta10, v_10, fmt='o-', capsize=1,color="green",label="beta=1")



plt.xlabel("number of samples")
plt.ylabel("accuracy")
plt.legend()

n=1000
k=10
r=8
p=0.5

file_path = f"/Users/sh1678/Dropbox/Research/Mallows/topkmallows-choices/Plots/withvariance_beta:0.4-1_n{n}_k{k}_r{r}_p{p}.png"

plt.savefig(file_path)


# beta=0.8,1,1.2

x = np.array(range(10, 110,10))
plt.figure()

print("sizes",y_beta8[:10].size, x.size)

plt.errorbar(x, y_beta8[:10], v_8[:10], fmt='o-', capsize=1,color="blue",label="beta=0.8")
plt.errorbar(x, y_beta10[:10], v_10[:10], fmt='o-', capsize=1,color="orange",label="beta=1")
plt.errorbar(x, y_beta12[:10], v_12[:10], fmt='o-', capsize=1,color="red",label="beta=1.2")


plt.xlabel("number of samples")
plt.ylabel("accuracy")
plt.legend()

file_path = f"/Users/sh1678/Dropbox/Research/Mallows/topkmallows-choices/Plots/withvariance_beta:0.1-0.2-0.5-1_n{n}_k{k}_r{r}_p{p}.png"

plt.savefig(file_path)

# plots without variance:
plt.figure()
x = np.array(range(10, 510,10))
plt.plot(x, y_beta3, color="purple",label="beta=0.3")
plt.plot(x, y_beta4, color="blue",label="beta=0.4")
plt.plot(x, y_beta5, color="brown",label="beta=0.5")
plt.plot(x, y_beta6,  color="cyan",label="beta=0.6")
plt.plot(x, y_beta7, color="pink",label="beta=0.7")
plt.plot(x, y_beta8,  color="orange",label="beta=0.8")
plt.plot(x, y_beta9, color="yellow",label="beta=0.9")
plt.plot(x, y_beta10,  color="green",label="beta=1")
plt.xlabel("number of samples")
plt.ylabel("accuracy")
plt.legend()

file_path = f"/Users/sh1678/Dropbox/Research/Mallows/topkmallows-choices/Plots/mean_beta_n{n}_k{k}_r{r}_p{p}.png"

plt.savefig(file_path)



######## find center 

n=500
k=10

p=0.5


#sigma: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#sample size array: [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
#beta =  0.4 

#mean of distances:
Ld= [np.float64(1040.85), np.float64(76.95), np.float64(51.65), np.float64(9.25), np.float64(6.3), np.float64(3.45), np.float64(3.0), np.float64(2.55), np.float64(2.9), np.float64(2.3), np.float64(2.4), np.float64(2.5), np.float64(2.2), np.float64(2.4), np.float64(2.3), np.float64(2.3), np.float64(2.2), np.float64(2.1), np.float64(2.1), np.float64(1.8)] 

#variance of distances:
Lv= [np.float64(243.27258887922412), np.float64(24.636811887904653), np.float64(23.87472512930777), np.float64(4.686416541452541), np.float64(3.8418745424597094), np.float64(1.2134661099511597), np.float64(1.4142135623730951), np.float64(1.105667219374799), np.float64(1.3), np.float64(0.9), np.float64(0.8), np.float64(0.9219544457292888), np.float64(0.7483314773547882), np.float64(0.66332495807108), np.float64(0.7810249675906654), np.float64(0.45825756949558405), np.float64(0.6), np.float64(0.7), np.float64(0.8306623862918076), np.float64(1.077032961426901)] 

y_beta04 = np.array(Ld[1:10])
v_04= np.array(Lv[1:10])

#beta =  0.6000000000000001 

#mean of distances:
Ld= [np.float64(1023.15), np.float64(90.2), np.float64(32.6), np.float64(5.7), np.float64(2.25), np.float64(0.4), np.float64(0.5), np.float64(0.6), np.float64(0.5), np.float64(0.2), np.float64(0.2), np.float64(0.0), np.float64(0.1), np.float64(0.2), np.float64(0.3), np.float64(0.2), np.float64(0.0), np.float64(0.1), np.float64(0.1), np.float64(0.0)] 

#variance of distances:
Lv= [np.float64(253.02530011838738), np.float64(36.46107513499842), np.float64(14.263239463740346), np.float64(3.2109188716004646), np.float64(1.5370426148939398), np.float64(0.48989794855663565), np.float64(0.6708203932499369), np.float64(0.66332495807108), np.float64(0.6708203932499369), np.float64(0.4000000000000001), np.float64(0.4000000000000001), np.float64(0.0), np.float64(0.30000000000000004), np.float64(0.4000000000000001), np.float64(0.45825756949558405), np.float64(0.4000000000000001), np.float64(0.0), np.float64(0.30000000000000004), np.float64(0.30000000000000004), np.float64(0.0)] 


y_beta06 = np.array(Ld[1:10])
v_06= np.array(Lv[1:10])

#beta =  0.8 

#mean of distances:
Ld= [np.float64(995.9), np.float64(84.95), np.float64(38.2), np.float64(6.4), np.float64(4.05), np.float64(0.3), np.float64(0.25), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

#variance of distances:
Lv= [np.float64(186.20631031197624), np.float64(37.852641915723666), np.float64(20.903588208726273), np.float64(3.184336665618132), np.float64(3.467347689517162), np.float64(0.6), np.float64(0.51234753829798), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

y_beta08 = np.array(Ld[1:10])
v_08= np.array(Lv[1:10])

#beta =  1.0 

#mean of distances:
Ld= [np.float64(1079.9), np.float64(79.75), np.float64(42.15), np.float64(4.35), np.float64(2.05), np.float64(0.35), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

#variance of distances:
Lv= [np.float64(239.99477077636502), np.float64(27.201332687940127), np.float64(17.69894064626468), np.float64(3.8408983324217263), np.float64(2.35), np.float64(0.8958236433584458), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

y_beta10 = np.array(Ld[1:10])
v_10= np.array(Lv[1:10])


#beta =  1.2000000000000002 

#mean of distances:
Ld= [np.float64(1091.35), np.float64(72.6), np.float64(41.95), np.float64(2.75), np.float64(3.75), np.float64(0.25), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

#variance of distances:
Lv= [np.float64(220.264278765305), np.float64(24.527331693439464), np.float64(22.926458514127297), np.float64(3.0186917696247164), np.float64(2.0766559657295187), np.float64(0.4609772228646444), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

y_beta12 = np.array(Ld[1:10])
v_12= np.array(Lv[1:10])
"""


#sigma: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#sample size array: [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
#beta =  0.4 

n=1500
k=16
p=0.5


#mean of distances:
Ld= [np.float64(9264.45), np.float64(905.85), np.float64(360.8), np.float64(46.75), np.float64(29.3), np.float64(9.25), np.float64(6.2), np.float64(4.0), np.float64(4.6), np.float64(3.6), np.float64(3.7), np.float64(5.1), np.float64(4.0), np.float64(3.4), np.float64(3.8), np.float64(4.1), np.float64(4.5), np.float64(3.4), np.float64(3.9), np.float64(3.1)] 

#variance of distances:
Lv= [np.float64(1073.16910247174), np.float64(255.37032423521728), np.float64(50.31858503574996), np.float64(17.67378001447342), np.float64(17.231076576929254), np.float64(3.43693177121688), np.float64(1.5524174696260022), np.float64(1.6733200530681511), np.float64(0.8306623862918076), np.float64(0.66332495807108), np.float64(0.7810249675906654), np.float64(1.8681541692269403), np.float64(1.1832159566199232), np.float64(1.019803902718557), np.float64(1.077032961426901), np.float64(0.9433981132056604), np.float64(0.9219544457292888), np.float64(1.0198039027185568), np.float64(1.1357816691600549), np.float64(1.044030650891055)] 

y_beta04 = np.array(Ld[1:10])
v_04= np.array(Lv[1:10])

#beta =  0.6000000000000001 

#mean of distances:
Ld= [np.float64(9651.1), np.float64(823.45), np.float64(432.95), np.float64(47.05), np.float64(24.5), np.float64(4.1), np.float64(1.3), np.float64(0.8), np.float64(0.6), np.float64(0.55), np.float64(0.5), np.float64(0.0), np.float64(0.3), np.float64(0.2), np.float64(0.3), np.float64(0.1), np.float64(0.5), np.float64(0.1), np.float64(0.0), np.float64(0.0)] 

#variance of distances:
Lv= [np.float64(992.7163441789401), np.float64(164.30375071799182), np.float64(131.98550109765844), np.float64(11.763184092753118), np.float64(17.00441119239358), np.float64(2.2449944320643644), np.float64(1.004987562112089), np.float64(0.8717797887081347), np.float64(0.66332495807108), np.float64(0.5678908345800274), np.float64(0.6708203932499369), np.float64(0.0), np.float64(0.45825756949558394), np.float64(0.4000000000000001), np.float64(0.45825756949558405), np.float64(0.30000000000000004), np.float64(0.5), np.float64(0.30000000000000004), np.float64(0.0), np.float64(0.0)] 

y_beta06 = np.array(Ld[1:10])
v_06= np.array(Lv[1:10])

#beta =  0.8 

#mean of distances:
Ld= [np.float64(10467.9), np.float64(894.6), np.float64(445.4), np.float64(61.5), np.float64(21.6), np.float64(2.6), np.float64(0.9), np.float64(0.35), np.float64(0.1), np.float64(0.0), np.float64(0.0), np.float64(0.1), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

#variance of distances:
Lv= [np.float64(1486.3464232809254), np.float64(169.73874042186125), np.float64(138.17485299431297), np.float64(17.725687574816384), np.float64(11.835962149314266), np.float64(3.462657938636157), np.float64(1.1357816691600549), np.float64(0.5024937810560445), np.float64(0.20000000000000004), np.float64(0.0), np.float64(0.0), np.float64(0.30000000000000004), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 
y_beta08 = np.array(Ld[1:10])
v_08= np.array(Lv[1:10])


#beta =  1.0 

#mean of distances:
Ld= [np.float64(9304.95), np.float64(1068.55), np.float64(412.1), np.float64(47.2), np.float64(22.9), np.float64(3.55), np.float64(1.65), np.float64(0.1), np.float64(0.25), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

#variance of distances:
Lv= [np.float64(1395.8814858361006), np.float64(205.4181649708711), np.float64(99.30679735043317), np.float64(28.67594810987075), np.float64(14.703400967123219), np.float64(3.2361242250568814), np.float64(2.236626924634504), np.float64(0.20000000000000004), np.float64(0.4609772228646444), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

y_beta10 = np.array(Ld[1:10])
v_10= np.array(Lv[1:10])

#beta =  1.2000000000000002 

#mean of distances:
Ld= [np.float64(9995.55), np.float64(896.8), np.float64(378.25), np.float64(48.7), np.float64(20.75), np.float64(2.8), np.float64(0.55), np.float64(0.3), np.float64(0.1), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

#variance of distances:
Lv= [np.float64(1211.8085543929783), np.float64(295.23517744333924), np.float64(154.35757998880393), np.float64(24.653802952080234), np.float64(13.33651003823714), np.float64(2.951270912674741), np.float64(0.8500000000000001), np.float64(0.45825756949558405), np.float64(0.20000000000000004), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)] 

y_beta12 = np.array(Ld[1:10])
v_12= np.array(Lv[1:10])

#sample_sizes=[20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
sample_sizes=[40, 60, 80, 100, 120, 140, 160, 180, 200]
#, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]

x = np.array(sample_sizes)



plt.figure()

plt.plot(x, y_beta04, label='beta=0.4', color='blue')
plt.fill_between(x, y_beta04 - v_04, y_beta04 + v_04, color='blue', alpha=0.1)
#plt.plot(x, y_beta06, label='beta=0.6', color='cyan')
#plt.fill_between(x, y_beta06 - v_06, y_beta06 + v_06, color='cyan', alpha=0.1)
plt.plot(x, y_beta08, label='beta=0.8', color='red')
plt.fill_between(x, y_beta08 - v_08, y_beta08 + v_08, color='red', alpha=0.1)
#plt.plot(x, y_beta10, label='beta=1', color='orange')
#plt.fill_between(x, y_beta10 - v_10, y_beta10 + v_10, color='orange', alpha=0.1)
plt.plot(x, y_beta12, label='beta=1.2', color='green')
plt.fill_between(x, y_beta12 - v_12, y_beta12 + v_12, color='green', alpha=0.1)



plt.xlabel("number of samples")
plt.ylabel("distance of true center and learned center")
plt.legend()

file_path = f"/Users/sh1678/Dropbox/Research/Mallows/topkmallows-choices/Plots/findcenter_newformat_evenbetas_n{n}_k{k}__p{p}.png"

plt.savefig(file_path)


plt.figure()

#plt.plot(x, y_beta04, label='beta=0.4', color='blue')
#plt.fill_between(x, y_beta04 - v_04, y_beta04 + v_04, color='blue', alpha=0.1)
plt.plot(x, y_beta06, label='beta=0.6', color='cyan')
plt.fill_between(x, y_beta06 - v_06, y_beta06 + v_06, color='cyan', alpha=0.1)
#plt.plot(x, y_beta08, label='beta=0.8', color='red')
#plt.fill_between(x, y_beta08 - v_08, y_beta08 + v_08, color='red', alpha=0.1)
plt.plot(x, y_beta10, label='beta=1', color='orange')
plt.fill_between(x, y_beta10 - v_10, y_beta10 + v_10, color='orange', alpha=0.1)
#plt.plot(x, y_beta12, label='beta=1.2', color='green')
#plt.fill_between(x, y_beta12 - v_12, y_beta12 + v_12, color='green', alpha=0.1)



plt.xlabel("number of samples")
plt.ylabel("distance of true center and learned center")
plt.legend()

file_path = f"/Users/sh1678/Dropbox/Research/Mallows/topkmallows-choices/Plots/findcenter_newformat_oddbetas_n{n}_k{k}__p{p}.png"

plt.savefig(file_path)



plt.figure()

plt.plot(x, y_beta04, label='beta=0.4', color='blue')
plt.fill_between(x, y_beta04 - v_04, y_beta04 + v_04, color='blue', alpha=0.1)
plt.plot(x, y_beta06, label='beta=0.6', color='cyan')
plt.fill_between(x, y_beta06 - v_06, y_beta06 + v_06, color='cyan', alpha=0.1)
plt.plot(x, y_beta08, label='beta=0.8', color='red')
plt.fill_between(x, y_beta08 - v_08, y_beta08 + v_08, color='red', alpha=0.1)
plt.plot(x, y_beta10, label='beta=1', color='orange')
plt.fill_between(x, y_beta10 - v_10, y_beta10 + v_10, color='orange', alpha=0.1)
plt.plot(x, y_beta12, label='beta=1.2', color='green')
plt.fill_between(x, y_beta12 - v_12, y_beta12 + v_12, color='green', alpha=0.1)



plt.xlabel("number of samples")
plt.ylabel("distance of true center and learned center")
plt.legend()

file_path = f"/Users/sh1678/Dropbox/Research/Mallows/topkmallows-choices/Plots/findcenter_newformat_allbetas_n{n}_k{k}__p{p}.png"

plt.savefig(file_path)


plt.figure()

plt.errorbar(x, y_beta04, v_04, fmt='o-', capsize=1,color="red",label="beta=0.4")
plt.errorbar(x, y_beta06, v_06, fmt='o-', capsize=1,color="green",label="beta=0.6")
plt.errorbar(x, y_beta08, v_08, fmt='o-', capsize=1,color="blue",label="beta=0.8")
plt.errorbar(x, y_beta10, v_10, fmt='o-', capsize=1,color="orange",label="beta=1")
plt.errorbar(x, y_beta12, v_12, fmt='o-', capsize=1,color="cyan",label="beta=1.2")


plt.xlabel("number of samples")
plt.ylabel("distance of true center and learned center")
plt.legend()

file_path = f"/Users/sh1678/Dropbox/Research/Mallows/topkmallows-choices/Plots/findcenter_allbetas_n{n}_k{k}__p{p}.png"

plt.savefig(file_path)