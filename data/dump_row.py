import sys

try:
    filename = sys.argv[1]
    line_num = int(sys.argv[2])
    lines = [line_num]
except IndexError:
    print ''
    print 'Please provide a tsv file name and a line number.
    print ''
    print 'A second number will give you a range.'
    print ''
    print 'If you use the word "error" as the second parameter, you'
    print 'will get lines starting at the line number of the first'
    print 'parameter, until there is an error.'
    print '(Not Yet Implemented)'
    print ''
    exit()

if len(sys.argv) > 3:
    if sys.argv[3] == 'error':
        until_error = True
    else:
        until_error = False    
        lines = range(int(line_num), int(sys.argv[3])+1)

print 'filename: %s' % filename

if not filename.startswith('tsv/'):
    filename = 'tsv/%s' % filename

f = open(filename, 'r')

columns = f.readline().strip('\r\n').split('\t')

for i in range(1,line_num):
    f.readline()

print ''

for idx in lines:

    error = False

    line_parts = f.readline().strip('\r\n').split('\t')

    while len(columns) < len(line_parts):
        columns.append('EXTRA')
        error = True

    while len(line_parts) < len(columns):
        line_parts.append('MISSING')
        error = True

    for idx in range(len(line_parts)):
        print '%s:  %s: "%s"' % (str(idx).rjust(4), columns[idx].rjust(12, ' '), line_parts[idx])

    while columns[-1] == 'EXTRA':
        columns.pop()

    if error:
        print ''
        print '****** ERROR ******'

    print ''
