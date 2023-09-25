
class NodeTree:
    def __init__(self, key=None, ptr=None, Left=None, Right=None):
        self._key = key
        self._ptr = ptr
        self._Left = Left
        self._Right = Right

    @property
    def key(self):
        return self._key

    @property
    def ptr(self):
        return self._ptr

    @property
    def Left(self):
        return self._Left

    @property
    def Right(self):
        return self._Right

    @key.setter
    def key(self, k):
        self._key = k

    @ptr.setter
    def ptr(self, p):
        self._ptr = p

    @Right.setter
    def Right(self, right):
        self._Right = right

    @Left.setter
    def Left(self, left):
        self._Left = left


vec = [3, 2, 1, 0]
mid = len(vec) // 2
node = NodeTree(vec[mid], mid, mid - 1, mid + 1)
def pick(vec, node):
    if node.Left == -1 and vec[node.ptr] >= vec[node.Right]:
        return(node.ptr)
    if node.Right == len(vec) and vec[node.ptr] >= vec[node.Left]:
        return(node.ptr)
    if node.key >= vec[node.Left] and node.key >= vec[node.Right]:
        return(node.ptr)
    else:
        if vec[node.Left] > vec[node.ptr]:
            node.Right = node.ptr
            node.ptr = node.Left
            node.key = vec[node.ptr]
            node.Left -= 1
            return pick(vec, node)
        if vec[node.Right] > vec[node.ptr]:
            node.Left = node.ptr
            node.ptr = node.Right
            node.key = vec[node.ptr]
            node.Right += 1
            return pick(vec, node)

print(pick(vec, node))