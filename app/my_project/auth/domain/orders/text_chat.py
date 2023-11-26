from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import ForeignKey

from app.my_project import db
from app.my_project.auth.domain.i_dto import IDto


class TextChat(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "text_chat"

    name = db.Column(db.String(50), primary_key=True, nullable=False)
    is_private = db.Column(db.Boolean, nullable=False)
    has_age_limit = db.Coulmn(db.Boolean, nullable=False)
    channel_id = db.Column(ForeignKey("channel.id"))

    # Relationship 1:M
    client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"TextChat({self.name}, '{self.is_private}', '{self.has_age_limit}', ''{self.channel_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "name": self.name,
            "is_private": self.is_private,
            "has_age_limit": self.has_age_limit,
            "channel_id": self.channel_id,
            "client_type_id": self.client_type_id or "",
            "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TextChat:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TextChat(
            name=dto_dict.get("name"),
            is_private=dto_dict.get("is_private"),
            has_age_limit=dto_dict.get("has_age_limit"),
            channel_id=dto_dict.get("channel_id"),
            client_type_id=dto_dict.get("client_type_id")
        )
        return obj
