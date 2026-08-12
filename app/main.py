from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    my_list = []
    for key in customers:
        cus1 = Customer(key["name"], key["food"])
        CinemaBar.sell_product(cus1.food, cus1)
        my_list.append(cus1)

    hall_c = CinemaHall(hall_number)

    name_cleaner = Cleaner(cleaner)

    hall_c.movie_session(movie, my_list, name_cleaner)
