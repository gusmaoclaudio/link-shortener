from pydantic import BaseModel, AnyHttpUrl, Field

class URLCreate(BaseModel):
    url: AnyHttpUrl
    custom_slug: str | None = Field(default=None, pattern=r"^[A-Za-z0-9-_]{3,32}$")

class URLInfo(BaseModel):
    slug: str
    url: AnyHttpUrl
    clicks: int

    class Config:
        from_attributes = True
