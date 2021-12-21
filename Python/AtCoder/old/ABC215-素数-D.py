class Prime:
    def __init__(self, max_number: int):
        """素数、素因数クラス
        max_numberが大きいほど初期化が遅い(O(nloglogn))
        max_number以下の素数のリストprime_list
        素数か判定する関数is_prime(int)
        素因数を1つ返す関数get_a_prime_factor(int)
        素因数全体を返す関数get_prime_factors(int)
        整数値リストの素因数全体を返す関数get_prime_factors_of_list(list)
        max_numberより小さい数値の場合は、エラトステネスの櫛で処理する
        そうでない場合は、試し割り法で処理する

        Args:
            max_number (int): [description]
        """
        self._max_number = max_number
        self._is_prime_list = []
        self.prime_list = []
        self._div_list = []
        if max_number >= 1:
            self.prime_list, self._div_list, self._is_prime_list = self.sieve(max_number)

    def sieve(self, n: int) -> list:  # n以下の素数全列挙(O(nloglogn))
        """n以下の素数全列挙(O(nloglogn))

        Args:
            n (int): [description]

        Returns:
            list: [素数のlist,最大の素因数のlist, 素数か判定するlist]からなるlist
        """
        assert n <= self._max_number  # nはmax_number以下でなければならない
        ret = []  # 素数のリスト
        div_list = [-1] * (n+1)  # 何で割ったかのリスト(初期値は-1)

        # エラトステネスの櫛
        is_prime_list = [True] * (n+1)
        is_prime_list[0] = False
        is_prime_list[1] = False

        for ind in range(2, n+1):
            if is_prime_list[ind]:
                ret.append(ind)
                ind2 = ind ** 2
                for ind3 in range(ind2, n+1, ind):
                    is_prime_list[ind3] = False
                    div_list[ind3] = ind

        return ret, div_list, is_prime_list

    def is_prime(self, n: int) -> int:
        """素数かどうか判定する
        max_numbers以下の時はエラトステネスの櫛で
        以上の時は試し割り法で処理する

        Args:
            n (int): [description]

        Returns:
            int: [素数ならばTrue,それ以外はFalse]
        """
        if n <= self._max_number:
            return self._is_prime_list[n]
        else:
            def is_prime_trial_division(n):
                if n == 1:
                    return True
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        return False
                return True
            return is_prime_trial_division(n)

    def get_a_prime_factor(self, n: int) -> int:
        """素因数を返す
        つまり、nを割る最大の素数を返す
        max_numbers以下の時はエラトステネスの櫛で
        以上の時は試し割り法で処理する

        Args:
            n (int): [description]

        Returns:
            int: [description]
        """
        if n <= self._max_number:
            return self._div_list[n]
        else:
            for i in range(2, int(-(-n**0.5//1))+1):
                if n % i == 0:
                    return i
            return -1

    def get_prime_factors(self, n: int) -> set:
        """素因数の集合を返す
        max_numbers以下の時はエラトステネスの櫛で
        以上の時は試し割り法で処理する

        Args:
            n (int): [description]

        Returns:
            set: [description]
        """
        if n <= self._max_number:  # nはmax_number以下でなければならない
            ret = set()
            while not (self.is_prime(n) or n == 1):  # nが素数もしくは1になるまで
                ret.add(self.get_a_prime_factor(n))  # nの最大の素因数を追加し
                n = n // self.get_a_prime_factor(n)  # nを素因数で割る

            if n != 1:
                ret.add(n)

            return ret
        else:
            def prime_factors_trial_division(n):
                ret = set()
                temp = n
                for i in range(2, int(-(-n**0.5//1))+1):
                    if temp % i == 0:
                        cnt = 0
                        while temp % i == 0:
                            cnt += 1
                            temp = temp // i
                        ret.add(i)

                if temp != 1:
                    ret.add(temp)

                if not ret:
                    ret.add(n)

                return ret
            return prime_factors_trial_division(n)

    def get_prime_factors_of_list(self, n_list: list) -> set:
        """整数のlistの素因数の集合を返す
        get_prime_factorsを繰り返すより、リストに対して一度に処理したほうが数倍以上高速

        Args:
            n_list (list): [description]

        Returns:
            set: [description]
        """
        ret = set()
        for n in n_list:
            assert n <= self._max_number  # nはmax_number以下でなければならない
            while not (self.is_prime(n) or n == 1):  # nが素数もしくは1になるまで
                ret.add(self.get_a_prime_factor(n))  # nの最大の素因数を追加し
                n = n // self.get_a_prime_factor(n)  # nを素因数で割る

            if n != 1:
                ret.add(n)
        return ret

    def factorization(self, n) -> list:
        """素因数分解
        nを素因数分解し、引数に整数を入れると係数が返ってくるlistを返す
        >list_ = c_prime.factorization(6)
        >print(list_)
        [0, 0, 1, 1, 0, 0, 0]

        Args:
            n ([type]): [description]

        Returns:
            list: [description]
        """
        ret = [0]*(n+1)

        if n <= self._max_number:  # nはmax_number以下でなければならない
            cnt = 0
            while not (self.is_prime(n) or n == 1):  # nが素数もしくは1になるまで
                ret[self.get_a_prime_factor(n)] += 1  # nの最大の素因数を追加し
                n = n // self.get_a_prime_factor(n)  # nを素因数で割る

            if n != 1:
                ret[n] += 1

            return ret
        else:
            temp = n
            for i in range(2, int(-(-n**0.5//1))+1):
                if temp % i == 0:
                    cnt = 0
                    while temp % i == 0:
                        cnt += 1
                        temp = temp // i
                    ret[i] = cnt

            if temp != 1:
                ret[temp] = 1

            if not ret:
                ret[n] = 1
            return ret


def main():
    c_prime = Prime(100010)
    # エラトステネスの櫛を使用する必要がないときは、
    # c_prime = Prime(0)等と、小さい数値を入れる

    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    prime_of_A = set()

    # Aの素因数全体の集合を作成する
    prime_of_A = c_prime.get_prime_factors_of_list(A)

    dp = [True] * (m+1)
    dp[0] = False

    for prime in prime_of_A:
        for i in range(prime, m+1, prime):
            dp[i] = False

    ans = []
    for i in range(m+1):
        if dp[i]:
            ans.append(str(i))

    print(len(ans))
    print(*ans, sep='\n')


main()
