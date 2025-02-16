from boyer_moor_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search
from timeit import timeit


if __name__ == "__main__":
    with open("st1.txt", "r", encoding="utf-8") as f:
        text1 = f.read()
    with open("st2.txt", "r", encoding="utf-8") as f:
        text2 = f.read()

    patterns = {"existing": "алгоритм", "non_existing": "gfdgdfgdfgklj"}

    for pattern_type, pattern in patterns.items():
        for i, text in enumerate([text1, text2], 1):
            bm_time = timeit(lambda: boyer_moore_search(text, pattern), number=1000)
            kmp_time = timeit(lambda: kmp_search(text, pattern), number=1000)
            rk_time = timeit(lambda: rabin_karp_search(text, pattern), number=1000)

            print(
                f"Artickle {i} - {pattern_type}: Boyer-Moore = {bm_time:.6f}s, KMP = {kmp_time:.6f}s, Rabin-Karp = {rk_time:.6f}s"
            )
