#พีรพัฒน์ สุทธิประสิทธิ์ - 6410742651
#circular_area
import math
def area_of_circular_sector(r, d):
    sector_area = (d/360)*(math.pi)*(r**2)
    return sector_area

area_1 = area_of_circular_sector(10, 90)
area_2 = area_of_circular_sector(10, 180)
print(f"Area 1 = {area_1:.2f}, Area 2 = {area_2:.3f}")