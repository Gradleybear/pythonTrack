#!/bin/python3

import math
import os
import random
import re
import sys




n = 18
if n%2==1:
  print("Weird")
elif n%2==0 and n<=5 and n>=2:
 print("Not Weird")  #If n is even and in the inclusive range of 2  to 5, print Not
elif n%2==0 and n>=6 and n<=20:
 print("Weird")
else:
 print("Not Weird")
