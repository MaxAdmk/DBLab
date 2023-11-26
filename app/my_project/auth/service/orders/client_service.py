from t08_flask_mysql.app.my_project.auth.dao import client_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ClientService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = client_dao
