from fastapi import APIRouter, Request, Response, status
from ..services.userService import UserService
from ..models.userDTO import UserDTO, UserUpdateDTO, UserCreateDTO

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def get_all_users(request: Request):    
    users = await UserService(request.app.state.db).get_all()
    return users

@router.get("/{id}")
async def get_user_by_id(id: str, request: Request, response: Response):
    try:
        user = await UserService(request.app.state.db).get_by_id(id)
        if(not user): raise Exception("User not found")
        
        return user
    except Exception as e:
        if(str(e) == "User not found"): 
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": str(e)}
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/")
async def create_user(user: UserCreateDTO, request: Request, response: Response):
    try:
        user = await UserService(request.app.state.db).create(user)
        return user
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": str(e)}

@router.put("/{id}")
async def update_user(id: str, user: UserUpdateDTO, request: Request, response: Response):
    try:
        user = await UserService(request.app.state.db).update(id, user)
        if(not user): raise Exception("User not found")

        return user
    except Exception as e:
        if(str(e) == "User not found"):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": str(e)}
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_user(id: str, request: Request, response: Response):
    try:
        user = await UserService(request.app.state.db).delete(id)
        if(not user): raise Exception("User not found")

        return user
    except Exception as e:
        if(str(e) == "User not found"):
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": str(e)}
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": str(e)}
