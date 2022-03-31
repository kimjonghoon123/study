program programming_kjh(input, output);



type
	Index = 1..Last;
	std = record { 학생 개인 정보 : 학번, 이름, 과목점수, 총점 }
		c, java, pyhon, tot : integer;
		number : string;
		pname : string;
		
	end;
var
	count : integer;
	people : array[Index] of std;

procedure Exchange(var X, Y: integer);

var
	temp : integer;
	tdata : std;

begin 
	
	tdata := people[X];
	people[X] := people[Y];
	people[Y] := tdata;
	
	temp := X;
	X := Y;
	Y := temp;
end; 


procedure Partition(Low, High: integer; var SplitIndex: integer);

var
	splitdata, up, down: integer;
begin
	splitdata := people[Low].tot; 
	up := Low;
	down := High;

	repeat
		While (people[up].tot <= splitdata) and (up < High) do
			up := up + 1;
		While (people[down].tot > splitdata) and (down > Low) do 
			down := down - 1;
		If up < down then 
			Exchange(up, down)
	until up >= down;

	SplitIndex := down;
	Exchange(Low, down);
end;


procedure qsort(Low, High : integer);

var
	SplitIndex: integer;

begin 
	If Low < High Then
	begin
		Partition(Low, High, SplitIndex); 
		qsort(Low, SplitIndex-1); 
		qsort(SplitIndex+1, High); 	end;
end; 


procedure input; { 자료를 입력받는 부분 }

begin { input }
	count := 0;

	repeat
		count := count + 1; 
		Write('Input Number       :');
		Readln(people[count].number);
		Write('Input Name         :');
		Readln(people[count].pname);
		Write('Input C++ score    :');
		Readln(people[count].c);
		Write('Input java score   :');
		Readln(people[count].java);
		Write('Input PYTHON score :');
		Readln(people[count].python);

		people[count].tot := people[count].c + people[count].java + people[count].python;
		Writeln;

	until 3 < count;
end;
procedure output; 
var
	i : integer;

begin
	writeln('[rank] [num] [name] [C++] [java] [PYTHON] [tot]');
	for i := 1 to count do
	begin
		write(count-i+1);
		write('	');

		write(people[i].number);
		write('	');

		write(people[i].pname);
		write('	');

		write(people[i].c);
		write('	');

		write(people[i].java);
		write('	');

		write(people[i].python);
		write('	');

		write(people[i].tot);
		writeln;
	end;
end; 

begin
	input;
	qsort(1, Last); 
	output; 
end. 
