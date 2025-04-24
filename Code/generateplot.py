import numpy as np 
import matplotlib.pyplot as plt

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