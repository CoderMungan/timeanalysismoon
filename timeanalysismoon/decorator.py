"""

                                                                                                                                
                                                            ____                                                                
  ,----..                                                 ,'  , `.                                                              
 /   /   \                ,---,                        ,-+-,.' _ |                                                              
|   :     :  ,---.      ,---.'|            __  ,-.  ,-+-. ;   , ||         ,--,      ,---,                               ,---,  
.   |  ;. / '   ,'\     |   | :          ,' ,'/ /| ,--.'|'   |  ;|       ,'_ /|  ,-+-. /  |  ,----._,.               ,-+-. /  | 
.   ; /--` /   /   |    |   | |   ,---.  '  | |' ||   |  ,', |  ':  .--. |  | : ,--.'|'   | /   /  ' /   ,--.--.    ,--.'|'   | 
;   | ;   .   ; ,. :  ,--.__| |  /     \ |  |   ,'|   | /  | |  ||,'_ /| :  . ||   |  ,"' ||   :     |  /       \  |   |  ,"' | 
|   : |   '   | |: : /   ,'   | /    /  |'  :  /  '   | :  | :  |,|  ' | |  . .|   | /  | ||   | .\  . .--.  .-. | |   | /  | | 
.   | '___'   | .; :.   '  /  |.    ' / ||  | '   ;   . |  ; |--' |  | ' |  | ||   | |  | |.   ; ';  |  \__\/: . . |   | |  | | 
'   ; : .'|   :    |'   ; |:  |'   ;   /|;  : |   |   : |  | ,    :  | : ;  ; ||   | |  |/ '   .   . |  ," .--.; | |   | |  |/  
'   | '/  :\   \  / |   | '/  ''   |  / ||  , ;   |   : '  |/     '  :  `--'   \   | |--'   `---`-'| | /  /  ,.  | |   | |--'   
|   :    /  `----'  |   :    :||   :    | ---'    ;   | |`-'      :  ,      .-./   |/       .'__/\_: |;  :   .'   \|   |/       
 \   \ .'            \   \  /   \   \  /          |   ;/           `--`----'   '---'        |   :    :|  ,     .-./'---'        
  `---`               `----'     `----'           '---'                                      \   \  /  `--`---'                 
                                                                                              `--`-'                            


Function running time analysis - dev CoderMungan
https://github.com/CoderMungan
"""


import time
from functools import wraps


def timeanalysismoon(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} working time: {end_time - start_time} second")
        return result

    return wrapper

"""
Example Func

@timeanalysismoon
def example():
    pass
    
example()

"""
