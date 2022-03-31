program Umfa(input, output);
const
Last = 4; { 전체 학생수 }
type
Index = 1..Last;
std = record { 학생 개인 정보 : 학번, 이름, 과목점수, 총점 }
number : string;
nickname : string;
korea, math, english, total : integer;
end;
var
count : integer;
student : array[Index] of std;
procedure Exchange(var X, Y: integer);
var
Temp : integer;
TempStd : std;
begin { Exchange }
{ 학생 개인정보 교환 }
TempStd := student[X];
student[X] := student[Y];
student[Y] := TempStd;
{ X값 Y값 교환 }
Temp := X;
X := Y;
Y := Temp;
end; { Exchange }
procedure Partition(Low, High: integer; var SplitIndex: integer);
var
SplitV, Up, Down: integer; { 기준점에서 위 아래로 구분 }
begin { Partition }
SplitV := student[Low].total; { 처음값을 기준점으로 }
Up := Low;
Down := High;
repeat
While (student[Up].total <= SplitV) and (Up < High) do { 배열 처음
부터 비교 }
Up := Up + 1;
While (student[Down].total > SplitV) and (Down > Low) do { 배열
마지막부터 비교 }
Down := Down - 1;
If Up < Down then { 기준점까지 오지 않았으면 Up, Down 교환 }
Exchange(Up, Down)
until Up >= Down;
SplitIndex := Down;
Exchange(Low, Down);
end; { Partition }
procedure Quicksort(Low, High : integer);
var
SplitIndex: integer;
begin { Quicksort }
If Low < High Then
begin
Partition(Low, High, SplitIndex); { 파티션을 나눈후 }
Quicksort(Low, SplitIndex-1); { 왼쪽부터 정렬 }
Quicksort(SplitIndex+1, High); { 오른쪽부터 정렬 }
end;
end; { Quicksort }
procedure input; { 자료를 입력받는 부분 }
begin { input }
count := 0;
repeat
count := count + 1;
Write('Input Number : ');
Readln(student[count].number);
Write('Input Name : ');
Readln(student[count].nickname);
Write('Input Korean score : ');
Readln(student[count].korea);
Write('Input Math score : ');
Readln(student[count].math);
Write('Input English score : ');
Readln(student[count].english);
student[count].total := student[count].korea + student[count].math
+ student[count].english;
Writeln;
until Last-1 < count;
end; { input }
procedure output; { 자료를 출력하는 부분 }
var
i : integer;
begin { output }
writeln('[rank] [num] [name] [korean] [math] [english] [total]');
for i := 1 to count do
begin
write(count-i+1);
write(' ');
write(student[i].number);
write(' ');
write(student[i].nickname);
write(' ');
write(student[i].korea);
write(' ');
write(student[i].math);
write(' ');
write(student[i].english);
write(' ');
write(student[i].total);
writeln;
end;
end; { output }
begin { main }
input; { 자료 입력 }
QuickSort(1, Last); { 정렬 부분 }
output; { 자료 출력 }
end. { main }