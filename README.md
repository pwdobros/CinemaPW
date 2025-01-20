## Przegląd

System ten jest zaprojektowany do zarządzania czasami seansów filmowych, rezerwacjami klientów oraz specjalnymi funkcjami dla klientów VIP w kinie. Główne komponenty systemu to klasy `Movie`, `Customer`, `VIPCustomer` oraz `Cinema`. Poniżej znajduje się opis każdej z klas oraz ich funkcjonalności.

## Klasy

### `Movie`

Klasa `Movie` reprezentuje film w kinie.

#### Atrybuty:
- **title (str)**: Tytuł filmu.
- **duration (int)**: Czas trwania filmu w minutach.
- **showtimes (list)**: Lista dostępnych godzin seansów filmu w formacie `"HH:MM"`.

#### Metody:
- **`__init__(title, duration, showtimes)`**: Inicjalizuje film z tytułem, czasem trwania i godzinami seansów. Waliduje czas trwania i godziny seansów.
- **`validate_time(time)`**: Metoda statyczna, która sprawdza, czy podany czas jest w poprawnym formacie (`HH:MM`) oraz mieści się w przedziale między 08:00 a 20:00.
- **`validate_duration(duration)`**: Metoda statyczna, która sprawdza, czy czas trwania filmu jest liczbą całkowitą większą niż 0.
- **`add_showtime(time)`**: Dodaje nową godzinę seansu, jeśli jest poprawna i nie znajduje się już na liście.
- **`remove_showtime(time)`**: Usuwa godzinę seansu z listy.
- **`display_details()`**: Wyświetla szczegóły filmu, w tym tytuł, czas trwania i dostępne godziny seansów.

### `Customer`

Klasa `Customer` reprezentuje klienta kina.

#### Atrybuty:
- **first_name (str)**: Imię klienta.
- **last_name (str)**: Nazwisko klienta.
- **reservations (list)**: Lista rezerwacji dokonanych przez klienta, każda rezerwacja to krotka zawierająca tytuł filmu i godzinę seansu.

#### Metody:
- **`__init__(first_name, last_name)`**: Inicjalizuje klienta z imieniem, nazwiskiem oraz pustą listą rezerwacji.
- **`add_reservation(movie, time)`**: Dodaje rezerwację dla klienta, jeśli wybrany czas seansu jest dostępny dla filmu.
- **`display_reservations()`**: Wyświetla rezerwacje klienta, w tym tytuł filmu i godzinę seansu.

### `VIPCustomer` (Dziedziczy po `Customer`)

Klasa `VIPCustomer` reprezentuje specjalnego klienta z dodatkowymi przywilejami.

#### Metody:
- **`get_discounted_price(price)`**: Zwraca cenę po rabacie dla klientów VIP (20% zniżki).
- **`book_private_show(movie, time)`**: Pozwala klientowi VIP zarezerwować prywatny seans filmu o określonej godzinie.

### `Cinema`

Klasa `Cinema` reprezentuje kino, w którym znajdują się filmy i klienci.

#### Atrybuty:
- **movies (list)**: Lista filmów dostępnych w kinie.
- **customers (list)**: Lista klientów kina.

#### Metody:
- **`__init__()`**: Inicjalizuje kino z pustymi listami filmów i klientów.
- **`add_movie(movie)`**: Dodaje film do listy filmów w kinie.
- **`add_customer(customer)`**: Dodaje klienta do listy klientów kina.
- **`display_movies()`**: Wyświetla filmy dostępne w kinie, w tym szczegóły o filmach.

## Przykład użycia

```python
# Tworzenie filmów
movie1 = Movie("Inception", 148, ["14:00", "18:00", "21:00"])
movie2 = Movie("Interstellar", 169, ["12:00", "16:00", "20:00"])

# Tworzenie klientów
customer1 = Customer("John", "Doe")
vip_customer = VIPCustomer("Jane", "Smith")

# Tworzenie kina
cinema = Cinema()
cinema.add_movie(movie1)
cinema.add_movie(movie2)
cinema.add_customer(customer1)
cinema.add_customer(vip_customer)

# Wyświetlanie filmów
cinema.display_movies()

# Dodawanie rezerwacji
customer1.add_reservation(movie1, "14:00")
vip_customer.add_reservation(movie2, "20:00")

# Wyświetlanie rezerwacji
customer1.display_reservations()
vip_customer.display_reservations()

# Rezerwacja prywatnego seansu przez klienta VIP
vip_customer.book_private_show(movie1, "18:00")
