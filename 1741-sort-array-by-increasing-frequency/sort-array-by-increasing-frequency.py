from collections import Counter

class Solution:
    def frequencySort(self, nums):
        count = Counter(nums)
        result = []

        for num in count:
            result.append(num)
            
        for i in range(len(result)):
            for j in range(i + 1, len(result)):

                if count[result[i]] > count[result[j]]:
                    result[i], result[j] = result[j], result[i]

                elif count[result[i]] == count[result[j]]:
                    if result[i] < result[j]:
                        result[i], result[j] = result[j], result[i]

        answer = []

        for num in result:
            for i in range(count[num]):
                answer.append(num)

        return answer