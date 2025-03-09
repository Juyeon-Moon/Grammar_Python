# 문자열 메소드
# 1. count()
hobby = 'knitting'
print(hobby.count('i')) # hobby에 할당된 'knitting'에 있는 i의 개수를 반환함

# 2. find()
print(hobby.find('k')) # 'knitting'에서 k의 인덱스를 찾아서 반환함.
print(hobby.find('e')) # hobby의 값에 없는 걸 매개변수로 주면 -1을 반환

# 3.index()
print(hobby.index('n'))

# 4.join()
hobby = ",".join('knitting')
print(hobby)