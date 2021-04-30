"""
 * Project: Real-estate-Picker.
 * Author: Levan Ostrowski
 * User: cod3venom
 * Date: 4/30/2021
 * Time: 8:09 PM
 * Github: https://github.com/cod3venom
"""

from colorama import Fore, Back, Style
from colorama import init
import random, colorama



class Logo:

    banner = '''
.______       _______     ___       __          _______     _______.___________.    ___   .___________. _______ 
|   _  \     |   ____|   /   \     |  |        |   ____|   /       |           |   /   \  |           ||   ____|
|  |_)  |    |  |__     /  ^  \    |  |        |  |__     |   (----`---|  |----`  /  ^  \ `---|  |----`|  |__   
|      /     |   __|   /  /_\  \   |  |        |   __|     \   \       |  |      /  /_\  \    |  |     |   __|  
|  |\  \----.|  |____ /  _____  \  |  `----.   |  |____.----)   |      |  |     /  _____  \   |  |     |  |____ 
| _| `._____||_______/__/     \__\ |_______|   |_______|_______/       |__|    /__/     \__\  |__|     |_______|
                                                                                                                                                                                                                    
    '''

    def __init__(self):
        colors = list(vars(colorama.Fore).values())
        colored_chars = [random.choice(colors) + char for char in self.banner]
        print(''.join(colored_chars))