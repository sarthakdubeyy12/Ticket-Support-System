from fastapi import FastAPI
import routes
import resend
from typing import Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as api_router  # Import your API routes
from database import get_db

resend.api_key = "re_8H98JVfu_Ln1MQe85XzULfDcRgYpT9CfB"

app = FastAPI()

app.include_router(routes.router)
@app.post("/email")
def send_mail() -> Dict:
    params: resend.Emails.SendParams = {
        "from": "onboarding@resend.dev",
        "to": ["dubeysarthak47@gmail.com"],
        "subject": "Hello World",
        "html": "<strong>it works!</strong>",
    }
    email: resend.Email = resend.Emails.send(params)
    print("Working")
    return email

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



#admin part 

from app.routes import router, admin_router

app = FastAPI()

app.include_router(router)
app.include_router(admin_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
