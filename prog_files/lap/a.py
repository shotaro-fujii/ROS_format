#!/usr/bin/env python
# coding: utf-8


import my_route
import datetime
from time import sleep

class GPS:

    def __init__(self):
        self.lat = 51.358 
        self.lon = -19.694 
        self.__gps_data = []

    def gps_data(self):
        self.lat += 0.18
        self.lon -= 0.05	
        time = str(datetime.datetime.now())
        self.__gps_data.extend([self.lat, self.lon, time])
        
			
    def send_gps_data(self):

        route = my_route.Excited_route(3)
        route.set_route(self.__gps_data)
        
if __name__ == "__main__":

    # インスタンス作成
    position = GPS()

    while True:
        # GPSデータを生成
        position.gps_data()

        # GPSデータを出力
        position.send_gps_data()






