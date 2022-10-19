from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

from __seedwork.domain.entities import Entity

@dataclass(kw_only=True, frozen=True, slots=True)  # init, repr, eq
class Category(Entity):

    name: str
    description: Optional[str]
    is_active: Optional[bool] = True

    # pylint: disable=unnecessary-lambda
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
    )

    def __post_init__(self):
        if not self.created_at:
            self._set('created_at',  datetime.now())
        self.validate()

    def update(self, name: str, description: str):
        self._set('name', name)
        self._set('description', description)
        self.validate()

    def activate(self):
        self._set('is_active', True)

    def deactivate(self):
        self._set('is_active', False)

    def validate(self):
        pass
