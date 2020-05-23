import base64
import io
import face_recognition
import cv2
import numpy as np

from django.conf import settings

def detect(upload_image):
    result_name = upload_image.name
    result_list = []
    result_img = ''
    image1 = face_recognition.load_image_file('static/image/Leonardo.jpg')  # 正解
    image2 = face_recognition.load_image_file(upload_image)  # Upload_image入力

    encoding1 = face_recognition.face_encodings(image1)[0]
    encoding2 = face_recognition.face_encodings(image2)[0]

    face_locations = []
    # 顔の位置情報を検索
    face_locations = face_recognition.face_locations(image2)

    # for face_encoding in face_encodings:
    # 顔画像が登録画像と一致するか検証
    matches = face_recognition.compare_faces([encoding1], encoding2, tolerance = 0.6)
    if matches[0]==True:
        name = 'Leonard DiCaprio'
    else:
        name = 'NOT Leonard DiCaprio'

    # 顔の位置情報を表示
    for (top, right, bottom, left) in face_locations:
        # 顔領域の枠
        cv2.rectangle(image2, (left, top), (right, bottom), (0,0,255), 4)

    # Commented out IPython magic to ensure Python compatibility.
    # import matplotlib.pyplot as plt
    # # %matplotlib inline
    # fig, ax = plt.subplots(figsize=(10,10))
    # plt.title(name, {'fontsize':20, 'color':'pink'})
    # plt.imshow(image2)

    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    cv2.imwrite('static/image/output.png', image2)
    result_name = name
    result_img = image2
    result_list.append(name)
    return (result_list, result_name, result_img)
    


    
#     # アップロードされた画像ファイルをメモリ上でOpenCVのimageに格納
#     image = np.asarray(Image.open(upload_image))
#     # 画像をOpenCVのBGRからRGB変換
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     # 画像をRGBからグレースケール変換
#     image_gs = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    
#     # OpenCVを利用して顔認識
#     face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1,
#                                          minNeighbors=5, minSize=(64, 64))

#     # 顔が１つ以上検出できた場合
#     if len(face_list) > 0:
#         count = 1
#         for (xpos, ypos, width, height) in face_list:
#             # 認識した顔の切り抜き
#             face_image = image_rgb[ypos:ypos+height, xpos:xpos+width]
#             # 切り抜いた顔が小さすぎたらスキップ
#             if face_image.shape[0] < 64 or face_image.shape[1] < 64:
#                 continue
#             # 認識した顔のサイズ縮小
#             face_image = cv2.resize(face_image, (64, 64))
#             # 認識した顔のまわりを赤枠で囲む
#             cv2.rectangle(image_rgb, (xpos, ypos),
#                           (xpos+width, ypos+height), (0, 0, 255), thickness=2)
#             # 認識した顔を1枚の画像を含む配列に変換
#             face_image = np.expand_dims(face_image, axis=0)
#             # 認識した顔から名前を特定
#             name, result = detect_who(model, face_image)
#             # 認識した顔に名前を描画
#             cv2.putText(image_rgb, f"{count}. {name}", (xpos, ypos+height+20),
#                         cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
#             # 結果をリストに格納
#             result_list.append(result)
#             count = count + 1

#     # 画像をPNGに変換
#     is_success, img_buffer = cv2.imencode(".png", image_rgb)
#     if is_success:
#         # 画像をインメモリのバイナリストリームに流し込む
#         io_buffer = io.BytesIO(img_buffer)
#         # インメモリのバイナリストリームからBASE64エンコードに変換
#         result_img = base64.b64encode(io_buffer.getvalue()).decode().replace("'", "")

#     # tensorflowのバックエンドセッションをクリア
#     backend.clear_session()
#     # 結果を返却
#     return (result_list, result_name, result_img)

# def detect_who(model, face_image):
#     # 予測
#     predicted = model.predict(face_image)
#     # 結果
#     name = ""
#     result = f"本田 翼 の可能性:{predicted[0][0]*100:.3f}% / 佐倉 綾音 の可能性:{predicted[0][1]*100:.3f}%"
#     name_number_label = np.argmax(predicted)
#     if name_number_label == 0:
#         name = "Honda Tsubasa"
#     elif name_number_label == 1:
#         name = "Sakura Ayane"
#     return (name, result)