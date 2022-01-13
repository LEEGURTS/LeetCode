strs = input("문자 입력")


def oddFind(s: list[str]) -> str:
    final = 0
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            temp = i + 1;
            gap = 1
            result = 1
            while temp-gap>=0 and temp+gap < len(s) and s[temp + gap] == s[temp - gap]:
                result += 2
                gap += 1
            if result > final:
                final = result

    return final


def evenFind(s: list[str]) -> str:
    final=0;
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            left=i
            right=i+1
            result=0
            while left!=0 and right < len(s) and s[left]==s[right]:
                result+=2
                left+=1
                right+=1
            if result > final:
                final = result
    return final


print(evenFind(strs))
