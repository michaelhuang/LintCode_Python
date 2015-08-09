class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        dic = ['1', '11', '21', '1211', '111221', '312211']
        if n < 7:
            return dic[n - 1]

        res = '312211'
        for i in xrange(7, n + 1):
            index, count, temp = res[0], 1, []
            for j in xrange(1, len(res)):
                if index == res[j]:
                    count += 1
                else:
                    temp.extend([str(count), index])
                    index, count = res[j], 1
            temp.extend([str(count), index])
            res = temp
        return ''.join(res)
