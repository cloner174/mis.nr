import bokeh
from bokeh.plotting import show
import matplotlib.pyplot as plt
import flowkit as fk

from main import nr


infolder1 = 'data/input/hum'
infolder2 = 'data/input/normal'

outfolder = 'data/output'

test = nr(infolder1, outfolder)

A, B, C, D = test.main()

print( len(A), len(B) )

a = A[0]
aa = A[1]
aaa = A[7]

b = B[0]
bb = B[1]
bbb = B[7]

test1_1 = fk.Sample(a)
test1_2 = fk.Sample(b)
test2_1 = fk.Sample(aa)
test2_2 = fk.Sample(bb)
test3_1 = fk.Sample(aaa)
test3_2 = fk.Sample(bbb)

p1_1 = test1_1.plot_scatter('FS Lin', 'SS Lin', source='raw')
p1_2 = test1_2.plot_scatter('FS', 'SS', source='raw')
show(p1_1)
show(p1_2)

p2_1 = test2_1.plot_scatter('FS Lin', 'SS Lin', source='raw')
p2_2 = test2_2.plot_scatter('FS', 'SS', source='raw')
show(p2_1)
show(p2_2)

p3_1 = test3_1.plot_scatter('FS Lin', 'SS Lin', source='raw')
p3_2 = test3_2.plot_scatter('FS', 'SS', source='raw')
show(p3_1)
show(p3_2)

for any_ in A:
    
    tempCreateFK = fk.Sample(any_)
    for i in range(0, (len(tempCreateFK.pnn_labels)-1), 2) :
        temp = (tempCreateFK.pnn_labels)[i]
        tempp = (tempCreateFK.pnn_labels)[i+1]
        p = tempCreateFK.plot_scatter(temp, tempp, source='raw')
        show(p)

for any_ in B:
    
    tempCreateFK = fk.Sample(any_)
    for i in range(0, (len(tempCreateFK.pnn_labels)-1), 2) :
        temp = (tempCreateFK.pnn_labels)[i]
        tempp = (tempCreateFK.pnn_labels)[i+1]
        p = tempCreateFK.plot_scatter(temp, tempp, source='raw')
        show(p)