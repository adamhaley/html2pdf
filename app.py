from fastapi import FastAPI, Body, Header, HTTPException, Response
from weasyprint import HTML
import uuid
import tempfile
import os

API_KEY = os.getenv("HTML2PDF_API_KEY", "")

app = FastAPI(title="Megyk HTML → PDF Service")

@app.post("/html-to-pdf")
async def html_to_pdf(
    html: str = Body(..., embed=True),
    x_api_key: str = Header(None)
):
    # Optional API key validation
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        HTML(string=html).write_pdf(tmp.name)
        tmp.seek(0)
        pdf_bytes = tmp.read()

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename={uuid.uuid4()}.pdf"
        }
    )

