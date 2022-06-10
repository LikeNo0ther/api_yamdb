from csv import DictReader

from django.core.management import BaseCommand

from users.models import User

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from users.csv"

    def handle(self, *args, **options):
        if User.objects.exists():
            print('users data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading users data")

        for row in DictReader(open('static/data/users.csv')):
            user = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                role=row['role'],
            )
            user.save()
