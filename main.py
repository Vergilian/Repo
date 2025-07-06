text = "hello world hello"
world_count= {}
for word in text.split():
    if word in world_count:
        world_count[word] += 1
    else:
        world_count[word] = 1

print(world_count)
