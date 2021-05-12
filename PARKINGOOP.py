# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:33:10 2021

@author: parin
"""

#vehicle class to account for vehicle type
class Vehicle :
    def __init__(self) :
        self.vehType = ' '
  
    def setVehicleType(self) :
        while True :
            veh = input("Enter Vehicle Type(Car, Bus, Truck): ").lower()
            if veh not in ("car", "bus", "truck") :
                print("Enter Valid Vehicle Type")
            else :
                self.vehType = veh
            break
    def getVehType(self) :
        return self.vehType

#ParkingLot class having 'HAS-A' realtionship with class Vehicle
class ParkingLot :
    def __init__(self) : # defining variables here
        self.hourIn = 0
        self.minuteIN = 0
        self.hourOut = 0
        self.minuteOut = 0
  
        self.parkingTime = 0
        self.parkingHour = 0
        self.parkingTime = 0
  
        self.parkingCharge = 0
  
        self.vehicle = Vehicle() # Vehicle class object
  
    def setVehicleType(self) : # sets the vehicle type
        self.vehicle.setVehicleType()
    def setInTime(self) : # takes user input of ENTERING HOUR AND MINUTE
        while True :
            hour = int(input("Hour Of Vehicle Entering(0-24): "))
            if hour < 0 or hour >= 24 : # if entered hour is invalid
                print("Enter Valid Hour") # then shows error
            else :
                self.hourIn = hour
            break
  
        while True :
            minute = int(input("Minute Of Vehicle Entering(0-60): "))
            if minute < 0 or minute >= 60 : # if entered minute is invalid
                print("!!Enter Valid Minute!!") # then show error
            else :
                self.minuteIn = hour
            break
    def setOutTime(self) : # takes user input of LEVING HOUR AND MINUTE
        while True :
            hour = int(input("Hour Of Vehicle Leaving(0-24)"))
            if hour < 0 or hour < self.hourIn or hour >= 24 : # LEAVING HOUR must be greater than or equal to Entering HOUR
                print("!!Enter Valid Hour!!")
            else :
                self.hourOut = hour
            break
  
        while True :
            minute = int(input("Minute Of Vehicle Leaving(0-60)"))
        if minute < 0 or minute >= 60 :
            print("!!Enter Valid Minute!!")
        else :
            self.minuteOut = hour
        break
  
    def calc_parkingTime(self) : # calculates the time of parking
        t1 = self.hourIn*60 + self.minuteIn
        t2 = self.hourOut*60 + self.minuteOut
        time = t2 - t1
        self.parkingHour = int(time/60)
        self.parkingMinute = time%60
# rounding-off the time
        self.parkingTime = self.parkingHour
        if self.parkingMinute > 0 :
            self.parkingTime = self.parkingHour+1
  
    def calc_parkingCharges(self) : # calculates the parking charge as per vehicle type
        self.calc_parkingTime()
        veh = self.vehicle.getVehType()
        if veh == "car" : #for "car"-type
            if self.parkingTime > 3 :
                self.parkingCharge = self.parkingTime * 1.50
        elif veh == "bus" : #for "bus"-type
            if self.parkingHour == 1 :
                self.parkingCharge = self.parkingHour * 2
        else :
            self.parkingCharge = self.parkingHour * 3.70
        elif veh == "truck" : #for "truck"-type
            if self.parkingHour <= 2 :
                self.parkingCharge = self.parkingHour * 1
                else :
                    self.parkingCharge = self.parkingHour * 2.3
  
    def display(self) : #shows the detail on the console
    print("\nPARKING LOT CHARGES")
    print("Type Of Vehicle: ", self.vehicle.getVehType())
    print("TIME-IN", self.hourIn, ":", self.minuteIn)
    print("TIME-OUT", self.hourOut, ":", self.minuteOut)
    print("PARKING-TIME", self.parkingHour, ":", self.parkingMinute)
    print("ROUNDED TOTAL", self.parkingTime)
    print("TOTAL CHARGES: $", self.parkingCharge)
    print("----------------------------------------------------\n")
  

    def main() : #user defined main function
    park = ParkingLot()
  
    while True :
    park.setVehicleType()
    park.setInTime()
    park.setOutTime()
    park.calc_parkingCharges()
    park.display()
  
flag = input("Want To Continue?(y/n): ").lower()
if flag == 'n' :
break
  
# calling of main() function
if __name__ == "__main__" :
main()