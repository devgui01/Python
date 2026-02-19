#!/usr/bin/env python3
"""Find duplicate GitHub issues"""

import subprocess
import json
from collections import defaultdict

# Get all issues
result = subprocess.run(
    ["gh", "issue", "list", "--state", "open", "--limit", "1000", "--json", "number,title,labels"],
    capture_output=True, text=True
)
issues = json.loads(result.stdout)

# Group by keywords
duplicates = defaultdict(list)

for issue in issues:
    num = issue['number']
    title = issue['title'].lower()
    
    # Extract keywords from title
    keywords = []
    if 'converter' in title:
        if 'temperature' in title: keywords.append('temperature_converter')
        elif 'currency' in title: keywords.append('currency_converter')
        elif 'binary' in title and 'decimal' in title: keywords.append('binary_decimal_converter')
        elif 'decimal' in title and 'binary' in title: keywords.append('decimal_binary_converter')
        elif 'unit' in title: keywords.append('unit_converter')
        elif 'case' in title: keywords.append('case_converter')
        else: keywords.append('general_converter')
    
    if 'calculator' in title:
        if 'simple interest' in title: keywords.append('simple_interest_calc')
        elif 'grade' in title: keywords.append('grade_calculator')
        elif 'age' in title: keywords.append('age_calculator')
        elif 'tip' in title: keywords.append('tip_calculator')
        elif 'bmi' in title: keywords.append('bmi_calculator')
        elif 'factorial' in title: keywords.append('factorial_calc')
        elif 'gcd' in title: keywords.append('gcd_calc')
        elif 'lcm' in title: keywords.append('lcm_calc')
        elif 'area' in title: keywords.append('area_calculator')
        elif 'simple calculator' in title: keywords.append('simple_calculator')
        else: keywords.append('general_calculator')
    
    if 'checker' in title:
        if 'prime' in title: keywords.append('prime_checker')
        elif 'palindrome' in title: keywords.append('palindrome_checker')
        elif 'leap year' in title: keywords.append('leap_year_checker')
        elif 'anagram' in title: keywords.append('anagram_checker')
        elif 'password' in title: keywords.append('password_checker')
        elif 'odd' in title or 'even' in title: keywords.append('odd_even_checker')
        elif 'vowel' in title: keywords.append('vowel_checker')
        else: keywords.append('general_checker')
    
    if 'counter' in title:
        if 'vowel' in title: keywords.append('vowel_counter')
        elif 'word' in title: keywords.append('word_counter')
        elif 'digit' in title: keywords.append('digit_counter')
        else: keywords.append('general_counter')
    
    if 'generator' in title:
        if 'password' in title: keywords.append('password_generator')
        elif 'quote' in title: keywords.append('quote_generator')
        elif 'random' in title: keywords.append('random_generator')
        else: keywords.append('general_generator')
    
    for kw in keywords:
        duplicates[kw].append(num)

# Print duplicates
print("=== DUPLICATE GROUPS ===\n")
for kw, nums in sorted(duplicates.items()):
    if len(nums) > 1:
        print(f"{kw}: {nums}")

print("\n=== SUMMARY ===")
total_dups = sum(1 for nums in duplicates.values() if len(nums) > 1)
print(f"Duplicate groups found: {total_dups}")
