import requests 

class_category = requests.post("http://192.168.50.247:8466/processing_part_match",json={"kornbot380@hotmail.com":{"command":'RMD-L9010 Servo Motor & Open protocol RS485 Driver 8A 14bit 0.02degree 1.07Nm 510g 61KV ; Nominal current, A, 3.30 ; Nominal torque, N.M, 0.61 ; Nominal Speed, rpm\xa0...',"ref_data":['Motion_system','Vision_system','Sensors','Navigation_system','Communication_system','Odometry_system','Materials','Battery','Microcontroller','Audio_system','Single_Board_Computer']}})

sub_categorydat = requests.post("http://192.168.50.247:8466/processing_part_match",json={"kornbot380@hotmail.com":{"command":'The L293D is designed to provide bidirectional drive currents of up to. 600-mA at voltages from 4.5 V to 36 V. Both devices are designed to drive inductive\xa0...',"ref_data":['dc-motor','servo-motor','bldc-motor','stepper-motor','acoustic-array','mechanical_force-array']}})

print(class_category)

print(sub_categorydat)
