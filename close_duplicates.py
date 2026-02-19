#!/usr/bin/env python3
"""Close duplicate GitHub issues, keeping the best version"""

import subprocess
import time

# Duplicate groups - keep first (usually oldest/best), close rest
DUPLICATES = {
    'age_calculator': {'keep': 197, 'close': [1549, 1337]},
    'anagram_checker': {'keep': 1304, 'close': [1356]},
    'area_calculator': {'keep': 213, 'close': [1192]},
    'binary_decimal_converter': {'keep': 1310, 'close': [1307]},
    'bmi_calculator': {'keep': 128, 'close': [1259]},
    'case_converter': {'keep': 138, 'close': [1564, 1296]},
    'currency_converter': {'keep': 1272, 'close': [1366, 1124]},
    'factorial_calc': {'keep': 1350, 'close': [1282]},
    'general_calculator': {'keep': 159, 'close': [1596, 1412, 1407, 1405, 1401, 1393, 1386, 1373, 1369, 1196, 1194, 1149, 206, 199, 189, 185, 156]},
    'general_checker': {'keep': 215, 'close': [1476, 1334, 1325, 1290, 1166]},
    'general_converter': {'keep': 188, 'close': [1572, 1365, 1362, 1346, 1238, 1189, 1142, 1140, 1131, 1123, 65]},
    'general_counter': {'keep': 234, 'close': [1562, 1399, 1383, 1359]},
    'general_generator': {'keep': 111, 'close': [1585, 1511, 1492, 1446, 1382, 1376, 1354, 1322, 1293, 1286, 1263, 1260, 1255, 1253, 1245, 1219, 1211, 1171, 1147, 1134, 1128, 230, 212, 204, 196, 194]},
    'grade_calculator': {'keep': 1336, 'close': [1410]},
    'leap_year_checker': {'keep': 1331, 'close': [1278]},
    'palindrome_checker': {'keep': 136, 'close': [1555, 1302, 1301]},
    'password_checker': {'keep': 129, 'close': [1428, 1125]},
    'password_generator': {'keep': 1129, 'close': [1580, 1315, 1266]},
    'prime_checker': {'keep': 3, 'close': [1360, 1288]},
    'simple_calculator': {'keep': 202, 'close': [1185]},
    'simple_interest_calc': {'keep': 1175, 'close': [1247]},
    'temperature_converter': {'keep': 1177, 'close': [1249, 127]},
    'tip_calculator': {'keep': 198, 'close': [1291, 1256]},
    'unit_converter': {'keep': 113, 'close': [1297, 1265]},
    'vowel_counter': {'keep': 1279, 'close': [1558, 1299]},
    'word_counter': {'keep': 211, 'close': [1385, 1349, 1289, 1119, 1096]},
}

total_closed = 0

for group, data in DUPLICATES.items():
    keep = data['keep']
    close_list = data['close']
    
    print(f"\nGroup: {group}")
    print(f"  Keeping: #{keep}")
    
    for num in close_list:
        comment = f"Duplicate of #{keep} - closing to consolidate issues"
        cmd = ["gh", "issue", "close", str(num), "--comment", comment]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"  ✓ Closed: #{num}")
            total_closed += 1
        else:
            print(f"  ✗ Failed: #{num} - {result.stderr}")
        
        time.sleep(2)  # Rate limiting

print(f"\n{'='*50}")
print(f"Total duplicates closed: {total_closed}")
print(f"{'='*50}")
