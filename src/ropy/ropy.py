import sys
import time
import warnings
import pyautogui

def init():
    with open("finished.lua", "a") as f:
        f.truncate(0)
def game():
    with open("finished.lua", "a") as f:
        return f.write('game.')
def workspace():
    with open("finished.lua", "a") as f:
        return f.write('Workspace')
def newline():
    with open("finished.lua", "a") as f:
        return f.write('\n')
def gameobject(object):
    with open("finished.lua", "a") as f:
        return f.write("." + str(object))
def dot():
    with open("finished.lua", "a") as f:
        return f.write(".")
def space():
    with open("finished.lua", "a") as f:
        return f.write(" ")
def NULL():
    with open("finished.lua", "a") as f:
        return f.write("nil")
def local():
    with open("finished.lua", "a") as f:
        return f.write("local")
def int(int):
    with open("finished.lua", "a") as f:
        if int.isalpha() == True:
            None
        else:
            return f.write(int)
def code(code):
    with open("finished.lua", "a") as f:
        return f.write(code)
def string(string):
    with open("finished.lua", "a") as f:
        if string.isalpha() == True:
            return f.write(string)
        else:
            None
def transparency(value):
    with open("finished.lua", "a") as f:
        if transparency.isalpha() == False:
            return f.write(".Transparency" + " = " + value)
        else:
            None
def equals():
    with open("finished.lua", "a") as f:
        return f.write(" = ")
def reflectance(value):
    with open("finished.lua", "a") as f:
        if reflectance.isalpha() == False:
            return f.write(".Reflectance" + " = " + value)
        else:
            None
def canCollide(value):
    with open("finished.lua", "a") as f:
        if canCollide.isalpha() == True:
            return f.write(".CanCollide" + " = " + value)
        else:
            None
def anchored(Anchored):
    with open("finished.lua", "a") as f:
        if Anchored.isalpha() == True:
            return f.write(".Anchored" + Anchored)
        else:
            None
def then():
    with open("finished.lua", "a") as f:
        return f.write(" then")
def customsetting(customsetting):
    with open("finished.lua", "a") as f:
        if customsetting.isalpha() == True:
            return f.write("." + customsetting)
        else:
            None
def isequalto():
    with open("finished.lua", "a") as f:
        return f.write("==")
def playing():
    with open("finished.lua", "a") as f:
        return f.write(".Playing")
def comment(comment):
    with open("finished.lua", "a") as f:
        return f.write("--" + comment)
def delay(wait):
    with open("finished.lua", "a") as f:
        return f.write("wait(" + wait + ")")
def starterplayer():
    with open("finished.lua", "a") as f:
        return f.write(".StarterPlayer")
def teams():
    with open("finished.lua", "a") as f:
        return f.write(".Teams")
def starterpack():
    with open("finished.lua", "a") as f:
        return f.write(".StarterPack")
def startergui():
    with open("finished.lua", "a") as f:
        return f.write(".StarterGui")
def players():
    with open("finished.lua", "a") as f:
        return f.write(".Players")
def lighting():
    with open("finished.lua", "a") as f:
        return f.write(".Lighting")
def chat():
    with open("finished.lua", "a") as f:
        return f.write(".Chat")
def TextChatService():
    with open("finished.lua", "a") as f:
        return f.write(".TextChatService")
def print(value):
    with open("finished.lua", "a") as f:
        return f.write("print(" + "'" + value + "'" + ")")
def settingbool(setting, value):
    with open("finished.lua", "a") as f:
        if customsetting.isalpha() == True:
            return f.write("." + setting + " = " + value)
        else:
            None
def settingint(setting, value):
    with open("finished.lua", "a") as f:
        if customsetting.isalpha() == False:
            return f.write("." + setting + " = " + value)
        else:
            None
