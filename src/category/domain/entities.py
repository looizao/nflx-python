from datetime import datetime
from dataclasses import dataclass, field
import uuid

@dataclass(kw_only=True, frozen=True)
class Category:

    id: uuid.UUID = field(default_factory=lambda: uuid.uuid4())
    name: str
    description: str
    is_active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now())
