import flowio
import numpy

fcs_data = flowio.FlowData('example.fcs')
npy_data = numpy.reshape(fcs_data.events, (-1, fcs_data.channel_count))
