from app.database.db import Base
import app.models  # noqa: F401  -- registers all models

for name, table in Base.metadata.tables.items():
    print(f"{name:20} {len(table.columns)} columns")