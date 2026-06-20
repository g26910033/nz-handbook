# AGENTS.md

## Project

This repository hosts the public GitHub Pages site for the travel handbook:

* Site: http://gpt.greenparty.org.tw/nz-handbook/
* Main file: `index.html`
* Language: Traditional Chinese for Taiwan (`zh-Hant`)
* Purpose: New Zealand winter self-drive travel handbook, including finance, itinerary, tickets, lodging, maps, safety, and operational cards.

## Core rules

1. Treat `index.html` as the single source of truth.
2. Do not split the handbook into multiple pages unless the user explicitly requests it.
3. Do not convert the project into a framework, bundler, React/Vue app, or build pipeline.
4. Keep the site static HTML + inline CSS only.
5. Do not add external dependencies, npm packages, analytics scripts, trackers, or external CSS frameworks.
6. Do not add JavaScript unless the user explicitly asks for interactive behavior.
7. Prefer small, targeted edits over full rewrites.
8. Preserve mobile readability and A4 print readability.
9. Preserve Traditional Chinese wording. Use English only for foreign place names, hotels, attractions, maps, booking platforms, or card/product names where useful.
10. Never silently remove travel-critical information such as payment dates, booking deadlines, safety warnings, emergency contacts, lodging names, or map links.

## Git workflow

1. Work on the current branch unless the user asks for a branch or PR.
2. Before editing, inspect the relevant part of `index.html`.
3. After editing, run these checks:

   * `git diff -- index.html`
   * `grep -n "<title>" index.html`
   * `grep -n "導航總表" index.html`
   * `grep -n "景點票券" index.html`
4. Commit the change when complete.
5. Push the completed commit to the current branch unless the user explicitly asks not to push.
6. Final response must include:

   * short summary of changes
   * files changed
   * commit SHA
   * any unresolved concern

## Content conventions

### Finance

* Keep original currency and TWD conversion visible.
* Use the current exchange rates specified by the user.
* If exchange rates change, recalculate:

  * finance summary
  * ticket table
  * lodging/payment table
  * any related totals
* Do not remove original-currency amounts.
* Reject DCC wording should remain where payment guidance appears.

### Tickets and attractions

* Section title: `景點票券與執行時間`.
* Ticket table columns should be:

  * 日期／時間
  * 項目
  * 原幣/計算
  * TWD
  * 備註
* Do not use the word `保留` as a decision label unless the user specifically requests it.
* Use `備註` wording instead.
* Attractions and hot springs should be shown in Chinese + English, for example:

  * `Hanmer Springs Thermal Pools 漢默溫泉`
  * `Tekapo Springs Hot Pools 蒂卡波溫泉`
  * `Steampunk HQ 蒸汽龐克總部`
* If an attraction is cancelled, remove it from the ticket table unless the user asks to keep a cancellation record.

### Navigation

* Lodging navigation should use multi-point route links:

  * one route for North Island lodging nodes
  * one route for South Island lodging nodes
* Attraction, hot spring, aurora, and free-stop navigation should use individual single-point Google Maps links.
* In the single-point map table, do not repeat the same category on many rows. Group links by category:

  * 付費景點
  * 溫泉
  * 極光
  * 免費停點
* Lodging table may still include single-point map links, because that table is for payment and lodging execution.

### Lodging/payment table

Keep these fields visible:

* 日期
* 地點／住宿
* 地圖
* 金額
* 刷卡／執行
* 付款／取消死線

Do not remove payment deadlines, card names, booking platforms, or execution dates.

### Itinerary

* Keep morning / noon / afternoon / night logic when present.
* Do not create high-risk night-driving plans.
* Winter driving principles:

  * avoid mountain roads early morning
  * avoid rural/mountain driving after dark
  * check NZTA and MetService before alpine roads
  * delete scenic stops before sacrificing lodging arrival time

### Privacy and public-site caution

This site is public. Before adding personal data, warn if it includes:

* passport numbers
* policy numbers
* full phone numbers
* private home addresses
* medical details
* credit card details

If private addresses are already intentionally included, do not remove them unless instructed, but mention the public-site risk when relevant.

## Current project facts

* GitHub Pages URL: `http://gpt.greenparty.org.tw/nz-handbook/`
* Repo: `g26910033/nz-handbook`
* Main file: `index.html`
* Current trip style: winter self-drive, finance-controlled, low-risk driving, mostly self-catering.
* Current exchange rates from user:

  * 1 NZD = 18.2714699 TWD
  * 1 MYR = 7.7100491 TWD
  * 1 USD = 31.6883016 TWD
* Current finance summary:

  * 已支出：TWD 98,196
  * 待支出：TWD 162,391
  * 總預估：TWD 260,587

## Output style

* Respond in Taiwan Traditional Chinese.
* Be concise but complete.
* Do not paste huge HTML blocks in the final response.
* Mention exact commit SHA after updating.
* If unsure, inspect files first rather than guessing.
