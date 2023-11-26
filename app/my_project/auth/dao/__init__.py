# orders DB
from .orders.client_dao import ClientDAO
from .orders.client_type_dao import ClientTypeDAO

client_dao = ClientDAO()
client_type_dao = ClientTypeDAO()
