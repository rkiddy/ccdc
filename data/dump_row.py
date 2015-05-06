import sys

try:
    filename = sys.argv[1]
    line_num = int(sys.argv[2])
    lines = [line_num]
except IndexError:
    print ''
    print 'Please provide a tsv file name and a line number. A second number will give you a range.'
    print ''
    exit()

if len(sys.argv) > 3:
    last_num = sys.argv[3]
    lines = range(int(line_num), int(last_num)+1)

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
