def solution(s):
    words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i, w in enumerate(words):
        s = s.replace(w, str(i))
    return int(s)