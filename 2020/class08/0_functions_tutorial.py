# -*- coding: utf-8 -*-

# %%
# side note: dictionaries in python
# https://www.w3schools.com/python/python_dictionaries.asp
# dummy initialization
thisdict =	{
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964,
  'descriptions': ['awsome', 'badass', 'neat']
}
print(thisdict['model'])
# or with dummy initialization
d = {}
d['name'] = 'max'
d['age'] = 9261
d['weight'] = 234523
# get keys as a list
print( 'keys: ' + repr( list( d.keys() ) ) )
# get values as a list
print( 'values: ' + repr( list( d.values() ) ) )

# %%

# side note: how to display lists
mylist = [1,2,3]
print(mylist)
print('this is mylist', mylist) # this is ok
a_number = 3
# print('this is mylist' + mylist + ' and this is a number: ' + str(a_number) ) # but this will create an error
s = repr( mylist )
print('this is mylist' + repr( mylist ) + ' and this is a number: ' + str(a_number) )


# %%

# for nice tutorials on functions:
# https://www.w3schools.com/python/python_functions.asp

# some basic parts that concern our course
# global variables
x = 'I am x'
s = [1, 2, 3]

# define function that returns nothing - has no arguments
# the function is simply defined here - it is NOT called
def fail_to_change_value_of_x():
    x = 4 # intent to distinguish nested parts
    print( 'x value inside function: ' + str(x) )
    # CAUTION: global variables are not affected
    # each function has its own scope - irrelevant of global
# function ends here - this comment is not necessary

print('x value before function has been called: ' + str(x))
# the function is called here
fail_to_change_value_of_x()
print('x value after function has been called: ' + str(x))

# %%

# define function that returns nothing - has arguments
def fail_to_change_value_of_incoming( t ): # try to use x as argument symbol
    t = 4
    print( 't value inside function: ' + str(t) )
    print( 'x value inside function: ' + str(x) )
    # x = 4 # try to uncomment - the above line becomes an error

# the function is called here
fail_to_change_value_of_incoming(x)


# %%

# define function that returns value - has arguments
def return_value_based_on_incoming( t ):
    y = s[1] + t
    return y

print('x value before function has been called: ' + str(x))
# the function is called here
x = return_value_based_on_incoming(12)
print('x value after function has been called: ' + str(x))


# %%

# multiple arguments
def fun_with_mult_args( a1 , a2 , a3 ):
    return a1 + a2 ** a3

# call function
print( 'multiple arguments example: ' + str( fun_with_mult_args( 1 , 2 , 3 ) ) )


# %%

# multiple returns
def fun_with_mult_args( a1 , a2 , a3 ):
    return a1 + a2 ** a3 , (a1+a2)**a3

# call function
r1 , r2 = fun_with_mult_args( 1 , 2 , 3 )
# r = fun_with_mult_args( 1 , 2 , 3 ) # equally valid but returns tuple
print( 'multiple returns example: r1: ' + str( r1 ) + ' - r2: ' + str( r2 ) )


# %%

# arbitrarily many arguments
def fun_with_arb_mult_args( *args ):
    print( 'arguments are the following: ' + repr(args) )
    y = 1
    if len( args ) == 2:
        y = args[0]**args[1]
    else:
        for a in args:
            y *= a
    return y

# call function
print( 'arbitrary arguments example: ' + str( fun_with_arb_mult_args( 2 , 3 ) ) )


# %%

# keyword agruments
def fun_with_keyword_args( myname , myage=625 ): # try to reverse order
    # check the value of each incoming argument
    print( 'myage: ' + str(myage) )
    print( 'myname: ' + myname )
    return myname + ' ' + str(myage)

# call function without arguments will produce error:
# print( 'keyword arguments - no args: ' + fun_with_keyword_args() )
# call function without initialised argument is ok
print( 'keyword arguments - no initialized arg: ' + fun_with_keyword_args(myname='max') )
# call function with mixed agr order
print( 'keyword arguments - mixed order: ' + fun_with_keyword_args(myage=4321, myname='max') )
# CAUTION: positional arguments (not initialized) need to be placed ahead of initialized


# %%

# arbitrary "dictionary" including many arguments
def fun_with_arb_dict_args( **args ):
    # arguments come in the form of a dictionay
    # we can check keys
    keys_list = list( args.keys() )
    print( repr( keys_list ) )
    # and do what we want
    s = ''
    if 'myname' in keys_list:
        s += 'my name is ' + args['myname']
    if 'myage' in keys_list:
        s += ' and my age is ' + str( args['myage'] )
    return s

# call function
y = fun_with_arb_dict_args( myname='max' , myage=98513 )
print( 'arbitrary dictionary example: ' + y )