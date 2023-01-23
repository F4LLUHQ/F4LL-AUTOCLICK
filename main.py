from pystyle import *
import keyboard
import threading
import pyautogui

System.Title("⚡  F4LL CLICKER  ⚡")

heart = """


        @@@@@@           @@@@@@
      @@@@@@@@@@       @@@@@@@@@@
    @@@@@@@@@@@@@@   @@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@
              @@@@@@@@@@@
                @@@@@@@
                  @@@
                   @



"""

Darling = """

███████╗██╗  ██╗██╗     ██╗          ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║  ██║██║     ██║         ██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
█████╗  ███████║██║     ██║         ██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝
██╔══╝  ╚════██║██║     ██║         ██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║          ██║███████╗███████╗    ╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝          ╚═╝╚══════╝╚══════╝     ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

[⚡] - @f4ll_1337 | t.me/chez_f4ll                                                                                      
                                                                                                             
"""

def Main(keybind_left , keybind_right):

    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(Darling)))

    print('\n')
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(f"[!] Press {keybind_left} To Start and Stop the Left Autoclicker")))
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(f"[!] Press {keybind_right} To Start and Stop the Right Autoclicker")))
    while True : 
        try :
            if keyboard.is_pressed(keybind_left) :

                    while True :
                        left = True
                        pyautogui.click()

                        if keyboard.is_pressed(keybind_left):
                            if left == True :
                                System.Clear()
                                Main(keybind_left=keybind_left , keybind_right=keybind_right)

            if keyboard.is_pressed(keybind_right):
                
                while True :
                    right = True
                    pyautogui.rightClick()

                    if keyboard.is_pressed(keybind_right):
                        if right == True :
                                System.Clear()
                                Main(keybind_left=keybind_left , keybind_right=keybind_right)

        except :
            pass

def Setup():
    System.Clear()
    Anime.Fade(Center.Center(heart) , Colors.purple_to_blue , Colorate.Vertical , enter=True)
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(Darling)))
    print('\n')

    Key_left = Write.Input("[!] Type The Keybind you want to set for the Left Autoclicker -> " , Colors.purple_to_blue , interval=0.0025)
    Key_right = Write.Input("[!] Type The Keybind you want to set for the Right Autoclicker -> " , Colors.purple_to_blue , interval=0.0025)
    
    System.Clear()
    Main(keybind_left=Key_left , keybind_right=Key_right)


Setup()