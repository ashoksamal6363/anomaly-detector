
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import variables as v

engine = create_engine(v.DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Frame(Base):
    __tablename__ = "frames"
    id = Column(Integer, primary_key=True)
    camera_id = Column(String)
    timestamp = Column(DateTime)
    storage_path = Column(String)
    llm_anomaly_flag = Column(Boolean)

class HumanLabel(Base):
    __tablename__ = "human_labels"
    id = Column(Integer, primary_key=True)
    frame_id = Column(Integer, ForeignKey("frames.id"))
    is_anomaly = Column(Boolean)
    labeled_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(engine)
