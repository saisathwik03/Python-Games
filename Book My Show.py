def moviesList():
    movies = {
        "1": {
            "title": "Avengers: Endgame",
            "seats": [["X" for _ in range(10)] for _ in range(10)],
            "price": 10.0
        },
        "2": {
            "title": "The Lion King",
            "seats": [["X" for _ in range(8)] for _ in range(8)],
            "price": 8.0
        },
        "3": {
            "title": "Joker",
            "seats": [["X" for _ in range(6)] for _ in range(6)],
            "price": 9.0
        }
    }
    return movies

# User's booking cart stored as a list of dictionaries
cart = []

# Function to display available movies
def display_movies(movies):
    print("Available Movies:")
    for key, movie in movies.items():
        print(f"{key}: {movie['title']} - Seats: {sum(row.count('x') for row in movie['seats'])} - Price: ${movie['price']}")

# Function to book tickets
def book_ticket(movies, cart):
    display_movies(movies)
    movie_id = input("Enter the movie ID to book: ")
    if movie_id in movies:
        movie = movies[movie_id]
        print(f"Selected movie: {movie['title']}")
        print("Available Seats (numbers represents available seats):")
        for i, row in enumerate(movie['seats']):
            seat_numbers = [str(j + 1) if seat == 'X' else 'X' for j, seat in enumerate(row)]
            print(f"Row {i + 1}: {' '.join(seat_numbers)}")
        num_tickets = int(input("Enter the number of tickets to book: "))
        if num_tickets <= sum(row.count('X') for row in movie['seats']):
            selected_seats = []
            for _ in range(num_tickets):
                while True:
                    try:
                        row = int(input("Enter the row for your seat: ")) - 1
                        col = int(input("Enter the column for your seat: ")) - 1
                        if 0 <= row < len(movie['seats']) and 0 <= col < len(movie['seats'][row]) and movie['seats'][row][col] == 'X':
                            movie['seats'][row][col] = 'O'
                            selected_seats.append((row + 1, col + 1))
                            break
                        else:
                            print("Invalid seat selection. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid row and column.")
            total_price = num_tickets * movie['price']
            print(f"Total Price: ${total_price}")
            confirm = input("Confirm booking (yes/no): ").lower()
            if confirm == "yes":
                cart.append({"movie": movie['title'], "tickets": num_tickets, "price": total_price, "seats": selected_seats})
                print("Booking confirmed!")
            else:
                print("Booking canceled.")
        else:
            print("Insufficient seats available.")
    else:
        print("Invalid movie ID.")

# Function to view and checkout the cart
def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        total_cart_price = 0
        for item in cart:
            print(f"Movie: {item['movie']} - Tickets: {item['tickets']} - Price: ${item['price']}")
            print(f"Seats: {', '.join([f'Row {row}, Seat {col}' for row, col in item['seats']])}")
            total_cart_price += item['price']
        print(f"Total Cart Price: ${total_cart_price}")
        checkout = input("Proceed to checkout (yes/no): ").lower()
        if checkout == "yes":
            # You can implement a payment gateway here
            print("Payment successful! Tickets booked.")
            cart.clear()
        else:
            print("Checkout canceled.")

def bookmyShow():
    while True:
        movies = moviesList()  # Retrieve the movies dictionary
        print("\nWelcome to BookMyShow!")
        print("1. Book Ticket")
        print("2. View Cart")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_ticket(movies, cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            print("Thank you for using BookMyShow!")
            break
        else:
            print("Invalid choice. Please try again.")
bookmyShow()
