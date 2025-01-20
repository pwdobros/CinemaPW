from datetime import datetime

class Movie:
    def __init__(self, title, duration, showtimes):
        self.title = title
        if not self.validate_duration(duration):
            raise ValueError("Duration must be a positive integer.")
        self.duration = duration
        for time in showtimes:
            if not self.validate_time(time):
                raise ValueError("Showtimes must be in the format HH:MM and between 08:00 and 20:00.")
        self.showtimes = showtimes

    @staticmethod
    def validate_time(time):
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            return False
        hours, minutes = map(int, time.split(":"))
        total_minutes = hours * 60 + minutes
        return 480 <= total_minutes <= 1200  # Between 08:00 and 20:00

    @staticmethod
    def validate_duration(duration):
        return isinstance(duration, int) and duration > 0

    def add_showtime(self, time):
        if not self.validate_time(time):
            raise ValueError("Showtime must be in the format HH:MM and between 08:00 and 20:00.")
        if time not in self.showtimes:
            self.showtimes.append(time)
        else:
            print("Showtime already exists.")

    def remove_showtime(self, time):
        if time in self.showtimes:
            self.showtimes.remove(time)
        else:
            print("Showtime not found.")

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Duration: {self.duration} minutes")
        print(f"Showtimes: {', '.join(self.showtimes)}")


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reservations = []

    def add_reservation(self, movie, time):
        if time in movie.showtimes:
            self.reservations.append((movie.title, time))
        else:
            print(f"Showtime {time} is not available for movie {movie.title}.")

    def display_reservations(self):
        print(f"Reservations for {self.first_name} {self.last_name}:")
        for movie, time in self.reservations:
            print(f"Movie: {movie}, Showtime: {time}")


class VIPCustomer(Customer):
    def get_discounted_price(self, price):
        discounted_price = price * 0.8
        print(f"Discounted price: {discounted_price}")
        return discounted_price

    def book_private_show(self, movie, time):
        if time in movie.showtimes:
            print(f"Private show booked for {self.first_name} {self.last_name} for movie {movie.title} at {time}.")
            self.reservations.append((movie.title, time, "Private"))
        else:
            print(f"Showtime {time} is not available for movie {movie.title}.")


class Cinema:
    def __init__(self):
        self.movies = []
        self.customers = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_customer(self, customer):
        self.customers.append(customer)

    def display_movies(self):
        print("Movies in Cinema:")
        for movie in self.movies:
            movie.display_details()


# Main program
def main():
    # Create movies
    movie1 = Movie("Inception", 148, ["14:00", "18:00", "21:00"])
    movie2 = Movie("Interstellar", 169, ["12:00", "16:00", "20:00"])

    # Create customers
    customer1 = Customer("John", "Doe")
    vip_customer = VIPCustomer("Jane", "Smith")

    # Create cinema
    cinema = Cinema()
    cinema.add_movie(movie1)
    cinema.add_movie(movie2)
    cinema.add_customer(customer1)
    cinema.add_customer(vip_customer)

    # Display movies
    cinema.display_movies()

    # Add reservations
    customer1.add_reservation(movie1, "14:00")
    vip_customer.add_reservation(movie2, "20:00")

    # Display reservations
    customer1.display_reservations()
    vip_customer.display_reservations()

    # VIP private show booking
    vip_customer.book_private_show(movie1, "18:00")

if __name__ == "__main__":
    main()
