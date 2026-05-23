from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import datetime
from typing import Optional

# 1. Definir la Base de Datos
class LecturaSensor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    temperatura: float
    timestamp: str = Field(default_factory=lambda: datetime.now().strftime("%H:%M:%S"))

sqlite_url = "sqlite:///riss_database.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# 2. Inicializar la API
app = FastAPI(title="RISS API v1.0")

# Permitir que el HTML se comunique con esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# 3. Rutas de la API
@app.post("/api/lecturas/")
def guardar_lectura(temperatura: float):
    with Session(engine) as session:
        nueva_lectura = LecturaSensor(temperatura=temperatura)
        session.add(nueva_lectura)
        session.commit()
        session.refresh(nueva_lectura)
        return nueva_lectura

@app.get("/api/lecturas/")
def obtener_lecturas():
    with Session(engine) as session:
        # Traer los últimos 10 registros
        lecturas = session.exec(select(LecturaSensor).order_by(LecturaSensor.id.desc()).limit(10)).all()
        # Invertir la lista para que salgan en orden cronológico en la gráfica
        return lecturas[::-1]