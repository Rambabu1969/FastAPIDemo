from pydantic import BaseModel

class house(BaseModel):
    Area: int
    BedRooms: int 
    BathRooms: int 