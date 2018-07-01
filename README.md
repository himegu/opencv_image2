バイラテラルフィルタでフィルタリングするコードを以下に示す。




２値化を行うコードを以下に示す.


    import numpy as np
    import cv2

    def myfunc(i):    #画像の２値化を行う関数
        global dst
        ret, dst=cv2.threshold(frame_g, i, 255, cv2.THRESH_BINARY)  #入力画像を２値化する


    cv2.namedWindow('title')  #画像やトラックバーを配置するウィンドの名前

    cv2.createTrackbar('value',  'title',  0, 
                       255, 
                       myfunc)    #トラックバーの設定


    cap = cv2.VideoCapture(1) # VideoCapture オブジェクトを取得
    cap.set(3,1280)
    cap.set(4,800)
    cap.set(5,15) #取得した画像を表示するフレームの大きさを設定


    while(True):

        ret, frame = cap.read() #カメラから1コマのデータを取得
        if not ret: continue

        frame_g=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #取得画像をグレースケールに変換

        v = cv2.getTrackbarPos('value',  'title')  

        myfunc(v) #関数を呼び出して取得した画像を処理

        cv2.imshow('title', dst)  #OSのフレーム(ウィンドウ)に2地下を行った画像を表示

        k = cv2.waitKey(1)
        if k == ord('q') or k == 27:  #Escキーかqキーをタイプするとループを抜ける
            break



    cap.release() # キャプチャをリリース
    cv2.destroyAllWindows() #ウィンドウをすべて閉じる


<br>
cv2.threshold:引数は入力画像、しきい値、最大値、行う２値化の処理
cv2.createTrackbar:引数はトラックバーの名前、表示するウィンドの名前、最小値、最大値、スライダの位置が変更されるたびに呼び出される関数のポインタ
While文の中で関数myfuncを呼び出してcapture2_1.py同様取得した画像に対して処理を行うようにしている。
実際の様子:https://youtu.be/K485q5yFnG4 <br>
参考サイト:http://pynote.hatenablog.com/entry/opencv_how_to_binarize　、　http://opencv.jp/opencv-2.1/cpp/user_interface.html
