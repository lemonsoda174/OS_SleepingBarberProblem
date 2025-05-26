import threading
import time
import random

total_customers = 10
customers = list(range(1, total_customers + 1))

# Number of seats in waiting room
available_seats = 3


class BarberShop:
    def __init__(self, num_chairs):
        self.available_seats = num_chairs
        self.accessWRSeats = threading.Lock()
        self.custReady = threading.Condition(self.accessWRSeats)
        self.barberReady = threading.Condition(self.accessWRSeats)

    def customer_enters(self, customer_id):
        with self.accessWRSeats:
            if self.available_seats > 0:
                self.available_seats -= 1
                print(f"Customer {customer_id} sits in the waiting room. Free seats left: {self.available_seats}")
                self.custReady.notify()  # Notify the barber that a customer is ready
                self.barberReady.wait()  # Wait for the barber to be ready
                print(f"Customer {customer_id} is getting a haircut.")
            else:
                print(f"Customer {customer_id} leaves without a haircut (no free seats).")

    def barber_cuts(self):
        with self.accessWRSeats:
            while self.available_seats == 3:
                print("Barber is sleeping...")
                self.custReady.wait()  # Wait for a customer to arrive
            self.available_seats += 1
            self.barberReady.notify()  # Notify the customer that barber is ready
            print(f"Barber is cutting hair... (Free seats: {self.available_seats})")


def barber(barber_shop, run_flag):
    while run_flag.is_set():
        barber_shop.barber_cuts()
        time.sleep(random.uniform(1, 2))  # Simulate haircut time
        print("Barber finished cutting hair.\n")


def customer(barber_shop, customer_id):
    time.sleep(random.uniform(0.5, 3))  # Simulate customer arrival time
    barber_shop.customer_enters(customer_id)


def main():
    barber_shop = BarberShop(available_seats)

    run_flag = threading.Event()
    run_flag.set()

    # Start barber thread
    threading.Thread(target=barber, args=(barber_shop, run_flag), daemon=True).start()

    # Start customer threads
    for customer_id in customers:
        threading.Thread(target=customer, args=(barber_shop, customer_id), daemon=True).start()

    # Let simulation run for a while
    time.sleep(10)
    run_flag.clear()
    print("Simulation has ended.")


if __name__ == "__main__":
    main()
