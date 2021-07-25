from core import db


class BaseModel:

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def get(cls, unique_id=None, username=None):
        if unique_id:
            return cls.query.filter_by(id=unique_id).first()

        if username:
            return cls.query.filter_by(username=username).first()
