from fastapi import FastAPI 
from pydantic import BaseModel 
# Khoi tao ung dung
app = FastAPI()

# Endpoint mac dinh (Trang chu)
@app.get("/")
def read_root():
    return{"message": "Hello Mentor, server API của em đã chạy"}

# Endpoint tính tổng 
@app.get("/tinh-tong")
def phep_cong(a: int,b: int):
    # Trả kết quả về dưới dạng JSON 
    return {"Số thứ nhất": a, "Số thứ hai": b,"Kết quả": a + b}

#1. Định nghĩa cấu trúc dữ liệu (JSON) mà API mong muốn nhận được
class ThongTinVanBan(BaseModel):
    noi_dung: str

#2. Endpoint POST xử lý văn bản
@app.post("/dem-tu")
def dem_so_tu(van_ban: ThongTinVanBan):
    danh_sach_tu = van_ban.noi_dung.split()
    so_luong = len(danh_sach_tu)

    return {
        "thong-bao": "Đã đếm xong",
        "so_tu": so_luong
    }