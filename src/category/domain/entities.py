from datetime import datetime
from dataclasses import dataclass, field

@dataclass()
class Category:

    name: str
    description: str
    is_active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now())
