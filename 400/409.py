# 409

nami_votes = 0
chopper_votes = 0
null_votes = 0

for _ in range(5):
    vote = int(input())
    if vote == 1:
        nami_votes += 1
    elif vote == 2:
        chopper_votes += 1
    else:
        null_votes += 1

    print(f"Total votes of No.1 Nami = {nami_votes}")
    print(f"Total votes of No.2 Chopper = {chopper_votes}")
    print(f"Total null votes = {null_votes}")

if nami_votes > chopper_votes:
    print("=> Nami won the election.")
elif chopper_votes > nami_votes:
    print("=> Chopper won the election.")
else:
    print("=> No one won the election.")
