class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        if string is None or length == 0:
            return None

        space_count, rep_arr = 0, ['%', '2', '0']
        for i in string:
            if i == ' ':
                space_count += 1

        true_len = length + 2 * space_count
        j, k = length - 1, true_len - 1
        while j >= 0:
            if string[j] == ' ':
                k -= 3
                for i in xrange(3):
                    string[k + 1 + i] = rep_arr[i]
            else:
                string[k] = string[j]
                k -= 1
            j -= 1

        return true_len

if __name__ == '__main__':
    a = Solution()
    a1 = ['A', 'B', 'C', ' ', 'D', ' ', '', '', '', '']
    print a.replaceBlank(a1, 6)
    print a1
