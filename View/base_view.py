class BaseView():

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_error(error):
        red = '\033[31m'
        white = '\033[0;0m'
        print(red + error + white)


