#!/usr/bin/python
import sys
#Class definition
class MyClass:
#print "Found function"
    count = 0
    save = 0 
    count_line = 1
    state = 0
    flag = False
    late = -1
    m=''
    matrix = [["@",1,"#"],#state 0
              ["T",2,"#"],#state 1
              ["r",3,"#"],#state 2
              ["a",4,"#"],#state 3
              ["n",5,"#"],#state 4
              ["s",6,"#"],#state 5
              ["d",7,"#"],#state 6
              ["u",8,"#"],#state 7
              ["c",9,"#"],#state 8
              ["e",10,"#"],#state 9
              ["r",11,"#"],#state 10
              [" ",12,"#"],#state 11
              ["N",13,"#"],#state 12
              ["N",13," ",12,"\n",14,"#"],#state 13
              ["N",15,"#"],#state 14
                [" ",16,"#"],#state 15
                ["C",17,"@","E","#"],#state 16  goto 30, and save current
                ["C",17," ",18,"#"],#state 17
                ["C",19,"@","E","#"],#state 18
                ["C",19," ",20,"#"],#state 19
                ["N",21,"#"],#state 20
                ["\n",22,"#"],#state 21  Final
                ["N",15,"\n",22,"#"],#state 22 Final
              ["@",24,"#"],#state 23 
              ["e",25,"#"],#state 24
              ["p",26,"#"],#state 25
              ["s",27,"#"],#state 26
              ["i",28,"#"],#state 27
              ["l",29,"#"],#state 28
              ["o",30,"#"],#state 29
              ["n","F","#"]]#state 30 # return 17, save 0
    def Return(self, x):
        self.late=self.state
        try:
            
            col=0
            result = "A"
            #temp = x.upper() upper case
            temp = x
            if x.isdigit():
                temp="N"
            
            if self.state==16 or self.state==18 or self.state==19 or self.state==17:
                if x.isalpha():
                    temp="C"
            while self.matrix[self.state][col]!="#":      
                if self.matrix[self.state][col] == temp:
                    result = self.matrix[self.state][col+1]
                col=col+2
            if str(result).isdigit():
                return result
            if result == 'E':
                self.save = self.state
                return 24
            if result == 'F':
                t = self.save
                #print "temp:", t
                self.save = t
                return (t+1)
            else:
                return -1
        except:
            return -1
    def Update(self):
        i = 0
        self.count_line = 1
        counter = 0
        while i < self.count:
            #print self.m[i]
            if '\n' in self.m[i]:
                self.count_line = self.count_line + 1
                counter = 0
            counter = counter + 1     
            i = i + 1
        #print 'counter:', counter
        return counter
            
    def Read(self, x):
        self.m=''
        for line in x:
            self.m = self.m + line#m is just the complete text
            #print self.state, line 
            if self.Return(line) == -1:
                self.Expect(line)
                return False
            else:
                self.state = self.Return(line)
                self.count = self.count + 1
        if self.state == 21 or self.state == 22:
            return True
        self.Complete()
        return False
    #Complete function:
    def Complete(self):
        print 'Complete the file as a Grail File'
    #Print function:
    def PrintM(self):
        row=0
        while row<20:
            col=0
            while col<2:
                print self.matrix[row][col],
                col=col+1
            print ("")
            row=row+1
    #Return what character should be use:
    def Expect(self, x ):
        #m1 == put the simple increse by one, but with the exceptions
        i = 0
        temp = self.state
        exp = self.matrix[temp][i]
        #print temp
        print 'Expected:',
        while self.matrix[temp][i]!= '#':
            exp = self.matrix[temp][i]
            if '\n' in exp:#formating instructions:
                exp = 'new line'
            if exp == 'N':
                exp = 'number'
            if exp == ' ':
                exp = 'space'
            if exp == 'C':
                exp = 'character'
            print exp,
            if self.matrix[temp][i+2]!= '#':
                print 'or',
            i = i + 2
        #print 'at', self.count, 'character',
        if '\n' in x:
            print 'instead of new line',
        else:
            print 'instead of "',x,'"',
        position = self.Update()
        print 'in position: ',position,'line:',self.count_line

#Operation:
print 'Number of arguments:',len(sys.argv), 'arguments.',
if len(sys.argv) > 1:
#print 'Argument List:', str(sys.argv)
#print 'first', sys.argv[1] #sys.argv[1:] all of them
    print 'File enter by user'
    name = sys.argv[1] #take the first argument
    fo = open(name, "r")
    text = fo.read()
    if len(sys.argv) > 2 and sys.argv[2] == 'Y':
        print text
    x = MyClass()
    print x.Read(text) #Show the result:
else: #Default.txt
    print 'File enter by default'
    fo = open("Default.txt", "r")
    text = fo.read()
    if len(sys.argv) > 2 and sys.argv[2] == 'Y':
        print text
    x = MyClass()
    print x.Read(text) #Show the result:
    
