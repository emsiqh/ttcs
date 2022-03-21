from collections import defaultdict


class Graph:
    # khởi tạo: u - đỉnh
    def __init__(self, u):
        self.U = u

        # Tạo 1 dict để lưu trữ đồ thị
        self.graph = defaultdict(list)

    # hàm thêm cạnh vào đồ thị (v là đỉnh liền kề với u hiện tại)
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # kiểm tra xem đã đến đích chưa
    def checkTarget(self, src, target, maxDepth):
        if src == target:
            return True

        # Nếu đã quá độ sâu tối đa, trả về False
        if maxDepth <= 0:
            return False

        # Sử dụng đệ quy qua tất cả các đỉnh liền kề với đỉnh hiện tại
        for i in self.graph[src]:
            if (self.checkTarget(i, target, maxDepth-1)):
                return True

        return False

    def IDDFS(self, src, target, maxDepth):

        # Tìm kiếm cho đến độ sâu tối đa
        for i in range(maxDepth):
            if (self.checkTarget(src, target, i)):
                return True
        return False


# Main
if __name__ == '__main__':
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)

    target = 6
    maxDepth = 3
    src = 3
    if g.IDDFS(src, target, maxDepth):
        print("Tồn tại đường đi")
    else:
        print("Không tồn tại đường đi")

# https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/
