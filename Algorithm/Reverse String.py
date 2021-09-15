# Reverse String
# 문자열 뒤집기

# 입력
s = ['h', 'e', 'l', 'l', 'o']

# 풀이 1
class Solution:
    def reverseString(self, s: list[str]) -> list[str]:
        s[:] = s[::-1]
        # 확인
        print(s)
# 확인
x = Solution()
x.reverseString(s)

####################################
# 왜 슬라이싱으로 뒤집는 것은 답으로 인정이 안 될까?
type(s[::-1]) # 원본에 반영 안 됨    # <class 'list'>
type(s.reverse()) # 원본에 반영됨    # <class 'NoneType'>

# s[:] 복사본에 할당해서 저장하면 답으로 인정됨
s[:] = s[::-1]


####################################
# 입력
s = ['h', 'e', 'l', 'l', 'o']

# 풀이 2 - 투포인터
class Solution:
    def reverseString(self, s):
        # 각 포인터의 인덱스 : 왼쪽은 처음, 오른쪽은 끝을 가리킴
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # 확인
        print(s)

# 확인
x = Solution()
x.reverseString(s)



####################################
# 입력
s = ['h', 'e', 'l', 'l', 'o']

# 풀이 3 - 파이썬답게
class Solution:
    def reverseString(self, s):
        s.reverse()
        # 확인
        print(s)

# 확인
x = Solution()
x.reverseString(s)

###################