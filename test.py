from python_imagesearch.imagesearch import imagesearch
import pyautogui

posX = 0
posY = 0

def quickImageSearch():
    pos = imagesearch("./imagesamples/button.png")
    if pos[0] != -1:
        # prints out the x,y coordinate positions of the image
        posX = pos[0]
        posY = pos[1]
        print("position : ", pos[0], pos[1])
    else:
        print("image not found")


def clickPoint():
    # try:
    quickImageSearch()
    print(type(posX))
    # pyautogui.FAILSAFE = False
    # pyautogui.click(x=posX, y=posY)
    # except:
    #     print("err")
    

if __name__ == "__main__":
    clickPoint()
    pass