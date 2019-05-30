import math
pi = math.pi
import pyautogui as aui

def main():
    #start at 800,800
    centrex = 1000
    centrey = 600
    #radius of 100
    radius = 350
    n = 5000
    points = PointsInCircum(radius,n,centrex,centrey)

    for i in range(n) :
        aui.click(points[i])


def PointsInCircum(r,n,cx,cy):
    return [(math.cos(2*pi/n*x)*r+cx,math.sin(2*pi/n*x)*r+cy) for x in range(0,n+1)]

