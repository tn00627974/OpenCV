OpenCV_12_effects 

Video Processing with OpenCV
This repository contains a Python script for processing videos using OpenCV. The script reads a video file, applies various effects to the frames, and saves the result to a new video file.此存儲庫包含一個用於使用 OpenCV 處理視頻的 Python 腳本。該腳本讀取視頻檔，將各種效果應用於幀，並將結果保存到新的視頻檔中。

Prerequisites
Make sure you have the following installed:請確保已安裝以下軟體：

-----------------------------

version :  (pip install list)

Python 3.8.10
OpenCV: 4.9.0.80
NumPy: 1.20.3

or
pip install -r requirements.txt

-----------------------------

Usage
Clone the repository:

使用方式如下 : 

#請將影片檔案放在與程式碼同一層 ('xxx.mp4')可自行修改名稱 
cap = cv2.VideoCapture('xxx.mp4')

#請更改你要修改的影片路徑 (xxxxx.avi) 可自行修改名稱 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('xxxxx.avi', fourcc, 20.0, (new_width, new_height))


bash
Copy code
git clone https://github.com/tn00627974/OpenCV.git
cd your-repository
Run the script:

bash
Copy code
python video_processing.py
This will execute the Python script that reads the car.mp4 video, applies various effects to the frames, and saves the result to a new video file named output.mp4.這將執行 Python 腳本，該腳本讀取視頻，將各種效果應用於幀，並將結果保存到名為 output.mp4 的新 car.mp4 視頻檔中。

Check the output:檢查輸出：

Once the script has finished running, you can find the processed video in the same directory with the name output.mp4.文稿運行完畢后，您可以在名為 output.mp4 .

Feel free to customize the script or experiment with different video files and effects!隨意自定義腳本或嘗試不同的視頻檔和效果！



特效列表特效清單
以下是應用程序支持的特效列表：

BGR2HSV: 將顏色空間從 BGR 轉換為 HSV。
Grayscale: 應用灰度效果。
Sepia Tone: 應用棕褐色調效果。
Convert to Gray: 將顏色空間從 BGR 轉換為灰度，然後再轉換回 BGR。
Horizontal Flip: 水平翻轉圖像。
Laplacian: 拉普拉斯邊緣檢測。
Rotation: 旋轉圖像 45 度。
Background Subtraction: 使用 MOG2 進行背景減除。
Blur: 模糊效果。Blur： 模糊效果。
Gaussian Blur: 高斯模糊效果。Gaussian Blur： 高斯模糊效果。
Add Noise: 添加噪點效果。
Resize: 調整圖像大小。
注意事項
請確保已安裝相應的套件。
您可以自行修改程式碼以添加新的特效或進行自定義更改。
授權
此程式以 MIT 授權提供。

貢獻
如果您有任何建議或改進意見，請隨時提交 [issue](<存儲庫的 URL>/issues) 或發起合併請求。

作者 : tn00627974
[點擊觀看我的YouTube視頻](https://www.youtube.com/watch?v=QS6JC6bzwAY)
![image](https://github.com/tn00627974/OpenCV/assets/139155210/aaa93c63-4aab-41f8-8a7a-e10c0e39fbc1)

