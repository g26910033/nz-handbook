# 紐西蘭冬季雙島自駕手冊

本 repo 用於部署 GitHub Pages (原 ufotime.netlify.app)。

## 維護模式：小檔來源 + 自動 build

專案已改用模組化維護，**請勿直接修改 `index.html`**。
GitHub Pages 仍以根目錄的 `index.html` 作為發布檔，但其內容由自動化流程統一生成。

### 如何修改內容？
1. 修改文字與章節：編輯 `src/sections/` 底下的對應小檔（如 `01-finance.html`）。
2. 修改樣式：編輯 `src/styles.css`。
3. 本地預覽：執行 `python3 build.py`，會重新生成最新的 `index.html`。
4. CI/CD：推送至 `main` 分支後，GitHub Actions 將會自動編譯並 Commit 最新的 `index.html`，隨後自動發布網頁。

主要檔案與目錄：
- `src/sections/`：各章節 HTML 片段
- `src/styles.css`：網站樣式
- `build.py`：建置組裝腳本
- `index.html`：自動生成的發布檔
- `_headers`：防快取設定
