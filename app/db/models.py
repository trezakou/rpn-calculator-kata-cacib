import sqlalchemy as sa
from .sessions import Base
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType
from uuid import uuid4


class Stacks(Base):
    __tablename__ = "stacks"

    id = sa.Column(sa.Uuid, primary_key=True, index=True, default=uuid4)
    creation_date = sa.Column(
        sa.DateTime, server_default=sa.func.now(), nullable=False)  # type: ignore
    content = sa.Column(MutableList.as_mutable(PickleType),
                        default=[])
