from pydantic import BaseModel, Field

from datetime import datetime

class User(BaseModel):

    birth_year: int = Field(gt=1920, lt=2026)
    
    def calculate_age(self) -> int:

        return datetime.now().year - self.birth_year

user1 = User(birth_year=1997)

print(user1.calculate_age()) # 29
