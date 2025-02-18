from langchain_openai import ChatOpenAI
from fastapi.concurrency import run_in_threadpool
from fastapi import HTTPException
from fpdf import FPDF
from .schemas import SaveRequest
from .config import Config
import re
import os

llm = ChatOpenAI(
    model="microsoft_Phi-3.5-mini-instruct",
    api_key=Config.LLM_API_KEY,
    base_url=Config.LLM_BASE_URL,
    temperature=0.35,
    stream_usage=True
)

class Story_Gen:
    async def generate_story(self, outline: str):
        prompt = f"""
        Below is the idea for a story:

        {outline}

        Generate a detailed, original, and well-structured story with a minimum of 500 words. Use vivid descriptions, dialogues, and clear progression. Avoid repetition.
        """
        story_chunks = []

        async for chunk in llm.astream(prompt):
            story_chunks.append(chunk.content)
            yield chunk.content

        full_story =SaveRequest(text=''.join(story_chunks))
        await run_in_threadpool(self.save_to_pdf, full_story)

    def save_to_pdf(self, request:SaveRequest):
        """Saves the generated text as a PDF file."""
        text=request.text
        title = re.search(r"Title:\s*(.+)", text)
        if title:
            title_match = title.group(1).replace('"','')
        filename = f"{title_match.group(1) if title_match else 'story'}.pdf".replace(" ", "_")

        os.makedirs(Config.SAVE_DIR,exist_ok=True)

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text.encode('latin-1','replace').decode('latin-1'))
        pdf_path = os.path.join(Config.SAVE_DIR,filename)
        pdf.output(pdf_path,'F')

        print(f"PDF saved as: {pdf_path}")
        return filename

    def get_latest_pdf_filename(self):
        files = os.listdir(Config.SAVE_DIR)
        if not files:
            raise HTTPException(status_code=404, detail="No PDF files found")

        latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(Config.SAVE_DIR, f)))
        return latest_file

    def get_pdf_file(self, filename: str):
        pdf_path = os.path.join(Config.SAVE_DIR, filename)
        if not os.path.exists(pdf_path):
            raise HTTPException(status_code=404, detail="PDF file not found")
        return pdf_path
