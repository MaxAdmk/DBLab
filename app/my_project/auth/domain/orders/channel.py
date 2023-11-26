from __future__ import annotations
from typing import Dict, Any

from app.my_project import db
from app.my_project.auth.domain.i_dto import IDto


class Channel(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "channel"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True , unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)

    # Relationship 1:M
    client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Channel({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "client_type_id": self.client_type_id or "",
            "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Channel:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Channel(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            client_type_id=dto_dict.get("client_type_id")
        )
        return obj
