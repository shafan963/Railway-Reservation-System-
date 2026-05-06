seats = 10
bookings = {}

def check_availability():
    print("Available seats:", seats)

def book_ticket():
    global seats
    if seats <= 0:
        print("No seats available")
        return
    
    name = input("Enter name: ")
    age = input("Enter age: ")
    booking_id = len(bookings) + 1
    
    bookings[booking_id] = {"name": name, "age": age}
    seats -= 1
    
    print("Ticket booked. ID:", booking_id)

def view_ticket():
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        print(bookings[bid])
    else:
        print("Not found")

def cancel_ticket():
    global seats
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        del bookings[bid]
        seats += 1
        print("Cancelled")
    else:
        print("Not found")

while True:
    print("\n1.Check 2.Book 3.View 4.Cancel 5.Exit")
    ch = input("Enter choice: ")
    
    if ch == "1":
        check_availability()
    elif ch == "2":
        book_ticket()
    elif ch == "3":
        view_ticket()
    elif ch == "4":
        cancel_ticket()
    elif ch == "5":
        break