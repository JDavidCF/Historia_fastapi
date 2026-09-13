from fastapi import APIRouter, HTTPException
from schemas import HistoriaRequest
from services import avanzar_motor_narrativo, obtener_opciones
router = APIRouter()

@router.post("/historia")
def jugar(data: HistoriaRequest):
    try:
        return avanzar_motor_narrativo(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

        
@router.get("/historia/{nodo}")
def mostrar_opciones(nodo: str):

    try:
        return obtener_opciones(nodo)

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))