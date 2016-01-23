import math

ab = int(input())
bc = int(input())
h = math.sqrt(ab ** 2 + bc ** 2)
mb = math.sqrt((2 * ab ** 2 + 2 * bc ** 2 - h ** 2) / 4)
angle = math.acos((mb ** 2 + bc ** 2 - (h / 2) ** 2) / (2 * mb * bc))
print(str(int(round(math.degrees(angle)))) + "°")
