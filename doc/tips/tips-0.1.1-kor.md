설치
----

![1.png](tip-images/1.png)

이거 말고

![2.png](tip-images/2.png)

https://github.com/KUR-creative/SickZil-Machine/releases \
여기서 다운로드하세요. \
밑에 쭉 내려보면 위에 짤처럼 assets가 있는데 거기서 받으시면 됨. 

gpu가 구리거나 AMD면 win64-cpu-kor.zip을 받으세요. \
<sub>암드가 안되서 꼬우시다고요...? 그건 제 탓이 아니라 텐서플로우 탓입니다. \
구글 사옥 앞에 가서 드러 누우셈</sub>




실행 
----

![3.png](tip-images/3.png)

SickZil-Machine-0.1.1-pre0-win64-gpu-eng.cmd 나 

![4.png](tip-images/4.png)


main 폴더의 SickZil-Machine-0.1.1-pre0-win64-gpu-eng.exe 파일을 더블클릭하여 실행합니다. 





만화 프로젝트 폴더 생성 
----

식질머신은 항상 "**만화 프로젝트 폴더**"를 열어서 작업을 수행합니다. \
만화 프로젝트 폴더는 다음과 같이 **images, masks, prev_images, prev_masks** 폴더 4개가 포함된 폴더입니다. 

![5.png](tip-images/5.png)


**images**에는 식질머신에서 편집하는 이미지가 모두 저장됩니다. \
작업이 끝난 뒤 images 폴더의 이미지에 글자를 넣으시면 됩니다. 

**masks**에는 생성한 마스크들이 저장됩니다. **이 마스크를 외부 프로그램으로 편집**할 수 있습니다! \
마스크를 외부에서 편집하고 만화 프로젝트 폴더를 새로 열거나 다른 이미지를 보고 돌아오면 편집한 마스크가 로드됩니다.

**prev_images**에는 **원본 이미지**가 저장됩니다. 식질머신은 이 이미지를 편집하지 않습니다. \
이미지 복원(툴바에서 가장 오른쪽 툴) 시에 사용되며, 이후 텍스트를 넣을 때 포토샵 등에서 편리하게 쓸 수 있습니다. 

prev_masks는 아직 별 기능이 없으며 항상 비어있습니다.


만일 만화 프로젝트 폴더가 아닌 폴더를 연다면 \
폴더에 이미지가 하나라도 있는 경우(이를 "단순 이미지 폴더"라고 합니다) \
**새로운 만화 프로젝트 폴더**를 생성합니다.



[열기] - [만화 프로젝트 폴더 열기]를 누르면

![6.png](tip-images/6.png)


위에서 choose를 누르면 만화 프로젝트 폴더를 만들지 물어봅니다.

그러면

![7.png](tip-images/7.png)


 

기존 폴더의 이름 뒤에 \_mproj가 붙은 이름이 기본적으로 주어집니다. \
Save를 누르면 폴더가 생성되고 

![8.png](tip-images/8.png)



이미지가 복사됩니다. 

![9.png](tip-images/9.png)



아직 masks는 비어있습니다. 마스크를 생성하면 masks에 마스크가 저장되며, 외부 프로그램으로 편집할 수 있습니다.



이후 생성한 만화 프로젝트 폴더를 다시 선택하여 로드할 수 있습니다.


![10.png](tip-images/10.png)


 

외부 툴로 이미지, 마스크 편집하기 
----

이게 사실 개꿀팁인 부분인디 \
솔직히 지금 구이는 확대도 안되고 페인트 툴도 없어서 허접합니다. \
그래서 제가 프로젝트를 폴더로 만들었습니다. 외부 툴 쓰시라구요. 


1) 식질머신에서 만화 프로젝트 폴더를 만듭니다. 
2) 마스크 일괄 생성 버튼(GenMaskAll: 왼쪽에서 첫번째 버튼)을 누릅니다. 
3) 모두 생성되었으면 식질머신을 종료합니다. 
4) 포토샵 같은 프로그램으로 *모든 마스크를 적절히 편집*합니다. 
5) 다시 식질머신을 켜고 편집한 만화 프로젝트 폴더를 엽니다. 
6) 텍스트 일괄 삭제 버튼(rmTxtAll: 왼쪽에서 두번째 버튼)을 누르면 됩니다. 

만화 이미지가 너무 클 경우 줌 인/아웃이 안되는 현재 gui는 굉장히 불편할 수 있습니다. \
위 방식은 기본적으로 제공하는 툴로는 힘들 때 사용하시기 바랍니다.



데이터셋 기여 
----

사실 4.의 쇼를 벌이는 건 다 정확도가 떨어져서 그렇습니다. \
데이터를 제공해 주시면 더 많고 다양한 이미지로 학습이 가능합니다. 

![11.png](tip-images/11.png)


식질머신에 필요한 데이터는 3(+1)가지입니다. 
1) 원본 만화 이미지(**원본**) 
2) 원본 만화 이미지의 텍스트와 효과음을 정확하게 덮는 마스크(**텍스트 컴포넌트 마스크**) 
3) 텍스트와 효과음이 지워진 만화 이미지(**출력**) <sub>(주의 - 번역된 텍스트를 입력한 이미지가 아닙니다) </sub> 
4) 번역을 완료하여 한글이 적절히 채워진 만화 이미지(위 그림에는 없음)

이 이미지들은 식질머신을 이용하면 쉽게 생성할 수 있습니다. \
(물론 식질머신을 쓰지 않아도 위 형식만 맞으면 학습에 이용할 수 있습니다.) \
제공된 데이터는 오직 연구용도로만 활용할 것이며, 주기적으로 학습하여 성능을 향상시킬 예정입니다. \
(현재 SegNet은 약 300장, ComplNet은 3만장 정도의 이미지로 학습했습니다. 아직 부족합니다.)

<a href="mailto:kur.creative.org@gmail.com"> kur.creative.org@gmail.com </a>

위 메일로 데이터를 보내주시면 감사하겠습니다.



그 외 기타 꿀팁 
----
- 위/아래 방향키로 이미지를 넘길 수 있습니다. 
- 마우스 휠을 클릭하여 드래그하면 이미지를 이동시킬 수 있습니다. 
- 가장 오른쪽의 되돌리기 버튼(RvertImage)은 오직 하나의 이미지만을 되돌립니다. 
   만일 모든 이미지를 되돌리고 싶으시다면 prev_images에서 이미지를 복사한 후 images에 덮어씌우세요. 
- 이미지가 너무 커서 마스크 편집이 힘들다면 역시 외부 프로그램을 사용하시면 됩니다.





마지막으로.. 
----
프로그램에 매뉴얼 같은 게 없어서 다들 약간 헤메시는 거 같습니다. \
위 내용들 포함해서 유튜브에 튜토리얼을 올릴 예정입니다.

그리고 식질머신으로 편집한 저작물에는 \
다음 워터마크와 

![12.png](tip-images/12.png)

깃헙 레포지토리 주소를 

https://github.com/KUR-creative/SickZil-Machine

넣어주셨으면 합니다. 홍보용이에요. (워터마크는 축소시켜서 넣으면 되요)

근데 저 워터마크가 촌스럽다는 분이 계시더군요.  


![13.png](tip-images/13.png)
 

ㅇㅈ합니다. 

더 예쁘고 직관적인 아이콘을 그려서 제게 메일(<a href="mailto:kur.creative.org@gmail.com"> kur.creative.org@gmail.com </a>)로 보내시거나 \
[깃헙 이슈](https://github.com/KUR-creative/SickZil-Machine/issues)에 올려주시면 반영해드리겠습니다. \
만약에 후보가 많으면 뭐 나중에 투표 같은 거 하면 될 듯?


긴 글 읽어주셔서 감사합니다.
