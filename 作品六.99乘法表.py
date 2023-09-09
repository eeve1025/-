
for a in range(1, 10):               # 讓 a 從 1 執行到 9
    for b in range(1, 10):             # 讓 b 從 1 執行到 9
        print(f'{a}x{b}={a*b}',end=' ')      # 使用格式化字串，印出產生對應的字串，最後加上 end=' '表示不換行
    print('')    # 內層迴圈執行結束後，執行 print('') 會換行顯示