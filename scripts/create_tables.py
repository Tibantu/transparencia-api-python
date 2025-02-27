"""
Create Table
    Is a script responsable to create or drop tables

    By: Jonathan Mandombe
"""

# pylint: disable=W0611,C0415,E0401,C0413
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from core.config import settings
from db.session import postgres_async_engine


async def create_tables() -> None:
    """
    Create Tables Function
    """

    import models.__all_models

    print("Criando as tabelas no banco de dados...")

    async with postgres_async_engine.begin() as conn:
        #await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print("Tabelas criadas com sucesso.")


if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())
