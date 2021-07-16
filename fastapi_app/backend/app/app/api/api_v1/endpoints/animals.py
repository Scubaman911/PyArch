from fastapi import APIRouter

from app.schemas import AnimalFactModel

router = APIRouter()

@router.post("/info/")
def info(animal: str):
    """Returns info by animal name...it only knows kangaroo"""
    if animal == "kangaroo":
        resp = AnimalFactModel(id=1, name="kangaroo", fun_fact="Kangaroos Are the Largest Marsupials on Earth")
    else:
        resp = AnimalFactModel(id=0, name=animal, fun_fact="Unknown animal!")
    return resp
