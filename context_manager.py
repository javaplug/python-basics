
class Manager:
    def __enter__(self):
        print('Entering')
        return 'some data'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Existing')
        print(exc_type, exc_val, exc_tb)


if __name__ == '__main__':
    m = Manager()
    with m:
        print('some execution')

    with m as context:
        print(f'Execution with context {context}')
        int('n/a')

