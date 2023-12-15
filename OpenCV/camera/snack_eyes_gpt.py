import cv2

# 비디오 파일 경로 또는 카메라 인덱스
cap = cv2.VideoCapture(0)  # 비디오 파일 경로 또는 카메라 인덱스를 설정

# 움직임 감지를 위한 ROI (Region of Interest) 좌표 설정
roi_x, roi_y, roi_width, roi_height = 100, 100, 200, 200

# ROI 영역 설정
roi = None

# 이전 프레임을 저장하기 위한 변수
previous_frame = None

while True:
    # 현재 프레임 읽어오기
    ret, frame = cap.read()

    # 프레임이 제대로 읽어왔는지 확인
    if not ret:
        break

    # ROI 설정
    roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

    # 현재 프레임을 흑백으로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ROI의 흑백 영상 추출
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # 원본 영상에서 ROI 영역 표시
    cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

    # 이전 프레임이 있으면 움직임 감지
    if previous_frame is not None:
        # 현재 프레임과 이전 프레임의 차이 계산
        frame_diff = cv2.absdiff(previous_frame, roi_gray)

        # 차이 이미지에서 움직임이 있는 부분을 찾기 위한 임계값 설정
        _, threshold_diff = cv2.threshold(frame_diff, 100, 255, cv2.THRESH_BINARY)

        # 움직임이 있는지 확인
        contours, _ = cv2.findContours(threshold_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 움직임이 감지된 경우
        if contours:
            # ROI 박스 색깔 변경 (빨간색)
            cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 0, 255), 2)

            # 화면에 움직임 감지 텍스트 표시
            cv2.putText(frame, "Motion Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # 전체 화면을 파일로 저장
            cv2.imwrite("captured_frame.jpg", frame)

    # 현재 프레임을 이전 프레임으로 저장
    previous_frame = roi_gray.copy()

    # 화면에 영상 출력
    cv2.imshow("Motion Detection", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 사용한 자원 해제
cap.release()
cv2.destroyAllWindows()
