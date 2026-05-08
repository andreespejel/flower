from pydantic import BaseModel
from typing import Optional

class FlowerBase(BaseModel):
    botanical_name: str
    common_name: str
    attracts: Optional[str]
    color: Optional[str]
    season: Optional[str]
    sun: Optional[str]
    water: Optional[str]
    companions: Optional[str]
    communities: Optional[str]
    tips: Optional[str]
    pests: Optional[str]
    plant_url: Optional[str]

class FlowerResponse(FlowerBase):
    class Config:
        from_attributes = True