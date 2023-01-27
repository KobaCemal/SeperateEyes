

from nilearn import plotting

from IPython.display import clear_output
import ipywidgets
from IPython.display import HTML
from IPython.display import display
import warnings
warnings.filterwarnings("ignore")


# Prepare the figure
signal_type = ipywidgets.widgets.Dropdown(
    options=['Raw', 'Convolved'],
    value='Raw',
    description='Signal Type:',
    disabled=False,
)

sub_list = ipywidgets.widgets.Dropdown(
    options=['01', '02','03','04','05','06','07','08','09','10','11','12','13','14'],
    value='01',
    description='Subject ID:',
    disabled=False,
)

def volPlotRight(sub_list, signal_type,threshold):
    if signal_type == "Raw":
        signal="raw"
    else:
        signal="wav"
    
    sub=sub_list
     
        
    file_right='sub-cb' + sub + '_eyes_' + signal  + '_sm_right_bucket_coef.nii.gz'

    a=plotting.view_img(file_right, draw_cross=False, cmap='seismic', dim=0, threshold=threshold)
    return a


def volPlotLeft(sub_list, signal_type,threshold):
    if signal_type == "Raw":
        signal="raw"
    else:
        signal="wav"
    
    sub=sub_list
     
        
    file_left='sub-cb' + sub + '_eyes_' + signal  + '_sm_left_bucket_coef.nii.gz'

    b=plotting.view_img(file_left, draw_cross=False, cmap='seismic', dim=0, threshold=threshold)
    return b
