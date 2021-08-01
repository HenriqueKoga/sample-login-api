from core import db


class BaseModel:

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        db.session.flush()
        return obj

    @classmethod
    def get(cls, unique_id=None, **kwargs):
        if unique_id:
            return cls.query.filter_by(id=unique_id).first_or_404()

        if kwargs:
            return cls.query.filter_by(**kwargs).first_or_404()

    @classmethod
    def delete(cls, unique_id):
        obj = cls.get(unique_id)
        db.session.delete(obj)
        db.session.commit()
