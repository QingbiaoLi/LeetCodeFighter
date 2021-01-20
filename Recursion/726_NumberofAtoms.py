class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        self.index = 0
        res = ""

        counter = self.countOfAtoms_(formula)

        for atom, num in sorted(counter.items()):
            if num == 1:
                res += atom
            else:
                res += atom + str(num)
        return res

    def countOfAtoms_(self, formula):
        import collections
        counter = collections.Counter()
        if not formula: return counter

        while self.index != len(formula):
            if formula[self.index] == "(":
                self.index = self.index + 1
                tmp_counter = self.countOfAtoms_(formula)
                count_repeat = self.getCount(formula, self.index)
                for name_atom, count_key in enumerate(tmp_counter):
                    counter[name_atom] += count_key * count_repeat
            elif formula[self.index] == ")":
                self.index += 1
                return counter
            else:
                name_atom = self.getName(formula, self.index)
                self.index += 1
                counter[name_atom] += self.getCount(formula, self.index)
                self.index+=1

        return counter


    def getName(self, formula, index):
        name = ''
        while formula[index].isalpha() and (name == '' or formula[index].islower()):
            name += formula[index]

        return name

    def getCount(self, formula, index):
        count_str = ''
        # ans = 0
        while formula[index].isdigit():
            index += 1
            count_str += formula[index]
        if count_str == '':
            ans = 1
        else:
            ans = int(count_str)
        return ans

class Solution_bc(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        i = 0
        res = ""

        counter = self.countOfAtoms_(formula, i)

        for atom, num in sorted(counter.items()):
            if num == 1:
                res += atom
            else:
                res += atom + str(num)
        return res

    def countOfAtoms_(self, formula, i):
        import collections
        counter = collections.Counter()
        if not formula: return counter

        while i != len(formula):
            if formula[i] == "(":
                i = i + 1
                tmp_counter = self.countOfAtoms_(formula, i)
                count_repeat = self.getCount(formula, i)
                for name_atom, count_key in enumerate(tmp_counter):
                    counter[name_atom] += count_key * count_repeat
            elif formula[i] == ")":
                i += 1
                return counter
            else:
                name_atom = self.getName(formula, i)
                counter[name_atom] += self.getCount(formula,i)
                i+=1

        return counter


    def getName(self, formula, i):
        name = ''
        while formula[i].isalpha() and (name == '' or formula[i].islower()):
            name += formula[i]
            i += 1

        return name

    def getCount(self, formula, i):
        count_str = ''
        # ans = 0
        while formula[i].isdigit():
            count_str += formula[i]
            i += 1
        if count_str == '':
            ans = 1
        else:
            ans = int(count_str)
        return ans

class Solution2(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        count = self.dfs(formula)
        res = ""
        for atom, num in sorted(count.items()):
            if num == 1:
                res += atom
            else:
                res += atom + str(num)
        return res

    def dfs(self, formula):
        import collections
        count = collections.Counter()
        if not formula: return count
        i = 0
        while i < len(formula):
            if formula[i].isalpha():  # 首字母是英文字符
                atom = formula[i]
                atomNum = 0
                # 找到这个元素所有字符
                i += 1
                while i < len(formula) and formula[i].isalpha() and formula[i].islower():
                    atom += formula[i]
                    i += 1
                while i < len(formula) and formula[i].isdigit():  # 后面是否有数字
                    atomNum = 10 * atomNum + int(formula[i])
                    i += 1
                count[atom] += 1 if atomNum == 0 else atomNum
            elif formula[i] == "(":  # 括号匹配
                left = i  # 左括号位置
                parent = 1  # 统计括号个数
                while i < len(formula) and parent != 0:
                    i += 1
                    if formula[i] == "(":
                        parent += 1
                    elif formula[i] == ")":
                        parent -= 1
                right = i
                atomNum = 0
                i += 1
                while i < len(formula) and formula[i].isdigit():  # 后面是否有数字
                    atomNum = 10 * atomNum + int(formula[i])
                    i += 1
                innerCount = self.dfs(formula[left + 1: right])
                for c, n in innerCount.items():
                    count[c] += n * atomNum
        count += self.dfs(formula[i + 1:])
        return count

if __name__ == "__main__":
    # a = Solution()
    # a.countOfAtoms("K4(ON(SO3)2)2")
    a = Solution()
    print(a.countOfAtoms("H2O"))
