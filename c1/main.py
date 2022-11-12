from tasks import add

result = add.apply_async(({'0': 'c1 (START)'}, ))

# Optional

print(result.get())
