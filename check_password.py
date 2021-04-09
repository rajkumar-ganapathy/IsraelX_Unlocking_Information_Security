import time
import sys # ignore
import math

def check_password(password): # Don't change it
    real_password = "3948394839489384"
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

def crack_password() :
    print("in crack_password")
    pass1 = "0000000000000000"
    current_digit = 0
    current_index = 0
    time_taken = time.time()
    check_password("0000")
    time_taken = time.time() - time_taken
    print("initial time taken is " + str(time_taken))

    password_cracked = False
    
    while password_cracked == False :
        print("current_index is " + str(current_index))
        pass1 = pass1[:current_index] + str(current_digit) + pass1[current_index+1:]
        print("pass1 value is " + str(pass1))
        start = time.time()
        password_cracked = check_password(pass1)
        current_time_taken = (time.time() - start)
        print("current time taken is " + str(current_time_taken))
        print("previous time taken is " + str(time_taken))
        if  password_cracked == False :
            if current_time_taken >= time_taken + 0.1 :
                time_taken = current_time_taken
                current_time_taken = 0
                current_index = math.floor(time_taken/0.1) - 1
                current_digit = 0
            else :
                current_digit = current_digit + 1
                if current_digit > 9 :
                    current_digit = 0
                    current_index = current_index + 1

    pass1

crack_password()