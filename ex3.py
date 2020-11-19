# a = 'cipi@test.com'
# a = 'cipi@test@.com'
# a = 'cipi@.com'
# a = 'cipi@a.'
# a = '@test.com'
a = 'cipi@test.com'

x = False
if (a.find('@') > 0):
  if (a.find('@', a.find('@'))> -1):
    if (a.find('.') > -1):
      if (a.find('.', a.find('@')+1)):
        if (a.find('.') < len(a)-1):
          x = True
        else:
          print('invalid email')
      else:
        print('invalid email')
    else:
      print('invalid email')
  else:
    print('invalid email')
else:
  print('invalid email')
        

print(x)

# print the correct error mesages
# make it more easily to be read