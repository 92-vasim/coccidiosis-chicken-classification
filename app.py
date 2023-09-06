from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from CNNClassifier.utils.common import decodeImage, save_file, delete_files_in_folder
from CNNClassifier.pipeline.prediction import PredictionPipeline


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

DELETE_FOLDER = "temporary"


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    delete_files_in_folder(DELETE_FOLDER)
    
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def upload_file(
    request: Request,
    file: UploadFile
    ):

    # Get the file size (in bytes)
    file.file.seek(0, 2)
    file_size = file.file.tell()

    # move the cursor back to the beginning
    await file.seek(0)
    
    content_type = file.content_type

    if file_size > 5 * 1024 * 1024:
        # more than 10 MB

        return templates.TemplateResponse("index.html", {"request": request, "message":"File is too large."})

    # check the content type (MIME type)
    elif content_type not in ["image/jpeg"]:

        return templates.TemplateResponse("index.html", {"request": request, "message": "Sorry! That is not image or not in jpeg format."})

    else:

        print(file.filename)
        image_path = save_file(file)
        predictor = PredictionPipeline(image_path)
        result = predictor.predict()
        print(f"This is output of image: {result[0]['status']}")
        final = result[0]['status']
        # final = ""

        # if result[0]['status'] == "Healthy":
        #     final = "Great! Chicken is healthy"
        # else:
        #     final = "Sorry, Chicken has symptoms of Coccidiosis"

        return templates.TemplateResponse("index.html", {"request": request, "message":"Successfully posted", "result":final})




if __name__ == "__main__":
    uvicorn.run("app:app", port=8829, reload=True)