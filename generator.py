

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

def volPlot(sub_list, signal_type ):
    if signal_type == "Raw":
        signal="raw"
    else:
        signal="wav"
    
    sub=sub_list
     
        
    #file='py/' + tis + 'VBM' + st + '-' + th + '.nii.gz'

    file_right='coefficients/sub-cb' + sub + '_eyes_' + signal  + '_sm_left_bucket_coef.nii.gz'
    file_left='coefficients/sub-cb' + sub + '_eyes_' + signal  + '_sm_right_bucket_coef.nii.gz'
    #sub-cb01_eyes_raw_sm_left_bucket_coef


    a=plotting.view_img(file_right, draw_cross=False, cmap='seismic', dim=0, threshold=1);
    #b=plotting.view_img(file_left, draw_cross=False, cmap='seismic', dim=0, threshold=0.1);
    return a


