1. 載入model所需檔案：wiki-zh-model, wiki-zh-model.wv.syn0.npy
2. sever：server.py, client(python)：client.py / client(js)：client.js
3. test command：python3 validate_accuracy
forever start -c python3 server.py[port: 12345]
[因為有相對路徑與執行問題，因此許多不合裡路徑名稱存在]
