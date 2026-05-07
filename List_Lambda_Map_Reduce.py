from functools import reduce

# మన దగ్గర ఉన్న నంబర్ల లిస్ట్
numbers = [1, 2, 3, 4, 5]

# 1. List Comprehension: కేవలం సరిసంఖ్యలను (Even numbers) మాత్రమే తీసుకుంటుంది
even_numbers = [x for x in numbers if x % 2 == 0]
print("1. List Comprehension (Even numbers):", even_numbers) 
# అవుట్‌పుట్: [2, 4]

# 2. Lambda Expression: ఒక నంబర్‌ని డబుల్ చేసే చిన్న ఫంక్షన్
double = lambda x: x * 2

# 3. Map: లిస్ట్‌లోని ప్రతి నంబర్‌ని 'double' ఫంక్షన్‌తో డబుల్ చేస్తుంది
doubled_numbers = list(map(double, numbers))
print("2. Map (Doubled numbers):", doubled_numbers) 
# అవుట్‌పుట్: [2, 4, 6, 8, 10]

# 4. Reduce: లిస్ట్‌లోని నంబర్లన్నింటినీ కలిపి మొత్తాన్ని (Sum) కనుగొంటుంది
total_sum = reduce(lambda x, y: x + y, numbers)
print("3. Reduce (Total sum):", total_sum) 
# అవుట్‌పుట్: 15 (అంటే 1+2+3+4+5)



