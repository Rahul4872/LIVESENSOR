from sensor.exception import  SensorException
import os
import sys
import traceback

def test_excpetion():
    try:
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)



if __name__ == "__main__":
    try:
        test_excpetion()
    except Exception as e:
        print(e)