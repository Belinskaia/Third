Skip to content
shinobu9
/
mipt_advanced_python
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
mipt_advanced_python/Lab 9 iterators and subprocesses/BinTree.py
@shinobu9
shinobu9 threads initial
 1 contributor
146 lines (114 sloc)  4.2 KB
#в лабе есть файл png
#в нем скрин ввода и вывода данной программы

class BinTree:
    def __init__ (self):
        self.start = None
        self.lenght = 0
        self.last = None

    def __iter__():
        pass

    def add(self, value):
        elem = Node(value)
        if self.start is None:
            self.start = elem
            self.length = 1
        else:
            self.current = self.start
            while True:
                if self.current.value >= value:
                    if self.current.left == None:
                        self.current.left = elem
                        break
                    else:
                        self.current = self.current.left
                else:
                    if self.current.right == None:
                        self.current.right = elem
                        break
                    else:
                        self.current = self.current.right
            self.lenght += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        #создает список обхода в глубину
        node = self.start
        stack = []
        result = []
        while node or stack:
            while node:
                stack.append(node)
                result.append(node)
                node = node.left
                
            if stack:
                node = stack.pop()
                node = node.right
        return iter(result)

    def __str__(self):
        lines = self._build_tree_string(self.start, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    @staticmethod
    def _build_tree_string(root, curr_index, index=False, delimiter='-'):
    
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
        else:
            node_repr = str(root.value)

        new_root_width = gap_size = len(node_repr)

    # получаем левую и правую часть + их размеры
        l_box, l_box_width, l_root_start, l_root_end = \
            BinTree._build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            BinTree._build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        line1.append(node_repr)
        line2.append(' ' * new_root_width)

    # добавляет пробелы
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

    # объеденяет левую и правую часть
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), new_root_start, new_root_end







class Node:
    def __init__(self, value, lft = None, rght = None):
        self.value = value
        self.left = lft
        self.right = rght

    def get_value(self):
        return self.value

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def __str__(self):
        return str(self.get_value())

my_tree = BinTree()

for i in range(10):
    value = int(input())
    my_tree.add (value)
print (my_tree)
for i in my_tree:
    print (i)


