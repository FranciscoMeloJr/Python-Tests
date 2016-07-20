#!/usr/bin/python
import sys
import Grail_validation_module
#Class definition
class MyClass:
#print "Found function"
    count = 0
    count_line = 1
    state = 0
    flag = False
    late = -1
    m=''
    final = False
    matrix = [["(",1,"#"],#state 0
              ["S",2,"#"],#state 1
              ["T",3,"#"],#state 2
              ["A",4,"#"],#state 3
              ["R",5,"#"],#state 4
              ["T",6,"#"],#state 5
              [")",7,"#"],#state 6
              [" ",8,"#"],#state 7
              ["|",9,"#"],#state 8
              ["-",10,"#"],#state 9
              [" ",11,"#"],#state 10
              ["N",12,"#"],#state 11
              ["N",12,"\n",13,"#"],#state 12
              ["(",1,"N",14,"#"],#state 13
              ["N",14," ",15,"#"],#state 14
              ["N",16," ",-1,"-","T","#"],#state 15 #problem state
              [" ",17,"#"],#state 16 accept only one space
              ["N","V","#"],#state 17
              ["N",18,"\n",19,"#"],#state 18
              ["N",14," ",19,"|",20,"#"],#state 19
              ["|",21,"#"],#state 20
              [" ",22,"#"],#state 21
              ["(",23,"#"],#state 22
              ["F",24,"#"],#state 23
              ["I",25,"#"],#state 24
              ["N",26,"#"],#state 25
              ["A",27,"#"],#state 26
              ["L",28,"#"],#state 27
              [")","F","#"],#state 28
              [" ",29,"\n",29,"#"]]#state 29
    def Return(self, x):
        self.late=self.state
        try:
            
            col=0
            result = "A"
            #temp = x.upper() upper case
            temp = x
            if x.isdigit():
                temp="N"
            while self.matrix[self.state][col]!="#":      
                if self.matrix[self.state][col] == temp:
                    result = self.matrix[self.state][col+1]
                col=col+2
            if str(result).isdigit():
                return result
            if result == 'T':
                if self.flag == True:
                    return 20
                else:
                    return 16
            if result == 'F':
                    self.final = True
                    return 29
            if result == 'V':
                    self.flag = True
                    return 18   
            if result == 'A' and self.state == 15:
                return 16
            else:
                return -1
        except:
            return -1
    def Update(self):
        i = 1
        self.count_line = 1
        counter = 1
        while i <= self.count:
            #print self.m[i]
            if '\n' in self.m[i]:
                self.count_line = self.count_line + 1
                counter = 1
            else:
                counter = counter + 1     
            i = i + 1
        #print 'counter:', counter
        print counter
        return counter
            
    def Read(self, x):
        self.m=''
        for line in x:
            self.m = self.m + line#m is just the complete text
            #print self.state, line
            if self.Return(line) == -1:
                return Expect(line)
            else:
                self.state = self.Return(line)
                self.count = self.count + 1
        if self.state == 29:
            return [-1,-1]
        self.Complete()
        return [-2,-2]
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
        return [position,self.count_line]

#Operation:
#print 'Number of arguments:',len(sys.argv), 'arguments.',
#if len(sys.argv) > 1:
#print 'Argument List:', str(sys.argv)
#print 'first', sys.argv[1] #sys.argv[1:] all of them
#    print 'File enter by user'
#    name = sys.argv[1] #take the first argument
#    fo = open(name, "r")
#    text = fo.read()
#    if len(sys.argv) > 2 and sys.argv[2] == 'Y':
#        print text
#    x = MyClass()
#    print x.Read(text) #Show the result:
#else: #Default.txt
#    print 'File enter by default'
#    fo = open("Default.txt", "r")
#    text = fo.read()
#    if len(sys.argv) > 2 and sys.argv[2] == 'Y':
#        print text
#    x = MyClass()
#    print x.Read(text) #Show the result:
    

def VerifyGrail (name):    # write Fibonacci series up to n
	fo = open(name, "r")
	text = fo.read()
	x = MyClass()
	return x.Read(text)    
