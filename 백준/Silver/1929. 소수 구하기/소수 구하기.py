#소수 구하기
#자연수 M 과 N이 빈칸을 사이에 두고 주어진다.
#소수 1과 자기 자신 외에는 나누어 떨어지지 않는다.
import math

# 에라토스테네스의 체 알고리즘을 사용하여 소수를 구하는 함수
def sieve_of_eratosthenes(n):
    # 각 수가 소수인지를 나타내는 리스트 생성
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # 2부터 제곱근(n)까지 반복하여 소수 여부를 체크
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            # 소수인 경우, 해당 소수의 배수는 모두 소수가 아니므로 False로 설정
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # 소수만을 담은 리스트 생성
    primes = [x for x in range(n + 1) if is_prime[x]]
    return primes

# 입력 받기
N, M = map(int, input().split())

# M 이하의 소수 구하기
primes = sieve_of_eratosthenes(M)

# N보다 크거나 같은 소수 출력
for prime in primes:
    if prime >= N:
        print(prime)

