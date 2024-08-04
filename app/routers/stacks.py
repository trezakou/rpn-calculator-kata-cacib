from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, delete
from app.db import sessions
from app.db.models import Stacks
from app.db.schemas import stacks as stacks_schema
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from typing import Sequence
from uuid import UUID
from enum import Enum


router = APIRouter(prefix="/rpn", tags=["RPN calculator"])


class OpEnum(Enum):
    add = "add"
    multiply = "multiply"
    substract = "substract"
    divide = "divide"


@router.get("/op")
async def get_all_available_operands(
):
    return list(OpEnum._member_map_.values())


@router.get("/op/{op}/stack/{id}")
async def apply_operand_to_stack(
    op: OpEnum,
    id: UUID,
    db: AsyncSession = Depends(sessions.get_async_session),
) -> stacks_schema.Stacks:
    q = await db.scalars(select(Stacks).filter(Stacks.id == id))
    stack = q.first()
    if not stack:
        raise HTTPException(status_code=404, detail="Stack not found")
    if len(stack.content) < 2:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                            detail="Cannot perform operation, stack should contain at least twos elements")
    B = stack.content.pop()
    A = stack.content.pop()
    match op:
        case OpEnum.add:
            stack.content.append(A + B)
        case OpEnum.substract:
            stack.content.append(A - B)
        case OpEnum.multiply:
            stack.content.append(A * B)
        case OpEnum.divide:
            if not B:
                raise HTTPException(
                    status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Cannot divide by 0")
            stack.content.append(A / B)
        case _:
            raise HTTPException(
                status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Operation not implemented")
    await db.commit()
    return stack


@ router.get("/stack")
async def get_all_stacks(
    db: AsyncSession = Depends(sessions.get_async_session),
) -> Sequence[stacks_schema.Stacks]:
    q = select(Stacks)
    result = await db.execute(q)
    stacks = result.scalars().all()
    if not stacks:
        raise HTTPException(status_code=404, detail="No stacks found")
    return stacks


@ router.get("/stack/{id}")
async def get_stack(
    id: UUID,
    db: AsyncSession = Depends(sessions.get_async_session),
) -> stacks_schema.Stacks:
    q = await db.scalars(select(Stacks).filter(Stacks.id == id))
    stack = q.first()
    if not stack:
        raise HTTPException(status_code=404, detail="Stack not found")
    return stack


@ router.post("/stack")
async def add_stack(
    stack: stacks_schema.StacksCreate,
    db: AsyncSession = Depends(sessions.get_async_session),
) -> stacks_schema.Stacks:
    stacks_db = Stacks(**stack.dict())
    db.add(stacks_db)
    await db.commit()
    return stacks_db


@ router.post("/stack/{id}")
async def push_new_value_to_stack(
    id: UUID,
    value: float,
    db: AsyncSession = Depends(sessions.get_async_session),
) -> stacks_schema.Stacks:
    q = await db.scalars(select(Stacks).filter(Stacks.id == id))
    stack = q.first()
    if not stack:
        raise HTTPException(status_code=404, detail="Stack not found")
    stack.content.append(value)
    await db.commit()
    return stack


@ router.delete("/stack/{id}")
async def delete_stack(
    id: UUID,
    db: AsyncSession = Depends(sessions.get_async_session),
) -> str:
    q = await db.scalars(select(Stacks).filter(Stacks.id == id))
    stack = q.first()

    if not stack:
        raise HTTPException(status_code=404, detail="Stack not found")

    q = delete(Stacks).filter(Stacks.id == id)
    await db.execute(q)
    await db.commit()
    return "ok"
