# -------------------- MOVIE TICKET BOOKING SYSTEM --------------------

movies = {
    1: {"name": "Avengers: Endgame", "price": 250, "seats": 50},
    2: {"name": "KGF Chapter 2", "price": 200, "seats": 60},
    3: {"name": "Leo", "price": 180, "seats": 40},
    4: {"name": "Dunki", "price": 220, "seats": 30},
}

def show_movies():
    print("\n--------- Available Movies ---------")
    for mid, info in movies.items():
        print(f"{mid}. {info['name']}  | Price: ₹{info['price']}  | Seats Left: {info['seats']}")
    print("-----------------------------------")

def book_ticket():
    show_movies()
    movie_id = int(input("Select movie ID: "))

    if movie_id not in movies:
        print(" Invalid Movie ID")
        return

    seats_needed = int(input("How many seats do you want? "))

    if seats_needed <= 0:
        print(" Invalid number of seats.")
        return

    if seats_needed > movies[movie_id]["seats"]:
        print(" Not enough seats available!")
        return

    # Update seat count
    movies[movie_id]["seats"] -= seats_needed

    total = movies[movie_id]["price"] * seats_needed
    print("\n Booking Successful!")
    print(f"Movie: {movies[movie_id]['name']}")
    print(f"Seats Booked: {seats_needed}")
    print(f"Total Amount: ₹{total}")
    print("-----------------------------------")

def cancel_ticket():
    show_movies()
    movie_id = int(input("Enter movie ID to cancel ticket: "))

    if movie_id not in movies:
        print(" Invalid Movie ID")
        return

    cancel_seats = int(input("How many seats you want to cancel? "))

    if cancel_seats <= 0:
        print(" Invalid seat number.")
        return

    movies[movie_id]["seats"] += cancel_seats
    print("\n Your ticket has been cancelled.")
    print("-----------------------------------")

def main():
    while True:
        print("\n========== MOVIE TICKET BOOKING ==========")
        print("1. Show Movies")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            show_movies()
        elif choice == 2:
            book_ticket()
        elif choice == 3:
            cancel_ticket()
        elif choice == 4:
            print("Thank you for using Movie Ticket Booking System! ")
            break
        else:
            print(" Invalid Choice. Try again.")

main()
