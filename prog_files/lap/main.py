# coding: utf-8
import my_gps
import my_route
import my_trigger

# インスタンス作成
position = my_gps.GPS()
trigger = my_trigger.Excited_trigger()

while True:

	# GPSデータを生成
	position.gps_data()

	# GPSデータを出力
	position.send_gps_data()

	# 興奮度を作成
	trigger.make_trigger()
	
	trigger.send_trigger()



	




