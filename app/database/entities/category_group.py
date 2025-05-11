from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import mapped_column, relationship
from dbcontext import Base


class CategoryGroup(Base):
    __tablename__ = "category_group"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    categories = relationship("Category", back_populates="category_group")

    def __repr__(self):
        return f"{self.name}"
