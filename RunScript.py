import os
foo = ('yes' if os.getenv('SAMPLE').strip() == "1" else 'no')
print(f"{foo} , {len(os.getenv('SAMPLE'))}")