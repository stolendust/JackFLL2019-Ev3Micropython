# JackFLL2019

Jack's EV3 Micropython Project for FLL 2019, jack@abow.my   
Created on 11/10/2019 by Terry, tao@abow.my, JackRobot Studio   


# Tips of EV3 Micropython 1.0.0

I has encountered some problems in working with EV3 Micropython. List some useful lessons or tips here.

- don't expect to use the data type enum.Enum, you will fail to import Enum from enum
- no chance to format an class or object to string, always get '' with str() 
- unittest does work, remember to run 'pybricks-micropython YOUR_TEST_MODULE.py' instead of 'pybricks-micropython -m unittest YOUR_TEST_MODULE'
- be careful to make sure no syntax in your unittest code because syntax error can not be shown 
