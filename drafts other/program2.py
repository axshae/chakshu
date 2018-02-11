print '\n---FIRST PROGRAM IN CHAKSHU PROGRAMMING LANGUAGE----\n\n'
print '**Find factorial of given number n**\n'

function get_fact(number) then
    fact=1
    repeat until number>0 then
        fact=fact*number
        number=number-1
    end
    print fact
end
input_number=input '\nFind factorial of?\nNumber: '

get_fact(int(input_number))
input
print '\nProgram terminated!'
