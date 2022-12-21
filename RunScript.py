import os
foo = ('yes' if os.environ('SAMPLE').strip() == "1" else 'no')
print(f"{foo} , {len(os.environ('SAMPLE'))}")