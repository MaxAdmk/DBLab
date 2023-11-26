from my_project.auth.dao import client_type_dao
from my_project.auth.service.general_service import GeneralService


class ClientTypeService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = client_type_dao
