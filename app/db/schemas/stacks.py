from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import List


class StacksBase(BaseModel):
    content: List[float]

    class Config:
        orm_mode = True


class StacksCreate(StacksBase):
    ...


class Stacks(StacksBase):
    id: UUID
    creation_date: date
