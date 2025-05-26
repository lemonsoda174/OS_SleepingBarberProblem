import threading
import time
import random

total_customers = 10
customers = list(range(1, total_customers+1))

#number of seats in waiting room
available_seats = 3

# 1 mutex and 2 semaphores
accessWRSeats = threading.Semaphore(1) # 1 means number of seats in waiting room can be changed
barberReady = threading.Semaphore(0) # binary semaphore
custReady = threading.Semaphore(0)

def barber():
    global available_seats
    while True:
        # Try to acquire a customer - if none is available, go to sleep.
        custReady.acquire()            

        # Awake - try to get access to modify number of available seats, otherwise sleep.
        accessWRSeats.acquire()           

        available_seats += 1             # One waiting room chair becomes free.
        # barber is ready to cut
        barberReady.release()        

        # Release access to seat count
        accessWRSeats.release()           

        # Cut hair (simulate with sleep)
        print("Barber is cutting hair...")
        time.sleep(random.uniform(1, 2))
        print("Barber finished cutting hair.\n")

def customer(customer_id):
    global available_seats
    time.sleep(random.uniform(0.5, 3))  # Customer arrives at random intervals

    # Try to get access to the waiting room chairs.
    accessWRSeats.acquire()
    if available_seats > 0:
        available_seats -= 1
        print(f"Customer {customer_id} sits in the waiting room. Free seats left: {available_seats}")
        custReady.release()      # Notify the barber a customer is waiting
        accessWRSeats.release()
        barberReady.acquire()       # Wait for the barber to be ready

        print(f"Customer {customer_id} is getting a haircut.")
    else:
        print(f"Customer {customer_id} leaves without a haircut (no free seats).")
        accessWRSeats.release()

def main():
    threading.Thread(target=barber, daemon=True).start()

    for customer_id in customers:
        threading.Thread(target=customer, args=(customer_id,), daemon=True).start()

    while True:
        time.sleep(1)
        

if __name__ == "__main__":
    main()
