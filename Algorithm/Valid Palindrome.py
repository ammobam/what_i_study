# 유효한 팰린드롬 (p138)
import collections

# 입력 데이터
s = "A man, a plan, a canal: Panama가가"



# 풀이 1 : re 패키지 이용
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 소문자 변환
        # lower() : 문자 외의 것이 있어도 변환됨
        s = s.lower()
        # 영어와 숫자만 필터링
        s = re.sub("[^0-9a-z]", "", s)
        # 뒤집은 것이 원본과 동일한지 bool 판정
        return s == s[::-1]

# 확인
x = Solution()
x.isPalindrome(s)




# 풀이 2 : deque 이용
# isalnum()이 한글도 통과시키기 때문에 한글이 포함된 팰린드롬에도 적용 가능

s = "가A man, a plan, a canal: Panama가"

import collections
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs = collections.deque()

        for char in s:
            # 영문자, 숫자, 한글 여부 판별
            if char.isalnum():
                # 맞으면 소문자 변환해서 데크에 추가
                strs.append(char.lower())
                #print(strs)

        while len(strs) > 1:
            # 왼쪽에서 꺼낸 것과 오른쪽에서 꺼낸 것이 다르면
            if strs.popleft() != strs.pop():
                # 팰린드롬이 아님
                return False

        # 위의 코드를 모두 통과하면 팰린드롬임
        return True

# 확인
x = Solution()
x.isPalindrome(s)
