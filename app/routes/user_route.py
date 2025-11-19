from app.controllers.user_controller import router as user_router

def init_routes(app):
    app.include_router(user_router)
