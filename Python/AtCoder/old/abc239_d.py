class Prime:
    def __init__(self, max_number=100010):
        """素数、素因数クラス
        max_numberが大きいほど初期化が遅い(O(nloglogn))
        max_number未満の素数のリストprime_list
        素数か判定する関数is_prime(int)
        素因数を1つ返す関数get_a_prime_factor(int)
        素因数全体を返す関数get_prime_factors(int)
        整数値リストの素因数全体を返す関数get_prime_factors_of_list(list)
        max_numberより小さい数値の場合は、エラトステネスの櫛で処理する
        そうでない場合は、試し割り法で処理する

        Args:
            max_number (int): [description]
        """
        self._max_number = max_number-1
        self._is_prime_list = []
        self.prime_list = []
        self._div_list = []
        if max_number >= 1:
            (self.prime_list,
             self._div_list,
             self._is_prime_list) = self.sieve(self._max_number)

    def sieve(self, n: int) -> list:  # n以下の素数全列挙(O(n_log_log_n))
        """n以下の素数全列挙(O(n_log_log_n))

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
        つまり、nを割る素数を返す
        nが合成数でない場合（1または素数）は-1を返す
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

    def factorization(self, n) -> dict:
        """素因数分解
        nを素因数分解し、引数に整数を入れると係数が返ってくる辞書を返す

        Args:
            n ([type]): [description]

        Returns:
            dict: [description]
        """
        ret = {}

        if n <= self._max_number:  # nはmax_number以下でなければならない
            cnt = 0
            while not (self.is_prime(n) or n == 1):  # nが素数もしくは1になるまで
                prime_factor = self.get_a_prime_factor(n)
                if prime_factor in ret:
                    ret[self.get_a_prime_factor(n)] += 1  # nの最大の素因数を追加し
                else:
                    ret[self.get_a_prime_factor(n)] = 1
                n = n // self.get_a_prime_factor(n)  # nを素因数で割る

            if n != 1:
                if n in ret:
                    ret[n] += 1
                else:
                    ret[n] = 1

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
    a, b, c, d = map(int, input().split())

    # 全探索
    prime = Prime(200)
    taka_win = False
    for taka in range(a, b+1):
        # 青木君が何を選んでも高橋君の勝利が確定するか
        for aoki in range(c, d+1):
            val = taka+aoki
            aoki_win = False
            if prime.is_prime(val):
                aoki_win = True
                break
        if not aoki_win:
            # 高橋君の処理が確定する、aokiの選び方が存在する
            taka_win = True
            break

    if taka_win:
        print('Takahashi')
    else:
        print('Aoki')


main()
