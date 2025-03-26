# NTU-EE3021-lab2 (Wifi and Sensor data)

## Members
- R12922A01 王廷郡
- R11944078 林資融


## Lab Requirements (From NTU Cool)
```
====basic problem====

Start/Modify a project in STM32 IoT node to read the sensor value,
such as 3D Accelerator or 3D gyro, and send the data (using wifi
with http or a tcp protocol) to a Linux(RPi)/Windows/Mac host and 
Visualize with some kind of GUI tools (such as using Python)

http sender example: https://github.com/iot2tangle/STM32_B-L475E-IOT01A/tree/main/http-sender

=================

 

====option problem_A====

Based on the basic problem, initialize and use the "significant
motion detection" features provided in the LSM6DSL BSP library (
LSM6DSL will send a signal to the STM32 IoT node via GPIO EXTI 
interrupt when a significant motion detected). 

If such event triggers, show on your Linux(RPi)/Windows/Mac host.
please refer these documents:

https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.st.com/resource/en/datasheet/lsm6dsl.pdf&ved=2ahUKEwj4p6aBrMqIAxVSa_UHHYpxE7AQFnoECBwQAQ&usg=AOvVaw2r_2ybK2prF7He1HXx3VHU
https://www.st.com/resource/en/application_note/an5040-lsm6dsl-alwayson-3d-accelerometer-and-3d-gyroscope-stmicroelectronics.pdf

===================

 

 

====option problem_B==== (optional personal report)

Students can choose content that is relevant to the class of this week, less repetitive with the assignment, and meaningful to conduct experiments on their own, and write a report on the experimental content and results.

```

## Run

My GUI code is unser GUI/ directory.
```
pip install matplotlib

export STM32_SERVER_HOST=[YOUR_PRIVATE_IPV4_IP] && export STM32_SERVER_PORT=[YOUR_SERVICE_PORT] && python3 server.py
```
