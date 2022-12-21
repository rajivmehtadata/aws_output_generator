import os
foo = ('yes' if os.getenv('SAMPLE') == "1" else 'no')
print(f'{foo}')