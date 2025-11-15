from app.main_app import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    # オブジェクトを直接渡す
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)