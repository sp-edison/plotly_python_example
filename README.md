# Plotly python example

python을 활용하여 입력 데이터를 Plotly json 형태로 변환해주는 예제 입니다. 폴더별로 ply로 변환해주는 python 코드와 octave 실행 코드 그리고 입력 파일이 있습니다.



각 예제별 설명

 1_line_plot : dat 파일을 읽어 line plot을 출력	

 실행 명령어 :  ```python convert.py -i Freq_S11Abs.dat ```
 결과 result 폴더에 Freq_S11Abs.ply 생성

 2_line_plot_holdon : dat 파일을 일거 2개의 line plot을 동시에 출력


 실행 명령어 :  ```python convert.py -i Time_Voltage_Current.dat ```
 결과 result 폴더에 Time_Voltage_Current.ply 생성

 3_iamge_2D :  dat 파일을 읽어 2D contour plot을 출력

 실행 명령어 :  ```python convert.py -i Hy5500.dat ```
 결과 result 폴더에 Hy5500.ply 생성


