$mkdir MONGODB
$cd MONGODB/
$git clone https://github.com/mikeckennedy/mongodb-quickstart-course.git
$cd mongodb-quickstart-course/src/snake_bnb/src
$python3 -m venv .env --copies
$. .env/bin/activate
$python program.py
#with pymongo
  raw queries in MongoDB API -- PyMongo -- Database
#with an ODM (Object Document Mapper)
  Queries in terms of objects/classes translates to MongoDB API
    ODM -- PyMongo -- Database
#ODM (MongoEngine)
#Registering Connections local
$vi mongo_setup.py
  import mongoengine
  alias_core='core'
  db='snakebnb'
  mongoengine.register_connection(alias=alias_core,name=db)
#Registering Connections Multi-server
$vi mongo_setup.py
  import mongoengine
  alias_core='core'
  db='snakebnb'
  data=dict(
    username=user_from_config_or_env,
    password=password_from_config_or_env,
    host=server_from_config_or_env,
    port=port_from_config_or_env,
    authentication_source='admin',
    authentication_mechanism='SCRAM-SHA-1',
    ssl=True,
    ssl_cert_reqs=ssl.CERT_NONE)
  mongoengine.register_connection(alias=alias,name=db,**data)

$vi snakes.py
import datetime
import mongoengine
class Snake(mongoengine.Document):
  registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
  species = mongoengine.StringField(required=True)

  length = mongoengine.FloatField(required=True)
  name = mongoengine.StringField(required=True)
  is_venomous = mongoengine.BooleanField(required=True)

  meta = {
      'db_alias': 'core',
      'collection': 'snakes'
  }

$vi cages.py
import datetime
import mongoengine

from data.bookings import Booking


class Cage(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    name = mongoengine.StringField(required=True)
    price = mongoengine.FloatField(required=True)
    square_meters = mongoengine.FloatField(required=True)
    is_carpeted = mongoengine.BooleanField(required=True)
    has_toys = mongoengine.BooleanField(required=True)
    allow_dangerous_snakes = mongoengine.BooleanField(default=False)

    bookings = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {
        'db_alias': 'core',
        'collection': 'cages'
    }

$vi bookings.py
import mongoengine

class Booking(mongoengine.EmbeddedDocument):
    guest_owner_id = mongoengine.ObjectIdField()
    guest_snake_id = mongoengine.ObjectIdField()

    booked_date = mongoengine.DateTimeField()
    check_in_date = mongoengine.DateTimeField(required=True)
    check_out_date = mongoengine.DateTimeField(required=True)

    review = mongoengine.StringField()
    rating = mongoengine.IntField(default=0)

    @property
    def duration_in_days(self):
        dt = self.check_out_date - self.check_in_date
        return dt.days

$vi owners.py
import datetime
import mongoengine


class Owner(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)

    snake_ids = mongoengine.ListField()
    cage_ids = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'owners'
    }
