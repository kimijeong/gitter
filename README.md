// 집중 타이머 (Focus Timer)

1. 개발 목적

이 프로그램은 사용자가 특정 시간 동안 집중할 수 있도록 도와주는 타이머입니다.  
사용자가 학습이나 업무 중 집중을 유지하고, 시간 관리를 보다 체계적으로 할 수 있으며,  
시간 종료 시 즉각적인 경고음을 통해 작업 전환 시점을 인지할 수 있도록 개발하였습니다.

---

2. 주요 기능

- 사용자가 분(minute)과 초(second)를 직접 입력하여 타이머를 설정할 수 있습니다.
- 남은 시간은 GUI 화면에 실시간으로 표시됩니다.
- 타이머가 종료되면 시스템 기본 사운드를 빠른 간격으로 반복 재생하여 종료를 알립니다.
- 알람은 별도의 스레드에서 실행되며, 사용자가 '정지' 버튼을 누르면 즉시 알람이 중단됩니다.
- GUI는 `tkinter`, 알람은 `winsound`를 사용하였으며, 두 기능은 `threading`을 통해 동시에 작동합니다.

---

3. 입출력 형태

입력  
- 프로그램 실행 후, 사용자로부터 분(minute)과 초(second)를 입력받습니다.

출력  
- 타이머 동작 중: GUI 상단에 남은 시간이 "MM:SS" 형식으로 실시간 표시됩니다.  
- 타이머 종료 시: 화면에 종료 메시지가 출력되며, 시스템 사운드가 반복 재생됩니다.  
- 알람 정지 시: 알람이 즉시 멈추고 종료 메시지가 표시됩니다.

---

4. 실행 방법 및 환경 설정

실행 환경  
- 운영체제: Windows (winsound 모듈 사용)  
- Python 3.6 이상 필요

실행 방법  
1. 본 저장소를 클론하거나 zip 파일로 다운로드합니다.  
2. Python이 설치된 환경에서 다음 명령어를 실행합니다:

   ```bash
   python timer.py
