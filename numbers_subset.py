"""
Given a set of n integers and sum of all numbers is at K, find the subset of 
consecutive elements whose sum is exactly half of the total sum of n
"""
def find_subset_indices(numbers, sum_all):
    half_sum = sum_all // 2
    totals = [0] * sum_all
    for i, n in enumerate(numbers):
        for pos in xrange(0, i + 1):
            totals[pos] += n
            if totals[pos] == half_sum:
                return (pos, i)
    return (0, 0)

if __name__ == '__main__':
    numbers = [1, 3, 9, 7, 4, 8, 6]
    sum_all = sum(numbers)
    start, end = find_subset_indices(numbers, sum_all)
    print 'Total sum: %s' % sum_all
    print 'Half sum: %s' % (sum_all // 2)
    if not start and not end:
        print 'Not found!'
    else:
        print numbers[start:end + 1]
