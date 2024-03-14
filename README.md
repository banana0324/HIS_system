# HIS_system
一套使用Flask開發的HIS系統，後端使用MS SQL資料庫

功能
提供CRUD範例，並搭配資料分析功能。
以MVC架構開發。
一般患者可以瀏覽、搜尋患者，並查看患者狀態。
後台管理者可以編輯患者資訊，並檢視每個患者資訊圖表。

# 實作方法
利用python  Flask方法，註冊時分為管理者及使用者兩種身分，其功能主要為新增、刪除、修改還有統計資料；可記錄患者醫療資料(新增)，並可修改內容(修改)。可儲存生命徵象(新增)，並提供刪除功能(刪除)。可查詢患者醫療及生命徵象資料(查詢)。可瀏覽患者資料概況(統計)。

語言：python、HTML、css
資料庫：SQL SERVER

登入頁示意圖
![image](https://github.com/banana0324/HIS_system/assets/14922129/c5382a18-a8a6-4ae4-912b-2581f8f2ce61)



前台介面-患者清單，查看患者清單，上方搜尋欄位可模糊查詢患者資訊
![image](https://github.com/banana0324/HIS_system/assets/14922129/7302883d-cfbd-4288-a70a-dd06ce111f39)

前台介面-患者詳細資訊，查看患者資訊可了解患者所有資訊
![image](https://github.com/banana0324/HIS_system/assets/14922129/852cb03a-437c-414d-874a-189050a4fd24)

後台管理-患者資料總覽，可編輯或是刪除做更一步的資料更動
![image](https://github.com/banana0324/HIS_system/assets/14922129/892f5e4f-9327-4153-9a84-fb83116ffe4e)

後台管理-修改患者資料，修改患者個人資訊

![image](https://github.com/banana0324/HIS_system/assets/14922129/023f7a52-c1bd-4d4e-a7e1-b241fce7914e)

後台管理-新增患者資訊，新增患者資訊

![image](https://github.com/banana0324/HIS_system/assets/14922129/671ad92a-4f19-4d26-b593-72b8b7ca2ba0)

後台管理-刪除提示，避免誤刪資料

![image](https://github.com/banana0324/HIS_system/assets/14922129/e0a6e522-f525-421c-9fcc-e95563562bd9)

後台介面-統計到院後狀態查詢患者到院後之狀態（出院/住院/死亡）並以圖形化界面展示
![image](https://github.com/banana0324/HIS_system/assets/14922129/e12647ab-50e7-413e-935a-937e98ce30d8)

後台介面-查詢所有患者之男女比例並以圖形化界面展示
![image](https://github.com/banana0324/HIS_system/assets/14922129/5e3f3e2b-1f21-4cbf-bae7-07b8df87b159)



