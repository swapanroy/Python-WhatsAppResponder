import pyautogui as pt 
from time import sleep
import pyperclip
import random
from re import search

sleep(7)

oldposition1 = pt.locateOnScreen("Smiley_paperclip.jpg", confidence = .6)
x = oldposition1[0]
y = oldposition1[1]

#Get message 

def get_message():
    global x,y
    position = pt.locateOnScreen("Smiley_paperclip.jpg", confidence = .6)
    x= position[0]
    y= position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x+40, y-70, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Recieved: " + whatsapp_message)
    return whatsapp_message



## Post response on Whatsapp

def post_message(message):
    global x, y 
    position = pt.locateOnScreen("Smiley_paperclip.jpg", confidence = .6)
    x= position[0]
    y= position[1]
    pt.moveTo(x+200, y+20, duration= 0.5)
    pt.click()
    pt.typewrite(message, interval=0.1)


    #pt.typewrite("\n", interval=0.01)



# Process messages LOGIC needs to be checked and worked upon.
def process_response(message):
    

      
    if search("Hi", str(message)):
        return "Thank you for your message ! \n . Press A for today's special, press B for location address, press C for hours of service."4
        
    elif search("GitHub", str(message)):
        return "Yes, share email ID."

    else:
        return "Apologies \n BOT testing in progress"

       
#Check for new messages continously 
def check_for_new_messages():
    pt.moveTo(x+40, y-70, duration= 0.5)

    while True:
        # Continously checks for green dot and new messages 
        try:
            position = pt.locateOnScreen("green_circle.jpg", confidence = 0.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new messages")

        if pt.pixelMatchesColor(int(x+40), int(y-70),(255,255,255), tolerance= 20):
            print("Color is while")
            processed_message = process_response(get_message()) 
            post_message(processed_message)
        else:
            print("No new messages yet....")
        sleep(5) 


#Calling functions 

check_for_new_messages()

# processed_message = process_response(get_message())
# post_message(processed_message)

# post_message(get_message())

