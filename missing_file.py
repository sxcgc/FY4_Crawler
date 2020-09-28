with open("has_geo_has_fdi.txt") as f:
    f_has = sorted(f.readlines())

with open("FY4A_2020JJA_FDI.txt") as f:
    f_all = sorted(f.readlines())

f_has_flag = [ff.split("MULT_NOM_")[-1][:-1].split("_")[0] for ff in f_has]
f_all_flag = [ff.split("MULT_NOM_")[-1][:-1].split("_")[0] for ff in f_all]

#print(f_all_flag)
# print(f_has_flag)
for i, f in enumerate(f_has_flag):
    if f not in f_all_flag:
        print(f_has[i], end="")

