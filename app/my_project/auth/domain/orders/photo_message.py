from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import ForeignKey

from app.my_project import db
from app.my_project.auth.domain.i_dto import IDto


class PhotoMessage(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "photo_message"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    arrival_time = db.Column(db.Datetime, nullable=False)
    sender = db.Coulmn(db.String(50), nullable=False)
    text_chat_name = db.Column(ForeignKey("text_chat.name"))

    # Relationship 1:M
    client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"PhotoMessage({self.id}, '{self.arrival_time}', '{self.sender}', ''{self.text_chat_name})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "arrival_time": self.arrival_time,
            "sender": self.sender,
            "text_chat_name": self.text_chat_name,
            "client_type_id": self.client_type_id or "",
            "client_type": self.client_type.type if self.client_type is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PhotoMessage:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = PhotoMessage(
            id=dto_dict.get("id"),
            arrival_time=dto_dict.get("arrival_time"),
            sender=dto_dict.get("sender"),
            text_chat_name=dto_dict.get("text_chat_name"),
            client_type_id=dto_dict.get("client_type_id")
        )
        return obj
