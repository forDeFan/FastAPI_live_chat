from pydantic import BaseModel

class UserValidator(BaseModel):
    """User model validator."""
    username: str

    class Config:
        orm_mode: bool = True