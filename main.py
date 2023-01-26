import uvicorn
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app import predict

templates=Jinja2Templates(directory="templates")

app=FastAPI()


@app.get('/',response_class=HTMLResponse)
def home(request:Request):
    context={'request':request}
    return templates.TemplateResponse('index.html',context)

@app.post('/upload',response_class=HTMLResponse)
async def get_spam(request:Request,message:str=Form(...)):
    spam_pred=predict(message)
    msg=[]
    if spam_pred[0]==1:
        context={'request':request,'msg':'Spam'}
    else:
        context={'request':request,'msg':'Not a Spam'}
    return templates.TemplateResponse('index.html',context)

if __name__=="__main__":
    uvicorn.run(app)