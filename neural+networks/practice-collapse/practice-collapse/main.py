import numpy as np


# Write your function here!
def collapse(values):
    shape = values.shape[0]
    answer = np.zeros((shape, 1), dtype=np.int64)
    index = 0
    for arr in values:
        answer[index] = np.sum(arr)
        index += 1
    return answer


def main():
    values = np.arange(12).reshape((3, 4))
    print(values)
    result = collapse(values)
    print(result)


if __name__ == '__main__':
    main()
