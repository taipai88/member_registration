📁 專案結構如下：
csharp
複製編輯
member_registration/
├── app.py                  # 主程式 (Flask)
├── members.db              # SQLite 資料庫
├── static/
│   └── uploads/            # 上傳照片儲存資料夾
│   └── images/             # 精美羽球背景圖片
├── templates/
│   └── index.html          # 前端網頁模板
└── README.md               # 使用說明
________________________________________
📖 README.md 內容摘要：
markdown
複製編輯
# 會員建檔系統（Flask + SQLite）

這是一個以 Flask 建立的簡易會員建檔與查詢系統，支援照片上傳與資料庫儲存，介面採淺綠色背景並搭配羽球專業風格圖片。

## ✅ 功能簡介
- 📋 會員建檔（含上傳照片）
- 🔍 會員查詢（可查詢單筆 / 預設顯示全部）
- 💾 SQLite 資料庫儲存
- 🖼 美觀簡潔 UI 設計（羽球主題）

## 🏗 專案架構
app.py # Flask 應用主程式
members.db # SQLite 資料庫
static/ # 靜態資源資料夾（圖片、上傳圖檔）
templates/ # HTML 模板
shell
複製編輯

## ▶ 如何執行
```bash
# 安裝 Flask
pip install flask

# 啟動伺服器
python app.py
瀏覽器開啟：http://127.0.0.1:5000

