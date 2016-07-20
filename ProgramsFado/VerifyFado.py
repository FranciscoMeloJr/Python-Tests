#!/usr/bin/python
import sys
#Class definition
class MyClass:
#print "Found function"
    count = 0
    count_line = 1
    state = 0
    flag = False
    late = -1
    m=''
    matrix = [["@",1,"%"],#state 0
              ["N",2,"%"],#state 1
              ["F",3,"%"],#state 2
              ["A",4,"%"],#state 3
              [" ",5,"%"],#state 4
              ["N",6,"%"],#state 5
              ["N",6," ",5,"\n",7,"%"],#state 6
              ["N",8,"%"],#state 7
              ["N",8," ",9,"%"],#state 8
              ["N",10,"%"],#state 9
              ["N",10," ",11,"%"],#state 10
              ["N",12,"%"],#state 11
              ["N",12,"\n",13,"#",14,"%"],#state 12
              ["N",8,"#",14,"%"],#state 13
              ["\n",7,"%"]]#state 14

    def Return(self, x):
        self.late=self.state
        try:
            
            col=0
            result = "A"
            #temp = x.upper() upper case
            temp = x
            if x.isdigit():
                temp="N"
            while self.matrix[self.state][col]!="%":      
                if self.matrix[self.state][col] == temp:
                    result = self.matrix[self.state][col+1]
                col=col+2
            if str(result).isdigit():
                return result
            if result == 'A' and self.state == 14:
                return 14
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
            print self.state, line
            if self.Return(line) == -1:
                return self.Expect(line)
            else:
                self.state = self.Return(line)
                self.count = self.count + 1
        if self.state == 13 or self.state==14:
            return [-1,-1]
        self.Complete()
        return [-2,-2]
    #Complete function:
    def Complete(self):
        print 'Complete the file as a FAdo File'
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
        while self.matrix[temp][i]!= '%':
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

def VerifyFAdo (name):    # write Fibonacci series up to n
	fo = open(name, "r")
	text = fo.read()
	x = MyClass()
	return x.Read(text)    
    
