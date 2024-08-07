from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .experiment import Experiment

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    taskUUID: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    expUUID: Mapped[str] = mapped_column(db.String(255), db.ForeignKey('experiments.expUUID'), nullable=False)
    status: Mapped[str] = mapped_column(db.String(50))
    resource_usage: Mapped[str] = mapped_column(db.Text)
    network_traffic: Mapped[str] = mapped_column(db.Text)
    logs: Mapped[str] = mapped_column(db.Text)
    
    experiment: Mapped['Experiment'] = relationship('Experiment', back_populates='tasks')