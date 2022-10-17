import random as rd

d2 = [1, 2]

while True:
    try:
        print('Input basic value')
        basicVal = int(input())
        break
    except ValueError:
        print('Basic value must be an integer, try again')

tolVal = 1.5 * basicVal / 96
tolVal2 = 0.1 * tolVal

while True:
    try:
        print('Input number of elements')
        numberElem = int(input())
        break
    except ValueError:
        print('Number of elements must be an integer, try again')


def square(series):
    res = []
    for elem in series:
        res.append(elem ** 2)
    return res


def math_expect(series):
    res = 0
    for elem in series:
        res += elem
    return res / len(series)


def variance(series):
    return math_expect(square(series)) - math_expect(series) ** 2


def noise(val):
    return (-1) ** rd.choice(d2) * rd.random() * val


valSeries = []
valSeriesFiltered = []

for i in range(numberElem):
    n = noise(tolVal)
    valSeries.append(basicVal + round(n, 3))
    if abs(n) < tolVal2:
        valSeriesFiltered.append(basicVal + round(n, 3))

output = open('output.txt', 'w')

output.write('Initial series\n')
output.write(f'Number of elements {numberElem}\n')
output.write(f'Tolerance {round(tolVal,3)}\n')
output.write(f'Mathematical expectation {round(math_expect(valSeries),3)}\n')
output.write(f'Variance {round(variance(valSeries),3)}\n')
output.write(f'Standard deviation {round(variance(valSeries)**(1/2),3)}\n')
output.write(f'{valSeries}\n')
output.write('___________________________________________________\n')
output.write('Filtered series\n')
output.write(f'Number of filtered elements {len(valSeriesFiltered)}\n')
output.write(f'Tolerance {round(tolVal2,3)}\n')
output.write(f'Mathematical expectation {round(math_expect(valSeriesFiltered),3)}\n')
output.write(f'Variance {round(variance(valSeriesFiltered),3)}\n')
output.write(f'Standard deviation {round(variance(valSeriesFiltered)**(1/2),3)}\n')
output.write(f'{valSeriesFiltered}\n')
output.write('___________________________________________________\n')
output.write(f'Probability of hitting within filtering range {round(tolVal2/tolVal, 3)}\n')
output.write(f'Frequency of hitting within filtering range {round(len(valSeriesFiltered)/numberElem, 3)}\n')

output.close()
