from fastapi import FastAPI
import uvicorn
import routes

app = FastAPI()
router = routes.router

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)