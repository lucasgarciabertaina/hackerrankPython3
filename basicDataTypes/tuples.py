# https://www.hackerrank.com/challenges/python-tuples/problem?h_r=next-challenge&h_v=zen
n = int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))
