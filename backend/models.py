from sqlalchemy import Column, Text
from .database import Base

# define the flower model
class Flower(Base):
    __tablename__ = 'flowers'

    botanical_name = Column("Botanical Name", Text, primary_key=True)
    common_name = Column("Common Name", Text)
    attracts = Column("Attracts Wildlife", Text)
    color = Column("Flower Color", Text)
    season = Column("Flowering Season", Text)
    sun = Column("Sun", Text)
    water = Column("Water Requirement", Text)
    companions = Column("Companions", Text)
    communities = Column("Communities", Text)
    tips = Column("Tips", Text)
    pests = Column("Pests", Text)
    plant_url = Column("Plant Url", Text)

    def __repr__(self):
        return f"<Flower(botanical_name='{self.botanical_name}', common_name='{self.common_name}', attracts='{self.attracts}', color='{self.color}', season='{self.season}', sun='{self.sun}', water='{self.water}', companions='{self.companions}', communities='{self.communities}', tips='{self.tips}', pests='{self.pests}', plant_url='{self.plant_url}')>"