from __future__ import annotations
from typing import Dict, Any

from app.my_project import db
from app.my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "user"

    username = db.Column(db.String(50), primary_key=True, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(13), nullable=False)
    has_nitro = db.Column(db.Boolean, nullable=True)

    # Relationship 1:M
    client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"User({self.username}, '{self.email}', '{self.phone_number}', '{self.has_nitro}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "username": self.username,
            "email": self.email,
            "phone_number": self.phone_number,
            "has_nitro": self.has_nitro,
            "client_type_id": self.client_type_id or "",
            "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = User(
            username=dto_dict.get("username"),
            email=dto_dict.get("email"),
            phone_number=dto_dict.get("phone_number"),
            has_nitro=dto_dict.get("has_nitro"),
            client_type_id=dto_dict.get("client_type_id")
        )
        return obj
