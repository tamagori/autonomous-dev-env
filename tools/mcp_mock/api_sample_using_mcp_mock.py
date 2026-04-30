# api.py
from fastapi import FastAPI

app = FastAPI()

# モックデータベース
MOCK_DB = {
    1: {"name": "高性能バッテリー", "price": 15000},
    2: {"name": "LiDARセンサー", "price": 85000},
    3: {"name": "ROS2対応モーター", "price": 32000},
}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """IDを受け取り、商品情報を返すAPI"""
    if item_id in MOCK_DB:
        return {"status": "success", "data": MOCK_DB[item_id]}
    return {"status": "error", "message": "Item not found"}
