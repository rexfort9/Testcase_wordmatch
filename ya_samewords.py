def find_common_prefix(words):
    if not words:
        return ""
    
    prefix = words[0]
    
    for word in words[1:]:
        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Word massive (editable)
massive = ["apple", "application", "apply", "approve", "applause", "append"]
prefix = find_common_prefix(massive)
print(prefix)
