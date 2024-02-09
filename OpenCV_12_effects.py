import cv2
import numpy as np
import time

# 設定視訊捕捉物件，讀取影片檔案 (請放入你的影片路徑)
cap = cv2.VideoCapture('car.mp4')

# 檢查影片是否成功打開
if not cap.isOpened():
    print("錯誤：無法開啟影片。")
    exit()

# 新的影片大小
new_width = 1280  # 新的寬度
new_height = 720  # 新的高度

# 定義切換特效的時間間隔（秒）
effect_duration = 10  # 每個特效顯示 10 秒

# 目前特效的編號和上一次切換特效的時間
current_effect = 0
last_effect_time = time.time()

# 定義使用 XVID 編碼器的 VideoWriter 物件
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output.avi', fourcc, 20.0, (new_width, new_height))

while True:
    # 讀取影片
    ret, frame = cap.read()

    # 若未讀取到影格，表示影片結束
    if not ret:
        print("影片結束。")
        break

    # 調整原始影格大小
    original = cv2.resize(frame, (new_width, new_height))

    # 檢查是否需要切換特效
    elapsed_time = time.time() - last_effect_time
    if elapsed_time >= effect_duration:
        current_effect = (current_effect + 1) % 12  # 總特效數量為12
        last_effect_time = time.time()

    # 根據 current_effect 應用相應的效果  (共有12個特效,依照需求請自行調整)
    effect_text = ""
    if current_effect == 1:
        # 將顏色空間從 BGR 轉換為 HSV
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        effect_text = "Effect: BGR2HSV"
    elif current_effect == 2:
        # 應用灰度效果
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        effect_text = "Effect: Grayscale"
    elif current_effect == 3:
        # 應用棕褐色調效果（Sepia Tone）
        sepia_matrix = np.array([[0.393, 0.769, 0.189],
                                [0.349, 0.686, 0.168],
                                [0.272, 0.534, 0.131]])
        frame = cv2.transform(frame, sepia_matrix)
        frame = np.clip(frame, 0, 255).astype(np.uint8)
        effect_text = "Effect: Sepia Tone"
    elif current_effect == 4:
        # 將顏色空間從 BGR 轉換為灰度，然後再轉換回 BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        effect_text = "Effect: Convert to Gray"
    elif current_effect == 5:
        # 水平翻轉圖像
        frame = cv2.flip(frame, 1)
        effect_text = "Effect: Horizontal Flip"
    elif current_effect == 6:
        # 拉普拉斯邊緣檢測
        laplacian = cv2.Laplacian(frame, cv2.CV_64F).astype(np.uint8)
        frame = laplacian
        effect_text = "Effect: Laplacian"
    elif current_effect == 7:
        # 旋轉圖像 45 度
        rows, cols, _ = frame.shape
        rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
        frame = cv2.warpAffine(frame, rotation_matrix, (cols, rows))
        effect_text = "Effect: Rotation"
    elif current_effect == 8:
        # 使用 MOG2 進行背景減除
        mog2 = cv2.createBackgroundSubtractorMOG2()
        fg_mask = mog2.apply(frame)
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_with_contours = frame.copy()
        frame = cv2.drawContours(frame_with_contours, contours, -1, (0, 255, 0), 2)
        effect_text = "Effect: Background Subtraction"
    elif current_effect == 9:
       # 模糊效果
        frame = cv2.blur(frame, (5, 5))
        effect_text = "Effect: Blur"
    elif current_effect == 10:
        # 高斯模糊效果
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        effect_text = "Effect: Gaussian Blur"
    elif current_effect == 11:
       # 添加噪點效果
        noise = np.random.normal(0, 20, frame.shape)
        frame = frame + noise
        frame = np.clip(frame, 0, 255).astype(np.uint8)
        effect_text = "Effect: Add Noise"
    elif current_effect == 12:
        # 調整圖像大小
        frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
        frame = cv2.resize(frame, (new_width, new_height))
        effect_text = "Effect: Resize"

    # 在左上角添加顯示當前效果的文本
    cv2.putText(frame, effect_text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # 通過水平串聯原始和處理後的幀來創建 split_frame
    split_frame = np.hstack((original, frame))

    # 調整 split_frame 的大小為所需的分辨率
    split_frame = cv2.resize(split_frame, (new_width, new_height))

    # 寫入幀至輸出視頻
    output_video.write(split_frame)

    # 顯示原始和處理後的幀
    cv2.imshow('Merged View', split_frame)

    # 按 ESC 鍵退出
    if cv2.waitKey(30) & 0xFF == 27:
        break
# Release resources
cap.release()
output_video.release()
cv2.destroyAllWindows()
