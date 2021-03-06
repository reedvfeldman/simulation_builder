import numpy as np

def filter_field(field,frac=0.5):
    field.require_coeff_space()
    dom = field.domain
    local_slice = dom.dist.coeff_layout.slices(scales=dom.dealias)

    coeff = []                                                            
    for i, n in enumerate(dom.global_coeff_shape):
        #if i == 1:
        #    coeff.append(np.linspace(-1,1,n,endpoint=False))
        #else:
        coeff.append(np.linspace(0,1,n,endpoint=False))

    cc = np.meshgrid(*coeff,indexing='ij')
    field_filter = np.zeros(dom.local_coeff_shape,dtype='bool')
    for i in range(dom.dim):                                                                                
        field_filter = field_filter | (np.abs(cc[i][local_slice]) > frac)
    field['c'][field_filter] = 0j
