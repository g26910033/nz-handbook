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
- 目前 Mastercard 匯率來源：`https://www.mastercard.com/global/en/personal/get-support/currency-exchange-rate-converter.html`；官方轉換器無法回傳結果時，以 SG Rates MasterCard 同日 `NZD`/`USD`/`TWD` 對 `SGD` 交叉換算。
- 目前 JPY 匯率來源：永豐銀行牌告匯率的日圓即期賣出；不再維護 MYR 每日匯率，歷史 MYR 消費仍保留原幣與正式 TWD。
- 目前匯率基準：Mastercard `08/12`、永豐 `08/12 15:30`
  - `1 NZD = 18.9592740 TWD`
  - `1 USD = 32.1998633 TWD`
  - `1 JPY = 0.2041 TWD`
- 目前財務摘要：
  - 實際支出：`TWD 305,623`
  - 扣除購車`TWD 77,921`與佳蓉MAS車險`TWD 10,500`後的旅行淨支出：`TWD 217,202`
- 目前 `src/sections/` 中已有導航總表、景點票券與執行時間、住宿與付款總表等核心區塊的源碼。
- 財務總控表已進入旅程結案模式，採「實際支出總額、實際支出分類、可展開帳單核對、預算結案紀錄」四層結構；不再顯示待支出或總預估，未使用預算只作紀錄且不計入支出。
- 住宿逐筆入帳狀態以「住宿與付款總表」為單一來源；財務總控表只保留各期信用卡帳單合計與跨類別逐筆核對，不重複列住宿明細。
- 根目錄另有獨立的 `medical-consult.html` 線上問診整備頁；此頁不連入主手冊、不由 `build.py` 組裝，並以少量中文欄位、結構化選項及本機常用醫療詞彙轉換，產生可一次複製的英文問診說帖。修改獨立頁時不得連動改寫 `index.html` 或主手冊封面更新時間，除非使用者另行要求。
- 根目錄另有獨立的 `parking-incident-guide.html` 停車擦撞線上處理卡；此頁不連入主手冊、不由 `build.py` 組裝，提供 Police 105、MAS 線上理賠與車主書面聯絡流程。使用者在多次收到公開風險提醒後明確要求頁面載入本案姓名、出生日期、住址、電話、Email、保單號與車牌；僅限此獨立頁，不得擴散到主手冊或其他公開頁。修改時不得連動主手冊或封面更新時間。
- 2026-08-13 對方車主已在48小時內聯絡並明確表示將提出保險理賠，Police 105尚未提交；依《Land Transport Act 1998》第22(4)至(5)條，現行流程應維持「48小時內完整提供姓名、住址、電子地址、車牌與地點，立即送MAS，105改為選擇性或依MAS書面要求」，不得再把105顯示為本案必做。
- MAS現行Motor Vehicle Insurance Policy的Making a claim條款要求可能導致理賠時儘快通知MAS，只有懷疑犯罪時才明文要求向警方報案；一般停車擦撞並未把105編號列為理賠送件前提，但仍須配合MAS合理調查與補件要求。
- `parking-incident-guide.html` 應依當下必要性排序，不按機構分類：目前採「補齊車主法定資料、立即送MAS、保存與補件、條件式105、金額與責任」；已經傳出的訊息須標為完成並只提供必要補充，次要情境回覆收進可展開區，避免使用者重複傳送或誤把105當前置步驟。
- 車主後續提供保險理賠管道與案件編號時，教戰卡應將「索取對方保險資料」標為已完成，下一則訊息只需確認收到並補齊尚缺資料；對方案件資料應直接納入MAS送件及證據清單，不再重複詢問。
- 當完整資料已傳給車主時，停車事故卡首頁只保留尚未完成的MAS線上理賠；已完成的資料交換移至後段作為紀錄與送出MAS案號後的短訊息，避免誤導使用者再次傳送。
- 2026-08-13 使用者更正本次停車事故為佳蓉低速向前駛入車位時，以自車前角接觸停放中Mazda的右後保險桿，不是倒車事故；`parking-incident-guide.html` 的MAS與備用105事實敘述應明確使用 `driving slowly forward into a parking space`，不得改寫成倒車，也不自行加入gross negligence、reckless或deliberate等法律定性。
- 2026-08-13 已以MAS公開線上車險表單逐頁確認本案欄位；表單分為事故、其他人、駕駛、聯絡資料與送出五段。Gallagher Onesurance的`S2378774`是對方提供的理賠案件編號，不得填入表單的「對方保單號」欄位；應在事故敘述與對話附件中提供，未知個資不得猜填。
- 已簽發的MAS報價／Schedule只列`Full Licence / Issued by Other`，不顯示駕照持有年數；MAS一般線上投保報價頁只要求駕照類型與簽發國，只有回答曾被停牌、取消或有特別條件時才追問總持照年數。理賠表另有Years held欄位。MAS後續書面確認已把有效保單的海外／國際駕照資料更正。公開理賠表單的可選類型為Full、Restricted、Learner、Overseas，沒有International；理賠表應選Overseas，年數欄依首次取得日如實填寫，不可猜測。現行Schedule額外自負額未列持照年數項目。留存的早期MV971912 PDF曾誤列New Zealand，不能作為更正後駕照資料的依據。
- 本案駕駛資料在停車事故卡採「英文欄位＋完整中文問題＋直接填值」的短句格式：Me、Overseas、1年；酒精、非法藥物、影響駕駛的處方藥、DUI檢測與駕駛定罪拆成五題，各自附中文說明。不得將持照年數本身表述為額外自負額原因。
- 停車事故卡的MAS Section 1同樣採英文欄位、完整中文問題、選項中文意義與直接填值；事故經過的英文貼文標題亦附中文，避免使用者必須依英文猜欄位。
- 停車事故卡的MAS Section 1–5均維持英文欄位、中文含義及本案填法；英文事故經過下方須提供精簡中文核對版，並標示中文僅供核對、不貼入英文欄。
- 本案MAS「Is your vehicle still at the scene?」選No後的現時車輛位置，依使用者確認填入獨立停車事故卡既有的地址資料；不得擴散至主手冊。
- 本案事故時間依使用者最新確認為2026-08-12 2:35 pm（紐西蘭當地時間）；停車事故卡的MAS填值、英文事故敘述與中文核對版必須一致。
- 本案事故地點依使用者確認為53 Peterborough Street, Christchurch Central City, Christchurch 8013, New Zealand；對方Gerald Dwyer的電話已由使用者提供，可填MAS其他涉案人資料，僅限獨立停車事故卡。
- `parking-incident-guide.html`頁首必須同步顯示台北與紐西蘭更新時間；九碼版本號只依紐西蘭時間產生，格式為`MMDDHHmmN`，前八碼為月日時分，最後一碼為同分鐘更新序號。
- `medical-consult.html` 另含台灣健保境外自墊醫療費用核退限制、實體院所文件清單與中英索取話術；純線上問診不得在頁面上表述為可核退，內容應以健保署現行表單、期限及當季上限為準。
- `medical-consult.html` 採手機優先的「安全判斷、填資料、複製英文、選線上醫師、領藥、實體備案」行動流程；醫療平台、時段與費用屬易變資料，更新備案時須以業者或 Health New Zealand 官方頁面重查，且實體費用必須區分 casual 與 non-resident／non-eligible 資格。
- `medical-consult.html` 的實體診所表應把「必須預約」與「可直接 walk-in」分開；目前 My Medical 對海外訪客列 NZD125，但 casual visitor 必須電話預約，Patient Portal 僅供已註冊病人使用。
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
- 2026-07-17 使用者確認購車相關支出中的NZD3,200為現金分次換匯：NZD3,000以18.5515、NZD200以18.2275，現金合計TWD59,300；其餘NZD1,000仍暫按既有估算保留，待取得實刷或實際換匯資料再替換。
- 2026-07-18 依06/26至07/17帳單與授權明細新增餐飲／食品已支出TWD11,478.85、生活用品／購物已支出TWD8,223.25；未出帳消費列為已支出待入帳，餐飲剩餘預算同步扣除。Waikite現場、Te Kuiti I-Site、Kapa Haka、Hurunui I-Site與Hanmer現場消費歸生活用品／購物。
- 2026-07-18 使用者確認不去Christchurch Gondola基督城纜車；票券、TWD1,510待支出、導航連結與07/19行程均移除，不保留取消紀錄。
- 2026-07-18 Gmail確認Skyline Queenstown Gondola + 3 Luge Rides皇后鎮纜車＋3次滑車雙人票由KKday以TWD3,360完成刷卡授權與款項確認，使用日07/24；KKday仍標示訂單處理中，因此公開手冊列為已支出、待出票，不公開訂單號或信用卡資訊。
- 2026-07-19 依07/18至07/19未出帳明細新增餐飲／食品TWD1,351、購物TWD2,953、Supercheap Auto交通TWD94與MOBIL SYDENHAM油資NZD48.19（暫估TWD913）；新增交易的海外手續費以1.5%暫估TWD80另列，正式請款後須按帳單替換並避免重複。
- 2026-07-20 Gmail確認07/27 Cozy room in Oamaru由住宿方要求取消，Booking.com已免費取消且不扣款；替代住宿為Empire Hotel Backpackers帝國背包旅舍經濟雙床房，NZD88.39尚未付款，07/25 23:59前可免費取消，07/26起取消或No-show收NZD95，19:00-20:00抵達已接受且最晚21:00辦理入住。公開手冊不放訂單號、PIN、完整地址或電話。
- 2026-07-22 使用者確認07/23穿越Haast Pass後先入住Lake Hāwea，再往Wānaka湖岸、Kai Kikokiko外帶、New World補給與免費夜間湖岸活動；07/24改經Cromwell至Queenstown，13:00-15:30執行Skyline，黃昏走免費湖岸後到Frankton PAK'nSAVE補給，再夜駕入住Kingston。兩晚均不排酒吧、電影、攀岩或其他付費夜間活動。
- 2026-07-23 依07/20至07/22未出帳明細新增餐飲／食品約TWD3,239、購物NZD12.50（Woolworths生活用品，約TWD238）、Challenge Greymouth油資TWD865、DOC停車TWD95與Hunters Moon Agoda授權TWD1,979；新增交易海外手續費以1.5%暫估TWD96。Hunters Moon原待支出NZD103.91已移入已支出，不重複計算。
- 2026-07-25 依07/23至07/25未出帳明細新增餐飲／食品TWD4,717、購物TWD695、MOBIL Queenstown油資TWD974、Queenstown LDC停車TWD184與Empire Hotel Backpackers Booking.com授權TWD1,676；新增交易海外手續費以1.5%暫估TWD124，MOTU TWD2列為實際手續費。07/25 Booking.com TWD2,302授權已取消，完全排除且不計入卡片回饋已用額；The Fort Timaru仍保留原訂待支出，付款狀態待確認。
- 2026-07-25 Gmail每日提醒確認07/25改走Kingston、Five Rivers、Mossburn、Te Anau鎮區、鳥類保護區、Ivon Wilson Park與湖岸，Milford Road僅保留嚴格條件下的短程備選；07/26依序安排Dolamore Park、Gore、Titri Creek、Lake Waihola、Dunedin Railway Station、St Clair、採買、Hunters Moon與Grand Casino Dunedin。
- 2026-07-25 Gmail逐筆核對確認：07/28 Lake Ruataniwha Holiday Park已免費取消，原待支出NZD79.11移除；較早的High Country Lodge訂單NZD121.50已取消退款，但其後另一筆High Country Lodge新訂單仍有效並已由聯邦M卡透過Booking.com付清NZD121.50，列已支出暫估TWD2,278並另估海外手續費TWD34。房型為雙人房附私人衛浴、不含餐，入住14:00-18:00、退房08:00-10:00；公開手冊不得放兩筆訂單號、PIN、地址或卡號。
- 2026-07-25 依永豐大戶卡已入帳截圖核對07/19至07/21交易：Denny's、BurgerFuel、Kmart、Monteith's、Four Square、Hokitika Sandwich與Woolworths本金均已在先前未出帳明細納入，僅更新狀態；Challenge Greymouth由TWD865改為入帳TWD866。九筆實際海外手續費合計TWD70取代同額估算，不重複增加。Te Anau Lakeview Holiday Park NZD68.81已付，從待支出移至已支出暫估TWD1,290，另估手續費TWD19。
- 2026-07-25 使用者確認除The Fort Timaru外所有住宿均視為已付；Wild Kea Lodge NZD68.83已由待支出移入已支出，另估海外手續費TWD19。住宿款待付只保留The Fort Timaru NZD114.51 → TWD2,147；基督城二姑家補貼NZD300尚未支付，仍併入「住」類別待支出，不得另開分類或算成已付住宿。
- 2026-07-25 Gmail收據確認YES Rentals租金原價NZD205.20、Merchant Services Fee NZD4.11、收據總額NZD209.31；收據列訂金／折抵NZD41.04、07/20尾款NZD168.27且餘額NZD0.00。使用者先前提供的訂金實付紀錄NZD42.06 = TWD781僅作實際匯率依據，1 NZD = TWD18.568711；整筆收據換算TWD3,887。NZD250僅為可退預授權，不列支出。
- 2026-07-25 使用者指定已支出的租車與車險併入「行」類別，不另列「租車／車險」；合併只調整分類呈現，不改已支出、待支出或總預估。
- 2026-07-26 Gmail確認Booking.com已收取The Fort Timaru全額NZD114.51；永豐07/25網路消費通知約當TWD2,157，依使用者指示以此TWD金額列已支出，另暫估1.5%海外交易手續費TWD32。住宿款已全數支付，待支出「住」只剩Upper Riccarton二姑家補貼NZD300。
- 2026-07-26 依永豐未出帳截圖新增PAK'nSAVE Dunedin TWD675、KFC Gore TWD367與CALTEX Te Anau TWD37及TWD1,024；前兩筆歸餐飲／食品，CALTEX兩筆暫歸行，TWD37標記小額授權待正式入帳確認。四筆海外手續費暫估TWD32；07/25 The Fort TWD2,157僅核對既有付款，已取消Booking.com TWD2,302持續排除。永豐幣倍本期回饋額度已用TWD19,866、剩TWD134；永豐大戶本期已用TWD15,003、剩TWD997。
- 2026-07-27 Gmail確認07/30 17:00已預訂Bullock Restaurant & Bar兩人First Table晚餐；餐點五折、每位至少點一杯飲料，兩人均須於17:15前入座。NZD15訂位費收據已收到，但尚無TWD實刷值；更新行程時不得誤寫成可折抵現場餐費。
- 2026-07-27 依永豐與玉山未出帳截圖新增On Street Parking TWD18、Woolworths兩筆TWD396.52、Badger & Mackerel兩筆TWD385.24、Steampunk HQ TWD563.77、Moeraki Boulders Gifts TWD154.10、Mosgiel Mobil TWD973.81與First Table NZD15／TWD281.88；另估海外手續費TWD42。Woolworths與Badger & Mackerel歸餐飲／食品，Mobil與停車歸行，Steampunk HQ歸票券，Moeraki Boulders Gifts歸購物，First Table歸餐飲且不可折抵現場餐費。Moeraki Boulders本身為免費景點，未列票券費。中信7月額度已滿；永豐幣倍剩TWD134、永豐大戶剩TWD979、聯邦M卡剩TWD49。玉山Unicard本批國外實體合格消費暫計TWD2,473.44，First Table網路訂位TWD281.88只算一般消費；後續確認使用任意選且紐西蘭為指定項目，應以+2.5%、月上限1,000點計算。
- 2026-07-30 依玉山07/28-07/29未出帳與永豐07/22-07/26已入帳截圖去重：新增玉山餐飲／食品TWD1,589.42、MOBIL Twizel油資TWD468.06，新增永豐MGL Wanaka與PAK'nSAVE Qtwn Fuel油資TWD1,305；十二筆既有永豐本金僅以正式入帳更新，淨差額TWD12。永豐大戶卡新顯示的實際手續費逐筆取代估值，KFC Gore仍暫估；玉山七筆另估手續費TWD31。財務更新為已支出TWD263,818、待支出TWD12,476、總預估TWD276,294。MGL Wanaka確認為加油站；玉山Unicard任意選紐西蘭加碼累計估計115點、剩885點。
- 2026-07-30 依玉山未出帳與加油機照片新增七筆有效消費：餐飲／食品TWD2,083.21、Fairlie Heritage Museum雙人票TWD375.58、NPD Timaru實際油資NZD80.87暫估TWD1,517，另估海外手續費TWD60。NPD顯示TWD3,778.58為預刷授權，完全排除且不得納入支出、預算或回饋額度。財務更新為已支出TWD267,862、待支出TWD8,930、總預估TWD276,792；玉山Unicard任意選紐西蘭加碼累計估計213點、剩787點。
- 2026-07-30 使用者確認新增三筆待支出：佳蓉自有車MAS全險年繳保費NZD552.08 → TWD10,356、給佳蓉的預備金NZD150 → TWD2,814、貓旅館TWD14,625。車險保單自07/30生效但尚待電話刷卡，MAS信用卡1.75%附加費尚未納入，實際付款後須以最終原幣與實刷TWD替換。財務更新為已支出TWD267,862、待支出TWD36,725、總預估TWD304,587；公開手冊不得放保單號、車牌或付款資料。
- 2026-07-30 Gmail更正07/31回基督城行程：淡菜採集改導航至Ellis Rd Beach Carpark，Marine Parade取消，Jack's Point Lighthouse只作地標；採集後依序前往PAK'nSAVE Timaru、Barker's Geraldine、Ashburton Museum、Rakaia Salmon Statue，17:20回Upper Riccarton基地冷藏淡菜，18:00後與二姑在Lincoln Road晚餐。公開手冊不得放基地私人地址。
- 2026-07-30 使用者確認08/01中午由二姑請吃Fuji Buffet & Bar小火鍋；下午律德與佳蓉到鄰近的PAK'nSAVE Riccarton採買伴手禮，再回基地完成行李與自有車交接。請客午餐不列使用者旅費，伴手禮待實際消費後再入帳。
- 2026-07-08 使用者確認08/01晚上不睡，08/02 01:30二姑載律德去CHC；08/02 AKL國際線銜接MH144前會安排貴賓室，若排隊或延誤則壓縮貴賓室、不壓登機口緩衝。
- 2026-07-31 Mastercard Global轉換器仍顯示錯誤；SG Rates四幣別MasterCard牌告日一致為07/30，交叉匯率更新為NZD/TWD19.0251290、MYR/TWD7.9406430、USD/TWD32.3501760。僅重算仍屬估算的已付款與待支出項目，實刷及授權TWD金額保持不變。
- 2026-07-31 永豐07/25-07/27已請款截圖與既有紀錄去重，DITTO、5 Rivers、Fresh Choice、CALTEX、PAK'nSAVE及手續費均不重複加總，僅將On Street Parking由授權TWD18替換為入帳TWD19。玉山新增Best Wok、Netherby Fish Shop與Barker's Foodstore & Eatery餐飲／食品TWD1,153.46、The Warehouse兩筆購物TWD505.29，另估海外手續費TWD25。財務更新為已支出TWD269,652、待支出TWD36,265、總預估TWD305,917；玉山Unicard任意選紐西蘭加碼累計估計255點、剩745點。
- 2026-08-01 Mastercard Global轉換器仍顯示錯誤；SG Rates四幣別頁面於2026-08-01 12:01同步產生最新MasterCard牌告，交叉匯率更新為NZD/TWD18.9923268、MYR/TWD7.9323604、USD/TWD32.2450412。僅重算仍屬估算的已付款與待支出項目，實刷及授權TWD金額保持不變。
- 2026-08-03 使用者更正貓旅館為已支出TWD13,650，新增兩次機場貴賓室已支出合計TWD798；Upper Riccarton二姑家住宿補貼改為已支出NZD100 × 18.2275 = TWD1,822.75，加TWD3,800後以TWD5,623列示。佳蓉MAS自有車全險NZD552.08已含1.75%刷卡附加費，仍為待支出，依08/01匯率估為TWD10,485。財務更新為已支出TWD289,710、待支出TWD15,857、總預估TWD305,567。
- 2026-08-04 Mastercard Global轉換器仍顯示錯誤；SG Rates四幣別頁面於2026-08-04 12:01同步產生MasterCard 08/03牌告，交叉匯率更新為NZD/TWD19.1668709、MYR/TWD7.9670235、USD/TWD32.4257820。僅重算仍屬估算的已付款與待支出項目，實刷及授權TWD金額保持不變；財務更新為已支出TWD289,778、待支出TWD16,258、總預估TWD306,036。
- 2026-08-05 依中信08/01未出帳截圖去重後新增六筆有效交易：餐飲／食品TWD2,307、Z Curletts加油與Motu Move交通TWD687，五筆實際海外手續費TWD44、Motu Move暫估TWD1。財務更新為已支出TWD292,817、待支出TWD14,276、總預估TWD307,093；餐飲預算已超出約TWD325。僅前兩張帳務截圖存入`private/billing/`，誤給的行動服務設定圖完全忽略且不得保存或公開。
- 2026-08-05 Mastercard Global轉換器仍顯示錯誤；SG Rates四幣別頁面於2026-08-05 08:00同步產生MasterCard 08/04牌告，交叉匯率更新為NZD/TWD19.0709043、MYR/TWD7.9167730、USD/TWD32.3400184。保留同日最新核帳，只重算仍屬估算的已付款與待支出項目；財務更新為已支出TWD292,779、待支出TWD14,205、總預估TWD306,984，餐飲預算超出約TWD474。
- 2026-08-05 使用者確認08/01中信PAK'nSAVE Hornby TWD746與Woolworths TWD975均歸「購物」，共TWD1,721由餐飲／食品移列購物。已支出維持TWD292,779；餐飲剩餘預算恢復為約NZD65.40 → TWD1,247，待支出更新為TWD15,452、總預估TWD308,231。
- 2026-08-06 Mastercard Global轉換器仍顯示錯誤；SG Rates四幣別頁面於2026-08-06 08:00同步產生MasterCard 08/05牌告，交叉匯率更新為NZD/TWD19.0419364、MYR/TWD7.8993929、USD/TWD32.2690166。保留最新購物分類，只重算仍屬估算的已付款與待支出項目；財務更新為已支出TWD292,769、待支出TWD15,384、總預估TWD308,153。
- 2026-08-06 最新中信與永豐08月帳單核對：中信TWD5,092及永豐台幣帳戶TWD23,395均為既有消費正式入帳，不重複增加；永豐幣倍日圓帳戶本期淨消費與手續費¥102,670、前期餘額¥168、應繳¥102,838。日圓依永豐08/06 15:30即期賣出0.2062換算；Agoda與舊Booking.com住宿正負沖銷排除，07/18 Kmart按退款後淨額，並補入先前漏列的Mobil Yaldhurst。財務更新為已支出TWD295,226、待支出TWD15,277、總預估TWD310,503。
- 2026-08-06 聯邦07月與08月帳單核對只採聯邦M卡的旅館／訂房平台交易，聯邦綠卡一卡通御璽卡及M卡其他消費、回饋全部排除。兩期住宿本金正式合計TWD9,704、海外交易手續費TWD145；以正式帳單取代6筆授權／估值後，財務更新為已支出TWD295,155、待支出TWD15,277、總預估TWD310,432。帳單PDF與擷取文字只存放`private/billing/`，不得提交或公開卡片資訊。
- 2026-08-07 Mastercard Global轉換器仍未回傳可用結果；SG Rates的NZD/USD/TWD三頁MasterCard牌告日一致為08/06，交叉匯率更新為NZD/TWD19.0390257、USD/TWD32.2859606。永豐牌告於08/07 08:01查詢時，JPY即期賣出仍為08/06 15:30的0.2062。停止維護MYR每日匯率，只重算仍屬估算的NZD項目；財務更新為已支出TWD295,155、待支出TWD15,271、總預估TWD310,426。
- 2026-08-07 玉山07月帳單無密碼，可直接解析；19筆旅行消費本金正式合計TWD7,671、海外交易手續費TWD106、應繳TWD7,777。所有本金均已由未出帳截圖納入，只以正式金額取代估值；NPD Timaru由TWD1,517改為TWD1,528，未出現在本期帳單的07/30與07/31交易保留暫列。財務更新為已支出TWD295,156、待支出TWD15,261、總預估TWD310,417；帳單與擷取文字只存`private/billing/`，不得提交或公開卡片資料。
- 2026-08-07 財務總控表完成資訊重整：待付款、待交付及可用預算提前呈現，已支出改為精簡分類摘要，6份信用卡帳單與聯邦、玉山、永豐日圓逐筆明細收進可展開核對區。金額與分類總額不變，手機保留三欄總額，A4列印強制展開詳細帳務。
- 2026-08-07 移除財務總控表內重複的聯邦M卡與永豐日圓住宿逐筆明細：聯邦07月、08月只保留帳單合計；永豐日圓保留住宿5筆小計並把個別旅館交由住宿總表記錄。Te Anau Lakeview、Hunters Moon、Empire Hotel與The Fort已更新正式帳單本金、手續費及已入帳狀態，財務總額不變。
- 2026-08-08 Mastercard Global未回傳可用結果；SG Rates的NZD/USD/TWD三頁以08/08同日資料交叉換算為NZD/TWD19.0325334、USD/TWD32.2148661。永豐JPY即期賣出更新為08/07 15:30的0.2060。保留正式TWD與歷史MYR原幣，只重算NZD估值及永豐日圓帳單TWD估算；財務更新為已支出TWD295,137、待支出TWD15,248、總預估TWD310,385。
- 2026-08-11 Mastercard Global直連仍回403；SG Rates的NZD/USD/TWD三頁MasterCard牌告日一致為08/10，交叉匯率更新為NZD/TWD19.0331841、USD/TWD32.2159667。永豐JPY即期賣出更新為08/10 15:30的0.2051。未查詢MYR，只重算NZD待支出與永豐日圓帳單估值；財務更新為已支出TWD295,044、待支出TWD15,261、總預估TWD310,305。
- 2026-08-12 Mastercard Global直連仍回403；SG Rates最新頁面的NZD牌告日為08/11，但USD與TWD仍為08/10，因日期不一致未交叉換算，NZD/USD沿用前次已驗證值。永豐JPY即期賣出更新為08/11 15:30的0.2045。未查詢MYR，只重算永豐日圓帳單估值；Kingston已有正式TWD實刷值不覆寫。財務更新為已支出TWD294,989、待支出TWD15,266、總預估TWD310,255。
- 2026-08-12 Gmail確認MAS已收到佳蓉自有車全險付款並寄出收據；原幣NZD552.08已含1.75%刷卡附加費，依使用者提供的信用卡即時未出帳值採TWD10,500。此筆由待支出移入「通訊／保險／簽證」已支出，不另加手續費；財務更新為已支出TWD305,489、待支出TWD4,758、總預估TWD310,247。公開手冊不放保單號、收據號或卡片資訊。
- 2026-08-12 使用者確認已離開紐西蘭，財務總控表改為結案模式；刪除未交付的佳蓉預備金，餐飲與油資未使用預算只留結案紀錄。另新增Skinny Mobile通訊費NZD9／實刷TWD171，實際支出總額更新為TWD305,660，不再列待支出或總預估。
- 2026-08-12 實際支出分類改為大類、子項及小計呈現；頁首與表尾另列扣除購車TWD77,921及佳蓉MAS車險TWD10,500後的旅行淨支出TWD217,239，完整實際支出仍保留TWD305,660。
- 2026-08-12 Gmail與本機正式保險證明核對通訊／保險／簽證細項：OrbitProtect律德NZD211、佳蓉NZD665；台灣產物旅平險律德TWD1,877、佳蓉TWD811；Mighty Mobile兩張發票各NZD262.15且均標示已付款，第二組門號後續售出；NZeTA／IVL合計NZD117。WHV、國際駕照等僅有核發或啟用信，個別TWD無法由原TWD34,708合併核帳值可靠拆出，不可虛構拆價。購物商家群組與退款狀態已恢復，總額維持TWD14,300。
- 2026-08-13 Mastercard Global直連仍回403；SG Rates的NZD、USD、TWD三頁MasterCard牌告日一致為08/12，交叉匯率更新為NZD/TWD18.9592740、USD/TWD32.1998633。永豐JPY即期賣出更新為08/12 15:30的0.2041。未查詢MYR，只重算日圓帳單估值與結案預算換算；正式TWD不覆寫。財務更新為實際支出TWD305,623、旅行淨支出TWD217,202。
- 工作樹可能出現 `.DS_Store` 或 Mac 的隱藏檔；不要納入提交，除非使用者明確要求。

## 已知注意事項

- Mastercard 官方頁面可被瀏覽器開啟；本機 `curl` 或直接 API 請求可能被 Mastercard/Akamai 擋下。必要時使用瀏覽器同源查詢。
- 每日匯率更新以 Mastercard Global 國際版 converter 為官方入口：`https://www.mastercard.com/global/en/personal/get-support/currency-exchange-rate-converter.html`。
- Mastercard current rate 查詢可使用頁面同源請求的 `fxDate=0000-00-00`，應以官方回應中的 `data.fxDate` 作為手冊匯率基準日期。
- 若官方 Mastercard 頁面可開但本機直接 API/JS 仍被 Akamai 或瀏覽器擴充阻擋，可用 SG Rates 的 MasterCard 同日 NZD/USD/TWD 對 SGD 匯率交叉驗證，使用前必須確認三個幣別的 MasterCard 日期一致。
- JPY每日匯率使用永豐銀行日圓即期賣出；非營業時間沿用牌告頁顯示的最新報價時間與數值，不用查詢MYR每日匯率。
- 匯率更新時要只在有實質匯率或換算變更時 commit。
- 已刷卡 TWD 實刷值應優先於估算匯率。
- 北島已完成段落不要加入公開敏感資訊，例如訂房 PIN、完整訂單號、信用卡尾號或私人聯絡資訊；必要時只保留住宿/平台/付款狀態與已刷金額。
- 若修改導航或地圖區塊，確認住宿多點路線與景點單點連結的分工沒有被破壞。
- 若出現未追蹤的 `assets/maps/*.svg`，先確認是否屬於本次需求，再決定是否提交。
- 車險條款與報價僅供本機評估時，放在 `private/insurance/`；此目錄由 `.gitignore` 排除，不得 stage、提交或公開引用其個人資料。
- 信用卡帳單與未出帳明細截圖僅供本機核帳時，放在 `private/billing/`；此目錄由 `.gitignore` 排除，不得 stage、提交或公開引用卡號、帳務或個人資料。
- YES Rentals與RentalCover的公開手冊只保留營運商、日期、車型、費用、付款狀態、保障分工與執行提醒，不放訂單號、保單參考號、私人地址或完整電話。
- Bookme景點改期在平台尚未書面確認前，票券表應標示「改期申請中」，不可把新日期寫成已確認，也不可公開訂單號碼。
- KKday「款項已確認」只代表付款完成；在收到訂單成立或電子憑證前，票券表應標示「待出票」，不可寫成已出票。

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
