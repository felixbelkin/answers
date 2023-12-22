def dislike_6(a):
    if isinstance(a, (int, float)) and a == 6:
        return "Только не б!"
    else:
        return True

print(dislike_6(6))    
print(dislike_6(5))     
print(dislike_6(6.0))   
print(dislike_6("test"))
