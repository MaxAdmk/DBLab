from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import ForeignKey

from app.my_project import db
from app.my_project.auth.domain.i_dto import IDto


class NitroBoost(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "nitro_boost"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    duration = db.Column(db.Datetime, nullable=True)
    user_username = db.Column(ForeignKey("user.username"))

    # Relationship 1:M
    client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"NitroBoost({self.id}, '{self.duration}', '{self.user_username}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "duration": self.duration,
            "user_username": self.user_username,

            "client_type_id": self.client_type_id or "",
            "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> NitroBoost:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = NitroBoost(
            id=dto_dict.get("id"),
            duration=dto_dict.get("duration"),
            user_username=dto_dict.get("user_username"),
            has_nitro=dto_dict.get("has_nitro"),
            client_type_id=dto_dict.get("client_type_id")
        )
        return obj
