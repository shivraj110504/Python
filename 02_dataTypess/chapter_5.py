import sys

ideal_temp = 95.5
current_temp = 95.49999999999999

print(f"ideal temperature {ideal_temp}")  #=> ideal temperature 95.55
print(f"current temperature {current_temp}")  #=> current temperature 95.499999
print(f"Difference: { ideal_temp - current_temp}")  #=> Difference: 1.4210854715202004e-14

print(sys.float_info)  #=> gives information about the float representation