from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric

# If you had relationships you'd need these:
# from sqlalchemy.orm import relationship

from database import Base


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Numeric(10, 2))
    forward_pe = Column(Numeric(10, 2))
    forward_eps = Column(Numeric(10, 2))
    dividend_yield = Column(Numeric(10, 2))
    ma50 = Column(Numeric(10, 2))
    ma200 = Column(Numeric(10, 2))

    # If had relationships
    # items = relationship("Item", back_populates="owner")