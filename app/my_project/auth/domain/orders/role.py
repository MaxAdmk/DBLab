from __future__ import annotations
from typing import Dict, Any

from app.my_project import db
from app.my_project.auth.domain.i_dto import IDto


class Role(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "role"

    name = db.Column(db.String(50), primary_key=True, nullable=False)
    color = db.Column(db.String(30), nullable=False)
    is_administrator = db.Column(db.Boolean, nullable=True)

    # Relationship 1:M
    client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Role({self.name}, '{self.color}', '{self.is_administrator}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "name": self.name,
            "color": self.color,
            "is_administrator": self.is_administrator,
            "client_type_id": self.client_type_id or "",
            "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Role:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Role(
            name=dto_dict.get("name"),
            color=dto_dict.get("color"),
            is_administrator=dto_dict.get("is_administrator"),
            client_type_id=dto_dict.get("client_type_id")
        )
        return obj
