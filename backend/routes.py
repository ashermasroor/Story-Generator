from fastapi import APIRouter
from starlette.responses import StreamingResponse, FileResponse,JSONResponse
from .schemas import OutlineRequest
from .utils import Story_Gen

router = APIRouter()

sg = Story_Gen()

@router.post("/sGen")
async def storyGen(request: OutlineRequest):
    return StreamingResponse(sg.generate_story(request.outline), media_type="text/plain")

@router.get("/download_pdf/{filename}")
async def download_pdf(filename: str):
    pdf_path = sg.get_pdf_file(filename)
    return FileResponse(pdf_path, media_type="application/pdf", filename=filename)

@router.get("/get_filename")
async def get_filename():
    filename = sg.get_latest_pdf_filename()
    return JSONResponse(content={"filename": filename})
