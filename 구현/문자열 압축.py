
def solution(s):

    nlist = [len(s)]

    for itv in range(1,len(s)//2+1) :
        cnt = 0
        tmp = ""
        word = s[:itv]
        idx = 0
        for idx in range(0, len(s), itv) :
            if s[idx:idx+itv] == word :
                cnt += 1
            else :
                if cnt > 1 :
                    tmp += str(cnt) + word
                else :
                    tmp += word

                if(len(s) - idx < len(word)) :
                    tmp += s[idx:]
                    break
                word = s[idx:idx+itv]
                cnt = 0
                continue
        nlist.append(len(tmp))

    return min(nlist)

print(solution("ababcdcdababcdcd"))
