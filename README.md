# VocabFlash 📚

背英文單字的 PWA App，類似 Quizlet 的學習體驗。

## 功能

- 📚 **卡片模式** — 點擊翻面看中文，左右標記「認識/不熟」
- 🎯 **測驗模式** — 四選一選擇題，自動計分
- 📖 **單字本** — 搜尋、新增、編輯、刪除
- 📊 **統計** — 已熟悉/學習中/新單字數量
- 📥 **匯入** — 貼上「英文, 中文」批次匯入
- 📤 **匯出** — 一鍵下載所有單字
- 🏷️ **分類** — 建立不同 deck 分類管理

## 使用方式

打開 https://ningisme.github.io/vocab-flash/

### 加到手機主畫面

- **iPhone Safari** → 分享按鈕 → 加入主畫面
- **Android Chrome** → 右上選單 → 加到主畫面

加好後像原生 App 一樣使用，離線也能開。

## 技術

- 純前端 PWA（HTML + CSS + JavaScript）
- Service Worker 離線快取
- localStorage 儲存單字資料
- 間隔複習演算法
- 深色 Notion 風格設計
- 部署在 GitHub Pages

## 資料說明

所有單字存在瀏覽器的 localStorage，不會上傳任何伺服器。  
換手機前請用「匯出」功能備份。
