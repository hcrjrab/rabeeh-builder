from typing import Generic, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Generic repository for database operations.
    """

    def __init__(
        self,
        db: Session,
        model: type[ModelType],
    ):
        self.db = db
        self.model = model

    def get(self, item_id: int):
        return (
            self.db.query(self.model)
            .filter(self.model.id == item_id)
            .first()
        )

    def get_all(self):
        return self.db.query(self.model).all()

    def create(self, obj: ModelType):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj: ModelType):
        self.db.delete(obj)
        self.db.commit()
