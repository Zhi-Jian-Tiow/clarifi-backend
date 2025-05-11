from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from dbcontext import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    category_group_id = mapped_column(ForeignKey("category_group.id"))
    category_group = relationship("CategoryGroup", back_populates="categories")

    def __repr__(self):
        return f"{self.name}"
