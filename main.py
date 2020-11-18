from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def dashboard():
    """
    Displays the stock filterer dashboard
    """
    return {"Dashboard": "Home Page"}


@app.post("/stock")
def create_stock():
    """
    Creates a stock and stores in the DB
    """
    return {
        "code": "success",
        "message": "stock created"
    }