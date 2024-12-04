import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lizhen/works/code/OpenRobot/urdf_mjcf_autogenerator/install/model_generator'
