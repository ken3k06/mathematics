<img width="959" height="668" alt="image" src="https://github.com/user-attachments/assets/e696d788-da3f-41c5-9107-c2acdadd74ff" />

## Tóm tắt
Một dãy $S=\lbrace s_i \rbrace$ được gọi là dãy $n$ nếu như mỗi phần tử trong dãy thỏa mãn $1 \leq s_i \leq n$ và có đúng $n$ phần tử. Như vậy sẽ có tổng cộng $n^n$ dãy $n$ khác nhau. 

Vì mỗi phần tử có $n$ cách chọn.

Với mỗi dãy $S$ như vậy, ta kí hiệu $L(S)$ là độ dài của dãy con của $S$ sao cho mọi phần tử đều bằng nhau. Ví dụ $S=\lbrace 1,5,5,10,7,7,7,2,3,7 \rbrace$ có một dãy con $\lbrace 7,7,7 \rbrace$ có độ dài là 3. Vậy $L(S)=3$.


Đặt $f(n) = \sum L(S)$ trên mọi dãy $S$ là dãy $n$. 

Cho trước $f(3)=45,f(7)=1403689$ và $f(11)=481496895121$. Tính $f(7500000) \bmod 1000000009$


## Phân tích

Trước tiên thử tính lại $f(3),f(7),f(11)$ coi sao. 

