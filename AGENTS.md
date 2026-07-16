# AGENTS.md

## 專案定位

此 repository 是公開發布的紐西蘭冬季自駕旅行手冊。

- 網站：`http://gpt.greenparty.org.tw/nz-handbook/`
- Repo：`g26910033/nz-handbook`
- 主要檔案：`src/sections/*.html` 與 `src/styles.css`（並由 `build.py` 生成 `index.html`）
- 語言：台灣繁體中文（`zh-Hant`）
- 發布方式：GitHub Pages，`.github/workflows/build-deploy.yml` 會在 `main` push 後自動執行 `build.py` 並部署整個 repository。
- 內容目標：冬季雙島自駕手冊，包含財務、行程、票券、住宿付款、導航、安全、通訊與作戰卡。
- `README.md` 說明維護模式已改為「小檔來源 + 自動 build」。
- `_headers` 設定 `Cache-Control: no-cache, no-store, must-revalidate`，用於避免靜態頁快取。

## 核心規則

1. 將 `src/sections/` 與 `src/styles.css` 視為內容的事實來源，`index.html` 僅為 build 產物，**嚴禁直接手動修改 `index.html`**。
2. 不要把手冊拆成多頁，除非使用者明確要求（最後 build 出的結果仍為單一 HTML）。
3. 不要把專案改成框架、bundler、React/Vue app 或複雜的 build pipeline。維持單純的 Python 組裝腳本。
4. 維持靜態 HTML（拆分為模組）與獨立 CSS（`src/styles.css`）。
5. 不新增外部 dependencies、npm packages、analytics、trackers 或外部 CSS framework。
6. 不新增 JavaScript，除非使用者明確要求互動行為。
7. 優先做小範圍、可檢查的修改，不做整份重寫。
8. 保留手機閱讀性與 A4 列印可讀性。
9. 旅遊內容以台灣繁體中文為主；外國地名、飯店、景點、平台、信用卡產品可中英雙語。
10. 不可默默移除旅行關鍵資訊，例如付款日期、訂房或取消期限、安全提醒、緊急聯絡、住宿名稱、地圖連結。
11. 每次更新網頁時，同步更新 `src/sections/00-cover.html` 中的「網頁更新」時間；此標籤應不影響閱讀，且列印時隱藏。

## Codex execution rules

- 每次只處理一個明確步驟，完成後停止並回報。
- 不得遞迴讀取整個專案。
- 除非明確要求，不讀取：
  - `.git/`
  - `node_modules/`
  - `dist/`
  - `build/`
  - `.cache/`
  - `venv/`
  - `**pycache**/`
  - 大型日誌與備份資料夾
- 讀取大型文字檔時，先使用搜尋、`head`、`tail` 或指定行數，不得直接輸出全文。
- PDF 優先使用 `pdftotext`，逐檔處理，不得一次將所有 PDF 全文載入上下文。
- 終端機指令必須使用非互動模式。
- 不得執行 `sudo` 或等待密碼輸入。
- 不得讓開發伺服器以前景程序永久執行。
- 指令超過 10 分鐘沒有新輸出時，停止指令並回報阻塞原因。
- 終端機輸出過長時，只保留錯誤段落與最後 200 行。
- 每完成一個階段，更新 `HANDOFF.md`。
- 不要因驗證結果不理想而無限重複修改；最多重試兩次，之後回報。

## 每次更新前的專案巡讀

每次處理本專案更新時，都要先巡讀專案資料夾，並把新學到、對後續工作有用的資訊整理回 `AGENTS.md`。

1. 先查看工作樹與檔案清單：
   - `git status --short --branch --untracked-files=all`
   - `find . -maxdepth 3 -type f | sort`

2. 巡讀與任務相關的專案檔案：
   - `AGENTS.md`
   - `README.md`
   - `_headers`
   - `.github/workflows/*`
   - `src/sections/` 內的對應章節 HTML
   - `assets/` 內本次會用到或新出現的靜態資產

3. 將學到的資訊寫入 `AGENTS.md`，格式要清楚，優先更新下列區塊：
   - `專案定位`
   - `目前專案事實`
   - `內容慣例`
   - `工作流程`
   - `已知注意事項`

4. 不要把短期推測、未確認資訊、私人資訊、密碼、完整電話、護照、保單、住家地址、醫療細節或信用卡資訊寫進 `AGENTS.md`。
5. 如果工作樹已有他人或使用者留下的未提交變更，先分辨本次任務範圍；不要誤提交不屬於本次任務的檔案。
6. 若本次有實質網頁更新，`AGENTS.md` 的專案學習更新應與本次修改一起提交；若只是檢查且沒有實質變更，回報無需提交。

## Git 工作流程

1. 除非使用者要求分支或 PR，否則在目前分支工作。
2. 對 `g26910033/nz-handbook` 工作時，必須修改 `src/sections/` 內的對應檔案或 `src/styles.css`，並執行 `python3 build.py` 產出結果。
3. 編輯前先檢查相關區塊，不要猜測檔案內容。
4. 若需要 PR，必須先明確告知使用者。
5. 修改完成後至少執行：
   - `python3 build.py`
   - `git diff -- src/ AGENTS.md build.py`
   - `grep -n "<title>" build.py index.html`
   - `grep -n "導航總表" src/sections/03-nav.html`
   - `grep -n "景點票券" src/sections/02-tickets.html`
   - `git diff --check`
6. 完成後直接 commit 到目前分支。
7. 除非使用者明確要求不要 push，完成 commit 後推送到目前分支的 GitHub 遠端。
8. 若工作樹有本次無關變更，只 stage 本次任務需要的檔案。
9. 最終回覆包含：
   - 修改摘要
   - 修改檔案
   - commit SHA
   - 尚未解決或刻意未處理的問題

## 內容慣例

### 財務
- 保留原幣與 TWD 換算，不可只留台幣合計。
- 使用使用者指定或本次查到的最新匯率。
- 匯率變更時，重算：
  - 財務摘要
  - 景點票券表
  - 住宿付款表
  - 相關總額
- 不移除原幣金額。
- 付款建議中應保留拒絕 DCC 的提醒。
- 已刷卡且已有 TWD 實刷值的項目，不要用新匯率覆寫實刷金額，除非使用者明確要求。

### 景點票券
- 區塊標題：`景點票券與執行時間`。
- 票券表欄位：
  - 日期／時間
  - 項目
  - 原幣/計算
  - TWD
  - 備註
- 除非使用者要求，不要用 `保留` 作為決策標籤；使用 `備註`。
- 景點與溫泉名稱中英雙語，例如：
  - `Hanmer Springs Thermal Pools 漢默溫泉`
  - `Tekapo Springs Hot Pools 蒂卡波溫泉`
  - `Steampunk HQ 蒸汽龐克總部`
- 若景點取消，除非使用者要求保留取消紀錄，否則從票券表移除。

### 導航
- 住宿導航使用多點路線：
  - 北島住宿節點環線
  - 南島住宿節點環線
- 景點、溫泉、極光、免費停點使用單點 Google Maps 連結。
- 單點地圖表不要重複同一類別；按類別合併：
  - 付費景點
  - 溫泉
  - 極光
  - 免費停點
- 住宿付款表可以保留單點地圖連結，因為該表用於付款與入住執行。
- 若使用 `assets/maps/*.svg` 等靜態地圖資產，維持為靜態檔，不新增外部框架或 build step。

### 住宿付款表
住宿付款表必須保留：
- 日期
- 地點／住宿
- 地圖
- 金額
- 刷卡／執行
- 付款／取消死線

不可移除付款死線、取消死線、信用卡名稱、訂房平台或執行日期。

### 行程
- 保留上午／中午／下午／夜間邏輯。
- 北島、基督城與南島作戰卡都應維持每日卡片格式；基督城整備週不要退回只有日期摘要的表格。
- 不新增高風險夜駕計畫。
- 冬季駕駛原則：
  - 避免清晨進山路。
  - 避免天黑後跑鄉間或山路。
  - 高山道路出發前確認 NZTA 與 MetService。
  - 先刪景點，不犧牲住宿抵達時間。
- 景點中文名稱優先採台灣較通用譯名並與英文並列；例如 `Rotorua 羅托魯瓦`、`Franz Josef Glacier 法蘭士約瑟夫冰河`、`Fox Glacier 福克斯冰河`、`Arthur's Pass 亞瑟山口`、`Church of the Good Shepherd 好牧羊人教堂`。

### 公開網站與隱私
本網站是公開網站。若使用者要求加入下列資訊，先提醒公開風險：
- 護照號碼
- 保單號碼
- 完整電話
- 私人住家地址
- 醫療細節
- 信用卡資訊
若私人地址已被使用者有意保留，不要自行移除；但在相關修改時提醒公開風險。

## 目前專案事實

- 目前分支：`main`
- GitHub Pages URL：`http://gpt.greenparty.org.tw/nz-handbook/`
- Repo：`g26910033/nz-handbook`
- 主檔案：改以 `src/sections/` 模組化分割維護，透過 `build.py` 編譯為 `index.html`。
- `<title>` 位於 `build.py` 的 HTML shell 中，並於 build 後出現在 `index.html`；`src/sections/00-cover.html` 只維護封面內容與網頁更新標籤。
- 目前旅行型態：冬季自駕、財務控制、低風險駕駛、多數餐食自炊。
- 目前頁面右上角有 `網頁更新` 標籤；位於 `src/sections/00-cover.html` 中，桌面固定右上角，手機在頁首，列印時隱藏。
- 目前 Mastercard 匯率來源：`https://www.mastercard.com/global/en/personal/get-support/currency-exchange-rate-converter.html`；官方轉換器無法回傳結果時，以 SG Rates MasterCard 同日 `NZD`/`MYR`/`USD`/`TWD` 對 `SGD` 交叉換算。
- 目前 Mastercard 匯率基準：`07/13`
  - `1 NZD = 18.6206 TWD`
  - `1 MYR = 7.9075527 TWD`
  - `1 USD = 32.1600179 TWD`
- 目前財務摘要：
  - 已支出：`TWD 201,837`
  - 待支出：`TWD 61,723`
  - 總預估：`TWD 263,560`
- 目前 `src/sections/` 中已有導航總表、景點票券與執行時間、住宿與付款總表等核心區塊的源碼。
- 2026-07-07 已結束北島行程，`src/sections/08-north.html` 已改為 Gmail 每日提醒與實際執行整併後的北島完成版；後續調整北島段時應維持實際紀錄語氣。
- 2026-07-08 Gmail確認回程改為律德Jetstar JQ226 2026-08-02 06:15 CHC → 07:35 AKL；改票費NZD6.09已列入已支出交通。
- 2026-07-08 使用者確認車子是給佳蓉後續使用，不賣車；回程段落應避免「賣車、出售、上架」語氣。
- 2026-07-12 使用者確認購車計畫仍保留，購入的自有車供佳蓉後續使用；南島07/20 10:00至08/01 10:00大環線另租YES Rentals Toyota Aqua Hybrid或同級車，兩套車輛與保險流程必須分開記錄。
- 2026-07-12 Gmail確認YES租金總額NZD205.20，確認信列NZD41.04已結算／折抵、餘額NZD164.16，Basic Insurance、第二駕駛與雪鏈為NZD0；未買YES Zero Risk，取車需NZD250信用卡預授權。
- 2026-07-12 RentalCover第三方保障期間為07/20至08/01、總價NZD149.12；保障文件解析出的居住資格與訂單資料存在不一致疑慮，未取得書面確認前不得在手冊中視為確定有效保障。
- 2026-07-12 使用者確認自購車最快07/15才能取得；07/15只安排交車、冷車試駕、過戶、保險與低速驗收，不安排漢默長途。Hanmer Springs漢默溫泉行程改排07/17，Bookme票券仍須以Ask Me書面改期確認為準。
- 2026-07-12 Gmail確認Kingston TOP 10 Holiday Park（07/24）標準小屋已付NZD91.76（含NZD1.76信用卡附加費）／實刷TWD1,714，入住前72小時以上取消可退75%。公開手冊不放訂房編號、地址或聯絡方式。
- 2026-07-14 Gmail確認兩筆Hanmer Springs Thermal Pools票券已改為07/17 10:00；07/16 09:30安排獨立驗車，僅在無重大問題後辦理過戶並線上投保State。State尚非已生效保單，財務先以首月車險加規費NZD75估列；公開手冊不得放車牌、報價號、保單號、VIN、賣方資訊或地址。
- 2026-07-14 使用者更新購車待支出為NZD3,880本金、NZD70驗車、NZD75首月車險加規費，且不買自有車雪鏈；基督城二姑家補貼改NZD300。YES Rentals訂金NZD41.04與RentalCover實刷TWD2,741已支出，YES餘額NZD164.16待付。南島油資採NZD370、基督城NZD100的上限；大馬機場旅館來回接駁MYR40.16加TWD39已支出。
- 2026-07-16 使用者確認自有車已完成購買：購車NZD3,630、修理加驗車NZD570，合計NZD4,200；本次不買雪鏈，車險與規費不由本次支出負擔。公開手冊不放車牌、VIN、賣方、保單或過戶私人資料。
- 2026-07-08 使用者確認08/01晚上不睡，08/02 01:30二姑載律德去CHC；08/02 AKL國際線銜接MH144前會安排貴賓室，若排隊或延誤則壓縮貴賓室、不壓登機口緩衝。
- 工作樹可能出現 `.DS_Store` 或 Mac 的隱藏檔；不要納入提交，除非使用者明確要求。

## 已知注意事項

- Mastercard 官方頁面可被瀏覽器開啟；本機 `curl` 或直接 API 請求可能被 Mastercard/Akamai 擋下。必要時使用瀏覽器同源查詢。
- 每日匯率更新可使用 Mastercard 中國 converter：`https://www.mastercard.com.cn/zh-cn/personal/get-support/convert-currency.html`。
- Mastercard current rate 查詢可使用頁面同源請求的 `fxDate=0000-00-00`，應以官方回應中的 `data.fxDate` 作為手冊匯率基準日期。
- 若官方 Mastercard 頁面可開但本機直接 API/JS 仍被 Akamai 或瀏覽器擴充阻擋，可用 SG Rates 的 MasterCard 同日 NZD/MYR/USD/TWD 對 SGD 匯率交叉驗證，使用前必須確認四個幣別的 MasterCard 日期一致。
- 匯率更新時要只在有實質匯率或換算變更時 commit。
- 已刷卡 TWD 實刷值應優先於估算匯率。
- 北島已完成段落不要加入公開敏感資訊，例如訂房 PIN、完整訂單號、信用卡尾號或私人聯絡資訊；必要時只保留住宿/平台/付款狀態與已刷金額。
- 若修改導航或地圖區塊，確認住宿多點路線與景點單點連結的分工沒有被破壞。
- 若出現未追蹤的 `assets/maps/*.svg`，先確認是否屬於本次需求，再決定是否提交。
- 車險條款與報價僅供本機評估時，放在 `private/insurance/`；此目錄由 `.gitignore` 排除，不得 stage、提交或公開引用其個人資料。
- 信用卡帳單與未出帳明細截圖僅供本機核帳時，放在 `private/billing/`；此目錄由 `.gitignore` 排除，不得 stage、提交或公開引用卡號、帳務或個人資料。
- YES Rentals與RentalCover的公開手冊只保留營運商、日期、車型、費用、付款狀態、保障分工與執行提醒，不放訂單號、保單參考號、私人地址或完整電話。
- Bookme景點改期在平台尚未書面確認前，票券表應標示「改期申請中」，不可把新日期寫成已確認，也不可公開訂單號碼。

## 歷史變更紀錄

### 2026-06-25（index.html 純格式重排）
- Commit：`c786d9a`
- 變更性質：**僅格式化**（將 HTML tag 間 `><` 改為換行），未調整行程/金額/連結等實質內容。

### 2026-06-26（模組化重構與自動化建置）
- Commit：`57693c8`
- 變更性質：**架構大改版**。
- 執行方式：
  - 將單一 `index.html` 捨棄，拆分為 12 個章節檔（位於 `src/sections/`）與 1 個 CSS 檔（`src/styles.css`）。
  - 建立 `build.py` 負責無損組裝發布檔。
  - 移除舊版 `static.yml`，改由 `.github/workflows/build-deploy.yml` 於 Push 至 `main` 時自動編譯與提交 `index.html`。
- 驗證結果：Canonical 檢查 100% 一致。
