def red_data_name(Method,params):
    fname = 'red_data/reduced_data_' +Method+ '.dat'
    return fname
def clust_name(Method,params):
    fname = 'cl_data/clustering_' + Method + '.dat'
    return fname
def plot_name(Method_red,Method_cl,params_red,params_cl,ext='.png'):
    fname = 'plots/plot_' + Method_red + '_' + Method_cl +ext
    return fname
